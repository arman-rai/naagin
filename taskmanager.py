from collections import deque
from datetime import datetime
import json

print(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

tasks = deque()

def create_task(task, priorty=False):
    if priorty:
        tasks.appendleft(task)
    else:
        tasks.append(task)
        print(f"Added {task}")
    
def read_task():
    if tasks:
        print("Current tasks")
        for task in tasks:
            print(f"💠 {task}")
    else:
        print("\nNo tasks yet~")


def save_tasks(tasks, filename=None): 
    if not filename:
        filename = "tasks_rn.json"
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(list(tasks), file, indent=4)
    print(f"Exported {filename}")

create_task("Create taskmanager.py", priorty=True)
create_task("Create a checklist")
create_task("Create an weather API ")

choice = input("Do you want to enter a new task?(yes/no)")

if choice == "yes":
    new_task = input("Enter task: ")
    priorty = input("Is it a priorty task? (yes/no)")
    create_task(new_task, priorty)

read_task()

save_tasks(tasks)