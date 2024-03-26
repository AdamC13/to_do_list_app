
tasks = []  #our list of tasks starting empty
def cli():
    #Main menu functionality
    user_input = input("""
    Welcome to the To-Do List App! 📝✨

    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
                       
    """)
    try:
        #each input is correlated with a function
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
            print("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")   #if they enter a number other than one of the options
            cli()
    except (ValueError, OverflowError): #Handles errors if they enter letters
        print("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
        cli()



def add_task(): #function for adding a task
    task = input("\nWhat task would you like to add? (back) ")
    if task.lower() == "back": #heads back to main menu
        cli()
    elif task.isspace() == True:    #if they only enter spaces we tell them invalid
        print("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
        add_task()
    elif task == '':    #if they don't enter anything we tell them invalid
        print("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
        add_task()
    else:   #otherwise whatever they enter we add as a task
        tasks.append([task, False])
        add_task()
        
    

def view_task():    #function for viewing the tasks
    print("\nHere are your tasks so far\n")
    for task in tasks:  #lopps through and prints each task with the completion status
        if task[1] == True: #checking if the task is done
            print(f"{task[0]} --> Complete! ✅ 😎")
        elif task[1] == False:
            print(f"{task[0]} --> Incomplete ❌ 🙄")
    input("\nPress enter to go back")   #we wait for them to be done viewing the tasks
    cli()

def mark_complete():    #function for marking tasks complete
    print("\nWhich task did you complete? (back)\n")
    for i in range(len(tasks)):     #printing each task with status again
        if tasks[i][1] == True:
            print(f"{i+1}: {tasks[i][0]} --> Already complete! ✅ 😎")
        elif tasks[i][1] == False:
            print(f"{i+1}: {tasks[i][0]} --> Incomplete ❌ 🙄")
    user_input = input()
    if user_input == "back":    #goes back to main menu if they enter back
        cli()
    else:
        try:
            tasks[int(user_input)-1][1] = True    #Reassigns the completion boolean to True
        except(ValueError, IndexError, OverflowError):      #handles errors
            print("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
        finally:
            mark_complete()


def delete_task():
    print("\nWhich task did you want to delete? (back)\n")      #delete task function
    for i in range(len(tasks)):     #tells them their tasks they could delete
        print(f"{i+1}: {tasks[i][0]}")
    user_input = input()
    if user_input == "back":        #allows them to back to main menu
        cli()
    else:
        try:
            tasks.pop(int(user_input)-1)        #Removes the task they selected
        except(ValueError, IndexError, OverflowError):      #Handles errors such as a number larger than our list of tasks
            print("\n\n\nInvalid input ༼ つ ◕_◕ ༽つ")
        finally:
            delete_task()


cli()