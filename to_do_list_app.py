def cli():
    user_input = input("""
    Welcome to the To-Do List App!

    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    """)
    try:
        if int(user_input) == 1:
            add_task()
        elif int(user_input) == 2:
            view_task()
        elif int(user_input) == 3:
            mark_complete()
        elif int(user_input) == 4:
            delete_task()
        elif int(user_input) == 5:
            quit()
        else:
            print("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
            cli()
    except (ValueError, OverflowError):
        print("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
        cli()



def add_task():
    task = input("\nWhat task would you like to add? (back) ")
    if task.lower() == "back":
        cli()
    else:
        tasks.append([task, False])
        add_task()
        
    

def view_task():
    print("\nHere are your tasks so far")
    for task in tasks:
        if task[1] == True:
            print(f"{task[0]} --> Complete! 😎")
        elif task[1] == False:
            print(f"{task[0]} --> Incomplete 🙄")
    input("\nPress enter to go back")
    cli()

def mark_complete():
    print("\nWhich task did you complete?")
    for i in range(len(tasks)):
        if tasks[i][1] == True:
            print(f"{i+1}: {tasks[i][0]} --> Already complete! 😎")
        elif tasks[i][1] == False:
            print(f"{i+1}: {tasks[i][0]} --> Incomplete 🙄")
    user_input = input()
    if user_input == "quit":
        cli()
    else:
        try:
            tasks[int(user_input)-1][1] = True
            mark_complete()
        except(ValueError, IndexError, OverflowError):
            print("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
            mark_complete()


def delete_task():
    print("\nWhich task did you want to delete?")
    for i in range(len(tasks)):
        print(f"{i+1}: {tasks[i][0]}")
    user_input = input()
    if user_input == "quit":
        cli()
    else:
        tasks.pop(int(user_input)-1)
        delete_task()



tasks = [["This is a task", False], ["Another task", True]]
cli()