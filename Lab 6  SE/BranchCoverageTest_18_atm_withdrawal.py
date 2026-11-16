
import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


# ==========================================
# WITHDRAW FUNCTION TEST CASES
# ==========================================

# Test 1: Successful withdrawal from own bank
def test_successful_withdrawal():
    assert withdraw(10000, 2000, "savings", True) == 8000


# Test 2: Successful withdrawal from current account
def test_current_account_withdrawal():
    assert withdraw(50000, 5000, "current", True) == 45000


# Test 3: Unknown account type
def test_invalid_account():
    with pytest.raises(ValueError):
        withdraw(10000, 1000, "student", True)


# Test 4: Zero withdrawal
def test_zero_withdrawal():
    with pytest.raises(ValueError):
        withdraw(5000, 0, "savings", True)


# Test 5: Negative withdrawal
def test_negative_withdrawal():
    with pytest.raises(ValueError):
        withdraw(5000, -500, "savings", True)


# Test 6: Amount not divisible by 100
def test_invalid_multiple():
    with pytest.raises(ValueError):
        withdraw(5000, 150, "savings", True)


# Test 7: Savings daily limit exceeded
def test_savings_limit_exceeded():
    assert withdraw(50000, 26000, "savings", True) == "limit exceeded"


# Test 8: Current account daily limit exceeded
def test_current_limit_exceeded():
    assert withdraw(60000, 51000, "current", True) == "limit exceeded"


# Test 9: Other bank withdrawal
def test_other_bank_withdrawal():
    assert withdraw(10000, 2000, "savings", False) == 7980


# Test 10: Other bank withdrawal above 10000
def test_other_bank_large_withdrawal():
    assert withdraw(20000, 11000, "savings", False) == 8970


# Test 11: Insufficient balance for own bank
def test_insufficient_funds_own_bank():
    assert withdraw(1000, 2000, "savings", True) == "insufficient funds"


# Test 12: Insufficient balance including bank fee
def test_insufficient_funds_other_bank():
    assert withdraw(1019, 1000, "savings", False) == "insufficient funds"


# ==========================================
# PIN CHECK FUNCTION TEST CASES
# ==========================================

# Test 13: Correct PIN
def test_correct_pin():
    assert pin_check(1234, 1234, 0) == "ok"


# Test 14: Incorrect PIN with attempts remaining
def test_incorrect_pin():
    assert pin_check(1111, 1234, 0) == "retry"


# Test 15: Card blocked after two previous attempts
def test_card_blocked():
    assert pin_check(1111, 1234, 2) == "card blocked"


# Test 16: Card already blocked
def test_card_already_blocked():
    assert pin_check(1234, 1234, 3) == "card blocked"


# Test 17: Correct PIN on final allowed attempt
def test_correct_pin_on_second_attempt():
    assert pin_check(1234, 1234, 2) == "ok"


# ==========================================
# NOTE BREAKUP FUNCTION TEST CASES
# ==========================================

# Test 18: Amount with 500 and 200 notes
def test_note_breakup_700():
    assert note_breakup(700) == (1, 1, 0)


# Test 19: Amount with 500 and 100 notes
def test_note_breakup_600():
    assert note_breakup(600) == (1, 0, 1)


# Test 20: Exact 500 note
def test_note_breakup_500():
    assert note_breakup(500) == (1, 0, 0)


# Test 21: Invalid note breakup amount
def test_invalid_note_breakup():
    with pytest.raises(ValueError):
        note_breakup(550)


# Test 22: Zero note breakup
def test_zero_note_breakup():
    assert note_breakup(0) == (0, 0, 0)
