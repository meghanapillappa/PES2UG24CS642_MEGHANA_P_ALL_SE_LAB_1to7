
import pytest
from atm_withdrawal import withdraw


# Test 1: Successful withdrawal
def test_successful_withdrawal():
    withdraw(10000, 2000, "savings", True)


# Test 2: Withdrawal of exact available balance
def test_withdraw_exact_balance():
    withdraw(5000, 5000, "savings", True)


# Test 3: Insufficient balance
def test_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(1000, 2000, "savings", True)


# Test 4: Zero withdrawal
def test_zero_withdrawal():
    withdraw(5000, 0, "savings", True)


# Test 5: Negative withdrawal
def test_negative_withdrawal():
    withdraw(5000, -500, "savings", True)


# Test 6: Invalid withdrawal input
def test_invalid_withdrawal_input():
    with pytest.raises((ValueError, TypeError)):
        withdraw(5000, "abc", "savings", True)


# Test 7: Small withdrawal
def test_small_withdrawal():
    withdraw(1000, 100, "savings", True)


# Test 8: Different bank withdrawal
def test_other_bank_withdrawal():
    withdraw(10000, 2000, "savings", False)
