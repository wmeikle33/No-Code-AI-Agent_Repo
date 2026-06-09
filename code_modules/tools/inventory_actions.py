
def update_inventory(product_name: str, quantity: int, df : pd.DataFrame):
    df[product_name] = quantity
    
def add_product(quantity):
    if sku in inventory:
        inventory[sku]["quantity"] += quantity
        print(f"Updated {name}: New total quantity is {inventory[sku]['quantity']}.")
    else:
        inventory[sku] = {"name": name, "quantity": quantity, "reorder_level": reorder_level}
        print(f"Product {name} added to system.")
        
def reconcile_inventory_channels(warehouse_count: int, ecommerce_count: int) -> dict:
    discrepancy = warehouse_count - ecommerce_count
    
    if discrepancy == 0:
        return {"status": "IN_SYNC", "discrepancy": 0}
    
    return {
        "status": "MISMATCH_DETECTED",
        "discrepancy": discrepancy,
        "action_required": "Sync ecommerce channel to match warehouse" if discrepancy > 0 else "Audit warehouse physical stock"
    }
    
def calculate_inventory_turnover(cogs: float, beginning_inv: float, ending_inv: float) -> float:
    average_inventory = (beginning_inv + ending_inv) / 2
    if average_inventory == 0:
        return 0.0
        
    turnover_ratio = cogs / average_inventory
    return round(turnover_ratio, 2)

def check_stock_health(inventory_list: list[dict]) -> list[dict]:
    items_to_reorder = []
    
    for item in inventory_list:
        if item['current_stock'] <= item['reorder_point']:
            shortage = item['reorder_point'] - item['current_stock']
            items_to_reorder.append({
                "sku": item['sku'],
                "status": "CRITICAL",
                "units_needed": shortage
            })
            
    return items_to_reorder
    
def generate_po_payload(vendor_id: str, items: list[dict], lead_time_days: int) -> dict:
    expected_delivery = datetime.now() + timedelta(days=lead_time_days)
    
    total_cost = sum(item['qty'] * item['unit_cost'] for item in items)
    
    return {
        "po_number": f"PO-{int(datetime.now().timestamp())}",
        "vendor_id": vendor_id,
        "date_created": datetime.now().strftime("%Y-%m-%d"),
        "expected_delivery_date": expected_delivery.strftime("%Y-%m-%d"),
        "items": items,
        "total_order_value": round(total_cost, 2),
        "status": "DRAFT_PENDING_APPROVAL"
    }
def calculate_reorder_point(daily_sales_velocity: float, lead_time_days: int, safety_stock: int) -> int:
    reorder_point = (daily_sales_velocity * lead_time_days) + safety_stock
    return int(reorder_point)
    
def initiate_reorder_function(condition):
    reorder_id = f"PO-{len(REORDER_QUEUE)+1:05d}"

    reorder = {
        "reorder_id": reorder_id,
        "condition": condition,
        "status": "pending",
        "created_at": datetime.utcnow().isoformat()
    }

    REORDER_QUEUE.append(reorder)

    return {
        "status": "success",
        "reorder": reorder
    }
    
def process_sale(sku, quantity_sold):
    if sku not in INVENTORY:
        return {
            "status": "error",
            "message": f"SKU {sku} not found."
        }

    product = INVENTORY[sku]

    if quantity_sold > product["quantity"]:
        return {
            "status": "error",
            "message": "Insufficient inventory."
        }

    product["quantity"] -= quantity_sold

    return {
        "status": "success",
        "sku": sku,
        "quantity_sold": quantity_sold,
        "remaining_inventory": product["quantity"]
    }

def check_reorder_alerts():
    alerts = []

    for sku, item in INVENTORY.items():

        inventory_health = (
            item["quantity"] / item["reorder_point"]
        )

        if inventory_health <= 1:

            alerts.append({
                "sku": sku,
                "risk_level": (
                    "critical"
                    if inventory_health < 0.5
                    else "warning"
                ),
                "current_quantity": item["quantity"],
                "reorder_point": item["reorder_point"],
                "recommended_reorder_quantity": item["reorder_quantity"]
            })

    return {
        "generated_at": datetime.utcnow().isoformat(),
        "alerts_found": len(alerts),
        "alerts": alerts
    }
