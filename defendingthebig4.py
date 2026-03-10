import pytest


# 1. THE LIST: "The Content & Order Guard"
# Scenario: Ensuring a list is sorted and has the right length.
def test_list_integrity():
    students = ["Alice", "Bob", "Charlie"]

    # Positive: Check length and specific position
    assert len(students) == 3
    assert students[0] == "Alice"

    # Negative: Proving it's NOT a different type
    assert not isinstance(students, tuple)


# 2. THE TUPLE: "The Immutability Proof"
# Scenario: Proving that data in a tuple CANNOT be changed (it should crash).
def test_tuple_safety_crash():
    coordinates = (37.77, -122.41)

    # This is how we test for a CRASH (TypeError)
    with pytest.raises(TypeError):
        coordinates[0] = 40.0  # This MUST fail in Python


# 3. THE SET: "The Duplicate Filter"
# Scenario: Ensuring a list with duplicates is properly cleaned.
def test_set_deduplication():
    raw_data = ["red", "blue", "red", "green"]
    clean_data = set(raw_data)

    # Logical Assert: Proving duplicates are gone
    assert len(clean_data) == 3
    assert "red" in clean_data
    # Proving an item is GONE
    assert len(clean_data) < len(raw_data)


# 4. THE DICTIONARY: "The Key-Value Lock"
# Scenario: Checking for a specific key and its data type.
def test_dict_validation():
    user_profile = {"id": 101, "role": "admin"}

    # Positive: Check value
    assert user_profile["role"] == "admin"

    # Negative: Accessing a missing key should raise a KeyError
    with pytest.raises(KeyError):
        print(user_profile["password"])


# 5. THE "TYPE MIX" GUARD: "The Schema Check"
# Scenario: Checking a Dictionary that contains a List (Common in Agile).
def test_nested_structure():
    sprint = {"tasks": ["Code", "Test"], "complete": False}

    # Ensure 'tasks' is specifically a list, not a string
    assert isinstance(sprint["tasks"], list)
    # Ensure the list isn't empty
    assert len(sprint["tasks"]) > 0


# 6. THE BOUNDARY CATCH: "The Empty List Risk"
# Scenario: Ensuring our code doesn't try to process an empty structure.
def test_empty_collection_guard():
    results = []  # Oops, empty!

    # Defensive logic: Asserting that the collection MUST have data
    with pytest.raises(AssertionError) as excinfo:
        assert len(results) > 0, "DATA ERROR: Collection is empty!"
    assert "Collection is empty" in str(excinfo.value)

"""
Testing the Crash (Test 2 & 4): Show the students that in QA, we want the TypeError and KeyError to happen when the data is wrong. If the code doesn't crash when we try to change a Tuple, the system is broken!

Schema Validation (Test 5): This is a "Senior QA" move. We aren't just checking the data; we are checking the structure (is the "Value" actually a "List"?).

The Message (Test 6): Notice the custom message "DATA ERROR: Collection is empty!". Tell the students: "A crash without a message is a nightmare for the developer. A crash with a clear message is a roadmap to a fix."
"""
