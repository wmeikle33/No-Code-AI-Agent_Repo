# tests/test_validation_errors.py

import pytest

from code_modules.tools.lead_capture import create_lead


def test_create_lead_rejects_missing_email():
    with pytest.raises(ValueError):
        create_lead(
            name="Jane Doe",
            email="",
            interest="AI Support Agent",
        )


def test_create_lead_rejects_invalid_email():
    with pytest.raises(ValueError):
        create_lead(
            name="Jane Doe",
            email="not-an-email",
            interest="AI Support Agent",
        )
