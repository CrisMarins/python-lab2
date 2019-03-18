todo_manager = ["spesa","poste", "chiama babbo"]

flag = 0
while flag == 0:
    choice = int(input(""" wich is your choice
    1. insert a new task
    2. remove a task
    3. show all the tsks sorted in alphabetic order
    4. close the program

    """))
    if choice == 1:
        todo_manager.append(input("type new task "))
    elif choice == 2:
        todo_manager.remove(input("type task to remove "))
    elif choice == 3:
        todo_manager.sort()
        print(todo_manager)
    elif choice == 4:
        flag = 1
    else:
        print("type a given option value")

