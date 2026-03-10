"""
1. The LIST [] (The "Queue")
Feature: Ordered and Changeable (Mutable).

QA Risk: Slow to search if it has millions of items.

Use Case: A list of student names waiting for a grade.
"""
students = ["Alice", "Bob", "Charlie"]
students.append("Paddu") # Easy to add to!

"""
2. The TUPLE () (The "Vault")
Feature: Ordered but Unchangeable (Immutable).

QA Risk: If you try to change it, Python crashes.

Use Case: Constants like GPS coordinates or the UCSC Domain name.
"""
ucsc_info = ("Santa Cruz", 95064, "ucsc.edu")
# ucsc_info[0] = "San Jose"  <-- THIS WILL TRIGGER A CRASH


"""
3. THE SET {} (The "Filter")
Feature: Unordered and No Duplicates.

QA Power: Instant searching. Great for cleaning "dirty" data.

Use Case: Finding how many unique visitors came to a website.
"""
raw_data = ["Alice", "Bob", "Alice", "Charlie"]
unique_students = set(raw_data) # Result: {'Alice', 'Bob', 'Charlie'}

"""
4. THE DICTIONARY {:} (The "Map")
Feature: Key-Value pairs.

QA Power: The fastest way to look up specific info.

Use Case: A student ID (Key) linked to a Grade (Value).
"""
grade_book = {"12345": "A", "67890": "B+"}
print(grade_book["12345"]) # Result: A
"""
PRACTICE CHALLENGE: "THE DATA CLEANER"

The Scenario: You received a list of 100 emails, but many are duplicates and some are formatted badly.
"""


def clean_enrollment(email_list):
    # 1. Use a SET to automatically remove duplicates
    unique_emails = set(email_list)

    # 2. Use a LIST to sort them alphabetically for the report
    sorted_emails = sorted(list(unique_emails))

    # 3. Use a DICTIONARY to count how many are from 'ucsc.edu'
    report = {"ucsc": 0, "other": 0}

    for email in sorted_emails:
        if email.endswith("ucsc.edu"):
            report["ucsc"] += 1
        else:
            report["other"] += 1

    return sorted_emails, report


# Test it
test_emails = ["paddu@ucsc.edu", "student@gmail.com", "paddu@ucsc.edu"]
emails, stats = clean_enrollment(test_emails)
print(emails)  # ['paddu@ucsc.edu', 'student@gmail.com']
print(stats)  # {'ucsc': 1, 'other': 1}

"""
"If I have 1,000,000 usernames and I need to check if 'Paddu' is one of them, should I store them in a List or a Set? Why?"
(Answer for you: A Set. Checking a List takes $O(n)$ time—it looks at every item. Checking a Set takes $O(1)$ time—it's instant!)
"""
