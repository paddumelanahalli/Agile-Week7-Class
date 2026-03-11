# Agile Sprint Tracker
# Reorganizes a backlog by developer and removes duplicate tasks

def organize_backlog(backlog):
    """
    Takes a backlog (list of task dictionaries)
    Returns a dictionary: {developer: [unique tasks]}
    """

    # Defensive check: backlog must be a list
    assert isinstance(backlog, list), "Backlog must be a list!"

    sprint_board = {}

    for item in backlog:
        # Validate structure
        assert isinstance(item, dict), "Each backlog item must be a dictionary"
        assert "developer" in item and "task" in item, "Each item must contain 'developer' and 'task'"

        dev = item["developer"]
        task = item["task"]

        # If developer not yet in dictionary, create entry
        if dev not in sprint_board:
            sprint_board[dev] = []

        # Add task only if it's not already assigned
        if task not in sprint_board[dev]:
            sprint_board[dev].append(task)

    return sprint_board


# --- MAIN PROGRAM ---

if __name__ == "__main__":

    # Example backlog with duplicates
    backlog = [
        {"developer": "Alice", "task": "Login API"},
        {"developer": "Bob", "task": "Database Schema"},
        {"developer": "Alice", "task": "JWT Authentication"},
        {"developer": "Bob", "task": "Database Schema"},  # duplicate
        {"developer": "Charlie", "task": "Frontend UI"},
        {"developer": "Alice", "task": "Login API"}  # duplicate
    ]

    print("=== ORIGINAL BACKLOG ===")
    for item in backlog:
        print(item)

    print("\n=== ORGANIZED SPRINT BOARD ===")

    sprint_board = organize_backlog(backlog)

    for dev, tasks in sprint_board.items():
        print(f"{dev}: {tasks}")

    print("\n=== OVERLOAD CHECK ===")

    # Example logic: identify overloaded developers
    for dev, tasks in sprint_board.items():
        if len(tasks) > 2:
            print(f"WARNING: {dev} may be overloaded ({len(tasks)} tasks)")
"""
output:
=== ORIGINAL BACKLOG ===
{'developer': 'Alice', 'task': 'Login API'}
{'developer': 'Bob', 'task': 'Database Schema'}
{'developer': 'Alice', 'task': 'JWT Authentication'}
{'developer': 'Bob', 'task': 'Database Schema'}
{'developer': 'Charlie', 'task': 'Frontend UI'}
{'developer': 'Alice', 'task': 'Login API'}

=== ORGANIZED SPRINT BOARD ===
Alice: ['Login API', 'JWT Authentication']
Bob: ['Database Schema']
Charlie: ['Frontend UI']

=== OVERLOAD CHECK ===

Process finished with exit code 0
"""
