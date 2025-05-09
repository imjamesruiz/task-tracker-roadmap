import json
import os
import sys

# print("[DEBUG] running task.py")

def load_tasks():
    if not os.path.exists("task.json"):
        with open("task.json", "w") as file:
            json.dump([], file)
    with open("task.json", "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=2)
        
        
def parse_commands():
    command = sys.argv[1]
    arguments = sys.argv[2:]      
    return command, arguments

def add_task(arguments):
    # commands, arguments = parse_commands()
    description = arguments[0]
    tasks = load_tasks()
    new_id= max((task["id"] for task in tasks), default=0) + 1
    new_task = {"id": new_id, "description": description, "status": "todo"}
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully")
    
def delete_task(arguments):
    # command, arguments = parse_commands()
    tasks = load_tasks()
    task_id = int(arguments[0])
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted")
            
def update_task(arguments):
    # command, arguments = parse_commands()
    tasks = load_tasks()
    task_id = int(arguments[0])
    task_description = str(arguments[1:])
    
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = task_description
            
    save_tasks(tasks)
    print("Task updated successfully")

def mark_in_progress(arguments):
    tasks = load_tasks()
    task_id = int(arguments[0])
    
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in progress"
    
    save_tasks(tasks)
    print("Task marked as in-progress")
    
def mark_done(arguments):
    tasks = load_tasks()
    task_id = int(arguments[0])
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Done"

    save_tasks(tasks)
    print("Task marked done")
    
def list_all(arguments):
    tasks = load_tasks()
    for task in tasks:
        task_dict = json.dumps(task, indent=2)
        print(task_dict)

def list_done(arguments):
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "Done":
            task_dict = json.dumps(task, indent=2)
            print(task_dict)
            
def list_todo(arguments):   
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "todo":
            task_dict = json.dumps(task, indent=2)
            print(task_dict)
            
def list_in_progress(arguments):
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "in progress":
            task_dict = json.dumps(task, indent=2)
            print(task_dict)
         
def methods():
    if len(sys.argv) < 2:
        print("Usage: python script.py [command] [arguments]")
        sys.exit(1)
    
    command, arguments = parse_commands()
    if command == "add":
        add_task(arguments)
    elif command == "delete":
        delete_task(arguments)
    elif command == "update":
        update_task(arguments)
    elif command == "mark-in-progress":
        mark_in_progress(arguments)
    elif command == "mark-done":
        mark_done(arguments)
    elif command == "list":
        list_all(arguments)
    elif command == "list-done":
        list_done(arguments)
    elif command == "list-todo":
        list_todo(arguments)
    elif command == "list-in-progress":
        list_in_progress(arguments)
    else:
        print(f"Unknown command")
        print(f"[DEBUG] Unknown command received: {command!r}")
        sys.exit(1)
        

if __name__ == "__main__":
    methods()

    




