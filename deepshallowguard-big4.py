# PRO QA TIP: Don't just check the 'Box', check the 'Contents'
"""
def process_data(items):
    assert isinstance(items, list), "Must be a list" # Shallow
    assert all(isinstance(x, int) for x in items), "Contents must be integers" # Deep
"""

import sys


def process_transaction_shallow(data):
    """
    PITFALL: This only checks if the container is a list.
    It does NOT check if the contents are safe to process.
    """
    assert isinstance(data, list), "QA Error: Input must be a list!"

    # This line will CRASH if data contains a string or None
    total = sum(data)
    return total


def process_transaction_deep(data):
    """
    PRO STANDARD: Checks the 'Box' AND the 'Contents'.
    This is true Defensive Programming.
    """
    # 1. Identity Check
    assert isinstance(data, list), "QA Error: Input must be a list!"

    # 2. Size Check
    assert len(data) > 0, "QA Error: Transaction list cannot be empty!"

    # 3. Content Check (The Deep Guard)
    # We use all() to verify every single item is an int or float
    assert all(isinstance(x, (int, float)) for x in data), "CRITICAL: Non-numeric data detected in transactions!"

    return sum(data)


# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    # Test Data: A list that looks okay but has a 'hidden' string error
    dirty_batch = [10.50, 20.00, "Error_500", 5.75]

    print("=== STARTING UCSC QA AUDIT ===")

    # 1. Demonstrate the Shallow Pitfall
    print("\n[TEST 1] Running Shallow Validation...")
    try:
        result = process_transaction_shallow(dirty_batch)
        print(f"Success! Total: {result}")
    except Exception as e:
        print(f"FAILED: Shallow check let bad data in. Python crashed with: {type(e).__name__}")
        print(f"Reason: {e}")

    print("-" * 40)

    # 2. Demonstrate the Deep Defense
    print("[TEST 2] Running Deep Validation...")
    try:
        result = process_transaction_deep(dirty_batch)
        print(f"Success! Total: {result}")
    except AssertionError as error:
        print(f"PASSED: The Deep Guard caught the error before the crash!")
        print(f"QA Shield Message: {error}")

    print("\n=== AUDIT COMPLETE ===")

"""
The Error Type: Note that Test 1 results in a TypeError (Python's internal engine failed), while Test 2 results in an AssertionError (Our QA Shield successfully intercepted the threat).

The all() Function: Explain that this is the most efficient way to perform a deep check on the Big 4 structures. It stops checking as soon as it finds the first error (Short-circuit logic).

The isinstance(x, (int, float)): Show them that they can check for multiple types at once by using a Tuple inside isinstance.
"""
