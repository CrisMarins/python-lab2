todo_manager = ["spesa","poste", "chiama babbo"]

flag = 0
while flag == 0:
    choice = input(""" which is your choice
    1. insert a new task
    2. remove a task
    3. show all the tasks sorted in alphabetic order
    4. close the program

    """)
    if choice == "1":
        new = input("type new task ")
        if new == "":
            print("nothing added")
        else:
            todo_manager.append(new)
            print("task succesfully added!")
    elif choice == "2":
        rem = input("type task to remove ")
        p = 0
        for tasks in todo_manager:
            if rem == tasks:
                todo_manager.remove(rem)
                print("Task successfully removed from the list ")
                p = 1
        if p == 0:
            print("The task isn't in the list ")
    elif choice == "3":
        todo_manager.sort()
        print(todo_manager)
    elif choice == "4":
        flag = 1
    else:
        print("type a given option value")

