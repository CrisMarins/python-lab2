#apro file e copio su lista

todo_manager=[]
txt=open("task_list.txt")
todo_manager=txt.read().splitlines()
txt.close()
flag = 0
while flag == 0:
    choice = input(""" which is your choice
    1. insert a new task
    2. remove a task
    3. show all the tasks sorted in alphabetic order
    4. remove all the tasks that contain a substring
    5. close the program

    """)
    if choice == "1":
        new=input("type new task ")
        if new=="":
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
        for tasks in todo_manager:
            print(tasks)
    elif choice == "4":
        remove_list = []
        substring = input("Type the substring you want to use to remove all tasks that contain it")

        for single_task in todo_manager:
            # if the substring is contained in the task we save it in the remove_list
            if (substring in single_task):
                remove_list.append(single_task)
        if (len(remove_list) > 0):
            for task_to_remove in remove_list:
                if (task_to_remove in todo_manager):
                    todo_manager.remove(task_to_remove)
                    print("The element " + task_to_remove + " was successfully removed")
        else:
            print("We did not find any tasks to delete!")

    elif choice == "5":
        flag = 1
    else:
        print("type a given option value")

#Copio sul file e chiudo
end=open("task_list.txt", "w")
for task in todo_manager:
    end.write(task+"\n")
end.close()