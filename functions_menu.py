import json

with open("task.json", "r") as file:
    try:
        json_task = json.load(file)
    except json.JSONDecodeError:
        json_task = {}

def save_tasks(tasks):
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)

def AddTask():
    task = input("What task do you want to do?: ")

    task_id = 1
    while f"Task {task_id}" in json_task:
        task_id += 1

    json_task[f"Task {task_id}"] = task
    save_tasks(json_task)

def DeleteTask():
    task_id = input("What task would you like to delete (e.g., Task 1)?: ")

    if task_id in json_task:
        del json_task[task_id]
        save_tasks(json_task)
    else:
        print("Wrong Task")

def ViewJson():
    print(json.dumps(json_task, indent=4))

# Test Jenkins - it add a task to a test file, if it's not there the programs does not work
def test():
    test = "Test"

    with open("test_task.json", 'w') as test_file:
        json.dump({"Task 1": test}, test_file)
    

    with open("test_task.json", 'r') as test_file:
        tasks = json.load(test_file)
        if "Task 1" in tasks and tasks["Task 1"] == test:
            print("Test passed!")
        else:
            print("Test failed!")
            exit(1)

if __name__ == "__main__":
    test()