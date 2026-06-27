from code_modules.routing.escalation import should_escalate


def test_escalates_angry_customer():
    assert should_escalate("I am very angry and want a refund now") is True


def test_escalates_legal_threat():
    assert should_escalate("I will contact my lawyer") is True


def test_does_not_escalate_normal_question():
    assert should_escalate("How do I reset my password?") is False
