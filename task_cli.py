import argparse #CLI
import json #json file
from datetime import datetime

def now():
    return datetime.now().isoformat(timespec="seconds")

data_file = "tasks.json"
statuses = ["todo","in-progress","done"]

#Functions for the file handling
def load():
    try:
        with open(data_file,encoding="utf-8") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        return []
def save(tasks):
    with open(data_file, "w",encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)
def find(tasks,n):
    for t in tasks:
        if t["id"] == n:
            return t
    print("id not found")
    return None

#Program functions
def add(task_name):
    if not task_name.strip():
        print("Empty Task Not Added")
        return
    tasks = load()
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task = {
        "id" : new_id,
        "description" : task_name.strip(),
        "status" : "todo",
        "createdAt" : now(),
        "updatedAt" : now(),
    }
    tasks.append(task)
    save(tasks)
    print("Task Added")

def update(i,new_task):
    if not new_task.strip():
        print("Empty Task Not Updated")
        return
    tasks = load()
    task = find(tasks,i)
    if task is None:
        return
    task["description"] = new_task.strip()
    task["updatedAt"] = now()
    save(tasks)
    print("Task Updated")


def delete(n):
    tasks = load()
    task =find(tasks,n)
    if task is None:
        return
    tasks.remove(task)
    save(tasks)
    print("Task Deleted")

def show(state):
    tasks = load()
    if state is None:
        print("Task List")
        for task in tasks:
            print(task["id"],"-",task["description"],"-",task["status"])
        return
    print(f"{state} List")
    for task in tasks:
        if task["status"] == state:
            print(task["id"],"-",task["description"],"-",task["status"])

def mark(t,state):
    tasks = load()
    task = find(tasks,t)
    if task is None:
        return
    task["status"] = state
    task["updatedAt"] = now()
    save(tasks)
    print("Status updated")

#main
def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='command',required=True)

    add_cmd = sub.add_parser('add', help='add a new task')
    add_cmd.add_argument('task')

    delete_cmd = sub.add_parser('delete', help='delete a task')
    delete_cmd.add_argument('n',type=int)

    update_cmd = sub.add_parser('update', help='update a task')
    update_cmd.add_argument('n',type=int)
    update_cmd.add_argument('new_task',type=str)

    mark_cmd = sub.add_parser('mark', help='mark a task')
    mark_cmd.add_argument('n',type=int)
    mark_cmd.add_argument('state',type=str,choices=statuses)

    show_cmd = sub.add_parser('show', help='show the tasks')
    show_cmd.add_argument('state',nargs='?',choices=statuses)



    args = parser.parse_args()

    if args.command == 'add':
        add(args.task)
    elif args.command == 'delete':
        delete(args.n)
    elif args.command == 'update':
        update(args.n,args.new_task)
    elif args.command == 'show':
        show(args.state)
    elif args.command == 'mark':
        mark(args.n,args.state)


if __name__ == '__main__':
    main()
