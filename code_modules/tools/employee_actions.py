from datetime import datetime, timedelta
from pathlib import Path
import shutil
import uuid


EMPLOYEES = {}
LEAVE_BALANCES = {}
TIME_OFF_REQUESTS = {}
DOCUMENT_ARCHIVE = {}


def create_employee_profile(first_name, last_name, email, role, salary, start_date):
    employee_id = f"EMP-{uuid.uuid4().hex[:8].upper()}"

    employee = {
        "employee_id": employee_id,
        "first_name": first_name,
        "last_name": last_name,
        "full_name": f"{first_name} {last_name}",
        "email": email,
        "role": role,
        "salary": salary,
        "start_date": start_date,
        "status": "active",
        "created_at": datetime.utcnow().isoformat()
    }

    EMPLOYEES[employee_id] = employee

    LEAVE_BALANCES[employee_id] = {
        "vacation": 15,
        "sick": 10,
        "personal": 3
    }

    return employee


def setup_employee_directory(employee_id):
    if employee_id not in EMPLOYEES:
        return {"status": "error", "message": "Employee not found."}

    employee = EMPLOYEES[employee_id]

    return {
        "status": "success",
        "employee_id": employee_id,
        "directory_record": {
            "display_name": employee["full_name"],
            "email": employee["email"],
            "role": employee["role"],
            "groups": ["all-employees", employee["role"].lower().replace(" ", "-")]
        }
    }


def generate_offer_letter(employee_name, role, salary):
    return f"""
Dear {employee_name},

We are pleased to offer you the position of {role}.

Your starting annual salary will be ${salary:,.2f}. This offer is subject to completion of standard onboarding requirements.

We are excited about the possibility of you joining our team.

Sincerely,
HR Team
""".strip()


def check_leave_balance(employee_id, leave_type):
    balance = LEAVE_BALANCES.get(employee_id)

    if not balance:
        return {"status": "error", "message": "Employee leave balance not found."}

    leave_type = leave_type.lower()

    return {
        "employee_id": employee_id,
        "leave_type": leave_type,
        "remaining_days": balance.get(leave_type, 0)
    }


def request_time_off(employee_id, start_date, end_date, leave_type):
    if employee_id not in EMPLOYEES:
        return {"status": "error", "message": "Employee not found."}

    start = datetime.fromisoformat(start_date)
    end = datetime.fromisoformat(end_date)
    days_requested = (end - start).days + 1

    balance = check_leave_balance(employee_id, leave_type)

    if balance.get("status") == "error":
        return balance

    if balance["remaining_days"] < days_requested:
        return {
            "status": "denied",
            "reason": "Insufficient leave balance.",
            "days_requested": days_requested,
            "remaining_days": balance["remaining_days"]
        }

    request_id = f"REQ-{uuid.uuid4().hex[:8].upper()}"

    TIME_OFF_REQUESTS[request_id] = {
        "request_id": request_id,
        "employee_id": employee_id,
        "start_date": start_date,
        "end_date": end_date,
        "leave_type": leave_type.lower(),
        "days_requested": days_requested,
        "status": "pending",
        "created_at": datetime.utcnow().isoformat()
    }

    return TIME_OFF_REQUESTS[request_id]


def update_leave_status(request_id, status):
    if request_id not in TIME_OFF_REQUESTS:
        return {"status": "error", "message": "Time-off request not found."}

    status = status.lower()

    if status not in {"approved", "denied", "pending"}:
        return {
            "status": "error",
            "message": "Status must be approved, denied, or pending."
        }

    request = TIME_OFF_REQUESTS[request_id]
    request["status"] = status
    request["updated_at"] = datetime.utcnow().isoformat()

    if status == "approved":
        employee_id = request["employee_id"]
        leave_type = request["leave_type"]
        days = request["days_requested"]

        LEAVE_BALANCES[employee_id][leave_type] -= days

    return request


def archive_employee_document(employee_id, uploaded_file_path, doc_type):
    if employee_id not in EMPLOYEES:
        return {"status": "error", "message": "Employee not found."}

    source = Path(uploaded_file_path)

    if not source.exists():
        return {"status": "error", "message": "Uploaded file not found."}

    archive_dir = Path("employee_documents") / employee_id
    archive_dir.mkdir(parents=True, exist_ok=True)

    destination = archive_dir / f"{doc_type}_{source.name}"
    shutil.copy(source, destination)

    record = {
        "employee_id": employee_id,
        "doc_type": doc_type,
        "archived_path": str(destination),
        "archived_at": datetime.utcnow().isoformat()
    }

    DOCUMENT_ARCHIVE.setdefault(employee_id, []).append(record)

    return {
        "status": "success",
        "document": record
    }


def scan_expiring_credentials():
    today = datetime.utcnow().date()

    mock_credentials = [
        {
            "employee_id": "EMP-EXAMPLE1",
            "credential": "Work Authorization",
            "expires_on": today + timedelta(days=20)
        },
        {
            "employee_id": "EMP-EXAMPLE2",
            "credential": "Safety Certification",
            "expires_on": today + timedelta(days=75)
        }
    ]

    expiring_soon = [
        item for item in mock_credentials
        if item["expires_on"] <= today + timedelta(days=30)
    ]

    return {
        "status": "success",
        "expiring_within_days": 30,
        "credentials": [
            {
                **item,
                "expires_on": item["expires_on"].isoformat()
            }
            for item in expiring_soon
        ]
    }


def alert_policy_update(changed_policy_name):
    return {
        "status": "sent",
        "message": f"Policy update alert sent for: {changed_policy_name}",
        "channels": ["email", "slack"],
        "sent_at": datetime.utcnow().isoformat()
    }


def send_announcement_to_slack(message, channel="#general"):
    return {
        "status": "sent",
        "platform": "slack",
        "channel": channel,
        "message": message,
        "sent_at": datetime.utcnow().isoformat()
    }


def schedule_onboarding_meetings(employee_id, manager_email):
    if employee_id not in EMPLOYEES:
        return {"status": "error", "message": "Employee not found."}

    employee = EMPLOYEES[employee_id]
    start_date = datetime.fromisoformat(employee["start_date"])

    meetings = [
        {
            "title": "HR Orientation",
            "attendees": [employee["email"], "hr@example.com"],
            "scheduled_for": start_date.replace(hour=9, minute=0).isoformat()
        },
        {
            "title": "Manager 1:1",
            "attendees": [employee["email"], manager_email],
            "scheduled_for": start_date.replace(hour=11, minute=0).isoformat()
        },
        {
            "title": "Benefits Overview",
            "attendees": [employee["email"], "benefits@example.com"],
            "scheduled_for": start_date.replace(hour=14, minute=0).isoformat()
        }
    ]

    return {
        "status": "scheduled",
        "employee_id": employee_id,
        "meetings": meetings
    }


def onboard_new_hire(first_name, last_name, email, role, salary, start_date):
    employee = create_employee_profile(
        first_name=first_name,
        last_name=last_name,
        email=email,
        role=role,
        salary=salary,
        start_date=start_date
    )

    directory = setup_employee_directory(employee["employee_id"])

    offer_letter = generate_offer_letter(
        employee_name=employee["full_name"],
        role=role,
        salary=salary
    )

    announcement = send_announcement_to_slack(
        message=f"Please welcome {employee['full_name']} as our new {role}!",
        channel="#general"
    )

    onboarding = schedule_onboarding_meetings(
        employee_id=employee["employee_id"],
        manager_email="manager@example.com"
    )

    return {
        "status": "success",
        "employee": employee,
        "directory_setup": directory,
        "offer_letter": offer_letter,
        "announcement": announcement,
        "onboarding_meetings": onboarding
    }
