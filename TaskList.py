input_task = [];

print("*** To-Do List Application ***");

while True:
    print("\n1. Add task");
    print("2. View task");
    print("3. Remove task");
    print("4. Exit application");
    
    try:
        task_length = len(input_task);
        menu_input = input("Enter your choice (1 - 4): ");
        choice = int(menu_input);
        count = 0;
    
        if choice == 1: #add task
            item = input("\nTask: ");
            input_task.append(item);
        elif choice == 2: #view task
            print("\n*** Task Remaining To-Do ***");
            for task in input_task:
                count += 1;
                print(f"{count}: {task}");
        elif choice == 3: #remove task
            if task_length <= 0:
                print("\nThere are no task to delete.");
            else:
                print("\n*** Task Remaining To-Do ***");
                for task in input_task:
                    count += 1;
                    print(f"{count}: {task}");
                
                while True:
                    try:
                        del_task = input(f"Which task would you like to delete? (1 - {task_length}): ");
                
                        while int(del_task) < 1 or int(del_task) > task_length:
                            print(f"Error: select a task to delete within 1 and {task_length}");
                            del_task = input(f"Which task would you like to delete? (1 - {task_length}): ");
                        break;
                    except ValueError:
                        print("Error (1): Enter a valid number.");
                        
                    
                removed_task = input_task.pop(int(del_task) - 1);
                print(f"Task '{removed_task}' was removed from the list.");
        elif choice == 4: #exit application
            print("Exiting the application.");
            break;
        else:
            print("Error: Invalid option entered. Please enter an option 1 - 4.");
    
    except ValueError:
        print("Error: Please enter a valid option.");
        
    
