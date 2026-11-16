from ai_tickets import find_severity, find_unsupported_numbers


def test_find_severity_reads_the_header():
    assert find_severity("**Found by:** · **Date found:** · **Severity:** Medium\n") == "Medium"


def test_find_severity_rejects_anything_else():
    assert find_severity("**Severity:** Medium, set by the tracking plan.\n") is None


def test_unsupported_numbers_ignore_thousands_separators():
    assert find_unsupported_numbers("1,533 records on Nov 1, 2020", "1533 records on Nov 1, 2020") == set()