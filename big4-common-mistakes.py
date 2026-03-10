def process_scores_shallow(scores):
    """Only checks the 'Box' (Is it a list?)"""
    assert isinstance(scores, list), "ERROR: Must be a list!"
    # PITFALL: If the list contains a string, this line crashes the program!
    return sum(scores)


def process_scores_deep(scores):
    """Checks the 'Box' AND the 'Contents'"""
    assert isinstance(scores, list), "ERROR: Must be a list!"
    assert len(scores) > 0, "ERROR: List cannot be empty!"

    # THE DEEP GUARD: Ensure every item is a number (int or float)
    assert all(isinstance(s, (int, float)) for s in scores), "CRITICAL: All scores must be numeric!"

    return sum(scores)


if __name__ == "__main__":
    # Case 1: The "Dirty" Data
    # A list of numbers, but someone accidentally typed "A" instead of 90.
    dirty_data = [85, 92, "A", 78]

    print("--- Starting QA Audit ---")

    # TEST 1: The Shallow Failure
    try:
        print("Attempting Shallow Validation...")
        result = process_scores_shallow(dirty_data)
        print(f"Result: {result}")
    except TypeError as e:
        print(f"FAILED: The Shallow Check let bad data in, and Python CRASHED with: {e}")

    print("-" * 30)

    # TEST 2: The Deep Success
    try:
        print("Attempting Deep Validation...")
        result = process_scores_deep(dirty_data)
        print(f"Result: {result}")
    except AssertionError as e:
        print(f"SUCCESS: The Deep Guard caught the bad data early! Error Message: {e}")

    print("--- Audit Complete ---")

"""
The "Try/Except" logic: It shows students how to "trap" a crash so the whole system doesn't go down.

The all() function: This is a "Big 4" power move. It’s the most efficient way to scan a List or Set for integrity.

The TypeError vs. AssertionError: * In Test 1, the Language (Python) crashed.

In Test 2, the QA Shield (Assert) stopped it.

"Students, you want your Assert to catch the error before Python crashes. If Python crashes, you didn't do your job as a QA Engineer."
"""
