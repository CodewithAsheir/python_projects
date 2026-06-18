# tasks = []

# while True:
#     print("\n1 Add Task")
#     print("2 View Task")
#     print("3 Delete Task")
#     print("4 Exit")

#     choice = input("choose:")
#     if choice =="1":
#         task = input("Enter task:")
#         tasks.append(task)
#         print("Task added")

#     elif choice == "2":
#         for i, task in enumerate(tasks):
#             print(i+1,task)

#     elif choice == "3":
#         num = int(input("Task number delete:"))
#         tasks.pop(num-1)
#         print("Deleted")

#     elif choice == "4":
#         break
#     else:
#         print("Invalid option")

tasks = []

while True:
    print("\n1 Add Task")
    print("2 View Task")
    print("3 Delete Task")
    print("4 Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(i + 1, task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks):
                print(i + 1, task)

            try:
                num = int(input("Enter task number to delete: "))

                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    print("Task deleted successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
    