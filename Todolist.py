def main():
    tasks = []
    
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            if not tasks:
                print("\nYour list is empty.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == '2':
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            print("Task added!")

        elif choice == '3':
            if tasks:
                task_num = int(input("Enter the task number to remove: "))
                if 0 < task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            else:
                print("Nothing to remove.")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()