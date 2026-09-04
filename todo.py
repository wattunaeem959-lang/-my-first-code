tasks = []
while True:
    print("\n1. Add Task  2. Show Tasks  3. Exit")
    choice = input("Chun: ")
    if choice == "1":
        task = input("Task likh: ")
        tasks.append(task)
        print("Added!")
    elif choice == "2":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        break