import pandas as pd

def generate_balance_sheet(assets: dict, liabilities: dict, equity: dict):
    total_assets = sum(assets.values())
    total_liabilities = sum(liabilities.values())
    total_equity = sum(equity.values())
    total_liabilities_and_equity = total_liabilities + total_equity

    is_balanced = round(total_assets, 2) == round(
        total_liabilities_and_equity, 2
    )

    statement_data = []

    def append_section(section_title, items_dict, section_total):
        statement_data.append(
            {"Category": f"--- {section_title.upper()} ---", "Amount ($)": ""}
        )
        for key, val in items_dict.items():
            statement_data.append({"Category": f"  {key}", "Amount ($)": val})
        statement_data.append(
            {"Category": f"TOTAL {section_title.upper()}", "Amount ($)": round(section_total, 2)}
        )
        statement_data.append({"Category": "", "Amount ($)": ""})  # Spacer row

    append_section("Assets", assets, total_assets)
    append_section("Liabilities", liabilities, total_liabilities)
    append_section("Owner's Equity", equity, total_equity)

    statement_data.append(
        {
            "Category": "TOTAL LIABILITIES & EQUITY",
            "Amount ($)": round(total_liabilities_and_equity, 2),
        }
    )
    statement_data.append(
        {"Category": "EQUATION STATUS", "Amount ($)": "BALANCED" if is_balanced else "UNBALANCED!"}
    )

    df = pd.DataFrame(statement_data)
    return df, is_balanced

def generate_income_statement(revenue: float, cogs: float, opex: dict, interest: float, tax_rate: float):
    statement_lines = []
    
    gross_profit = revenue - cogs
    
    statement_lines.append({"Line Item": "Total Revenue", "Amount ($)": float(revenue)})
    statement_lines.append({"Line Item": "  Less: Cost of Goods Sold (COGS)", "Amount ($)": -float(cogs)})
    statement_lines.append({"Line Item": "GROSS PROFIT", "Amount ($)": float(gross_profit)})
    statement_lines.append({"Line Item": "", "Amount ($)": ""})  # Spacer
    
    statement_lines.append({"Line Item": "Operating Expenses (OPEX):", "Amount ($)": ""})
    total_opex = 0.0
    for expense_name, amount in opex.items():
        statement_lines.append({"Line Item": f"  {expense_name}", "Amount ($)": -float(amount)})
        total_opex += amount
        
    operating_income = gross_profit - total_opex
    statement_lines.append({"Line Item": "Total Operating Expenses", "Amount ($)": -float(total_opex)})
    statement_lines.append({"Line Item": "OPERATING INCOME (EBIT)", "Amount ($)": float(operating_income)})
    statement_lines.append({"Line Item": "", "Amount ($)": ""})  # Spacer
    
    pretax_income = operating_income - interest
    statement_lines.append({"Line Item": "  Less: Interest Expense", "Amount ($)": -float(interest)})
    statement_lines.append({"Line Item": "INCOME BEFORE TAXES (EBT)", "Amount ($)": float(pretax_income)})
    
    taxes = pretax_income * tax_rate if pretax_income > 0 else 0.0
    net_income = pretax_income - taxes
    
    statement_lines.append({"Line Item": f"  Less: Income Tax Expense ({int(tax_rate*100)}%)", "Amount ($)": -float(taxes)})
    statement_lines.append({"Line Item": "", "Amount ($)": ""})  # Spacer
    statement_lines.append({"Line Item": "NET INCOME", "Amount ($)": float(net_income)})
    
    df = pd.DataFrame(statement_lines)
    return df

def generate_cash_flow_statement(
    net_income: float,
    non_cash_items: dict,
    working_capital_changes: dict,
    investing_activities: dict,
    financing_activities: dict,
    beginning_cash: float,
):
    statement_lines = []

    statement_lines.append(
        {"Component": "--- CASH FLOWS FROM OPERATING ACTIVITIES ---", "Amount ($)": ""}
    )
    statement_lines.append(
        {"Component": "Net Income", "Amount ($)": float(net_income)}
    )

    total_non_cash = 0.0
    for item, amount in non_cash_items.items():
        statement_lines.append(
            {"Component": f"  Add: {item}", "Amount ($)": float(amount)}
        )
        total_non_cash += amount

    total_wc_changes = 0.0
    for item, amount in working_capital_changes.items():
        statement_lines.append(
            {"Component": f"  Change in {item}", "Amount ($)": float(amount)}
        )
        total_wc_changes += amount

    net_operating_cash = net_income + total_non_cash + total_wc_changes
    statement_lines.append(
        {
            "Component": "Net Cash Provided by Operating Activities",
            "Amount ($)": net_operating_cash,
        }
    )
    statement_lines.append({"Component": "", "Amount ($)": ""})  # Spacer

    statement_lines.append(
        {"Component": "--- CASH FLOWS FROM INVESTING ACTIVITIES ---", "Amount ($)": ""}
    )
    net_investing_cash = 0.0
    for item, amount in investing_activities.items():
        statement_lines.append(
            {"Component": f"  {item}", "Amount ($)": float(amount)}
        )
        net_investing_cash += amount

    statement_lines.append(
        {
            "Component": "Net Cash Used in Investing Activities",
            "Amount ($)": net_investing_cash,
        }
    )
    statement_lines.append({"Component": "", "Amount ($)": ""})  # Spacer

    statement_lines.append(
        {"Component": "--- CASH FLOWS FROM FINANCING ACTIVITIES ---", "Amount ($)": ""}
    )
    net_financing_cash = 0.0
    for item, amount in financing_activities.items():
        statement_lines.append(
            {"Component": f"  {item}", "Amount ($)": float(amount)}
        )
        net_financing_cash += amount

    statement_lines.append(
        {
            "Component": "Net Cash Provided by Financing Activities",
            "Amount ($)": net_financing_cash,
        }
    )
    statement_lines.append({"Component": "", "Amount ($)": ""})  # Spacer

    net_change_in_cash = (
        net_operating_cash + net_investing_cash + net_financing_cash
    )
    ending_cash = beginning_cash + net_change_in_cash

    statement_lines.append(
        {
            "Component": "NET INCREASE (DECREASE) IN CASH",
            "Amount ($)": net_change_in_cash,
        }
    )
    statement_lines.append(
        {
            "Component": "Cash at Beginning of Year",
            "Amount ($)": float(beginning_cash),
        }
    )
    statement_lines.append(
        {"Component": "CASH AT END OF YEAR", "Amount ($)": ending_cash}
    )

    df = pd.DataFrame(statement_lines)
    return df
