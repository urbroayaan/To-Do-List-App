FILENAME = "task.txt"


def get_next_id():
    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return 1

    max_id = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split("|")
        if len(parts) != 3:
            continue
        try:
            tid = int(parts[0])
            if tid > max_id:
                max_id = tid
        except ValueError:
            continue

    return max_id + 1


def add_task():
    desc = input("Enter task description: ")
    tid = get_next_id()

    with open(FILENAME, "a") as f:
        f.write(f"{tid}|{desc}|0\n")

    print("Task added.")


def list_tasks():
    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No tasks yet.")
        return

    if not lines:
        print("No tasks yet.")
        return

    print("\nID  Status       Description")
    print("------------------------------")

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split("|")
        if len(parts) != 3:
            continue

        tid, desc, status = parts
        status_text = "Completed" if status == "1" else "Not completed"
        print(f"{tid:<3} {status_text:<12} {desc}")


def mark_complete():
    tid = input("Enter task ID to mark as complete: ")

    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No tasks found.")
        return

    updated = []
    found = False

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split("|")
        if len(parts) != 3:
            continue

        current_id, desc, status = parts

        if current_id == tid:
            status = "1"
            found = True

        updated.append(f"{current_id}|{desc}|{status}\n")

    with open(FILENAME, "w") as f:
        f.writelines(updated)

    if found:
        print("Task marked as complete.")
    else:
        print("Task ID not found.")


def delete_task():
    tid = input("Enter task ID to delete: ")

    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No tasks found.")
        return

    updated = []
    found = False

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split("|")
        if len(parts) != 3:
            continue

        current_id = parts[0]

        if current_id == tid:
            found = True
            continue

        updated.append(line + "\n")

    with open(FILENAME, "w") as f:
        f.writelines(updated)

    if found:
        print("Task deleted.")
    else:
        print("Task ID not found.")


def main():
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
