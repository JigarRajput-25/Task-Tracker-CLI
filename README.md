# Task Tracker CLI

A simple command line app to track what you need to do, what you are working on, and what you have finished. Tasks are stored in a local JSON file, and the project uses only the Python standard library.

## Features

- Add, update, and delete tasks
- Mark a task as `todo`, `in-progress`, or `done`
- List all tasks, or filter by status
- Tasks saved in `tasks.json` in the current directory (created automatically)
- Input validation with clear error messages

## Requirements

- Python 3.6 or newer
- No external libraries

## Getting Started

1. Download `task_cli.py` into any folder.
2. Open a terminal in that folder.
3. Run commands with `python task_cli.py <command>`.

## Usage

### Add a task

```
python task_cli.py add "Buy groceries"
```

### Update a task

```
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```
python task_cli.py delete 1
```

### Change a task's status

```
python task_cli.py mark 1 in-progress
python task_cli.py mark 1 done
python task_cli.py mark 1 todo
```

### List tasks

```
python task_cli.py show              # all tasks
python task_cli.py show todo         # tasks not started
python task_cli.py show in-progress  # tasks being worked on
python task_cli.py show done         # completed tasks
```

### Get help

```
python task_cli.py -h
python task_cli.py mark -h
```

## Command Summary

| Command | Arguments | Description |
|---|---|---|
| `add` | `"description"` | Add a new task (status starts as `todo`) |
| `update` | `id "new description"` | Change a task's description |
| `delete` | `id` | Remove a task |
| `mark` | `id status` | Set status to `todo`, `in-progress`, or `done` |
| `show` | `[status]` | List all tasks, or only those with the given status |

## Example Session

```
$ python task_cli.py add "Write report"
Task Added
$ python task_cli.py add "Email the team"
Task Added
$ python task_cli.py mark 1 in-progress
Status updated
$ python task_cli.py show
Task List
1 - Write report - in-progress
2 - Email the team - todo
$ python task_cli.py show todo
todo List
2 - Email the team - todo
```

## Task Format

Each task in `tasks.json` looks like this:

```json
{
  "id": 1,
  "description": "Write report",
  "status": "in-progress",
  "createdAt": "2026-10-14T10:30:00",
  "updatedAt": "2026-10-14T11:05:00"
}
```

| Field | Meaning |
|---|---|
| `id` | Unique number for the task |
| `description` | What needs to be done |
| `status` | `todo`, `in-progress`, or `done` |
| `createdAt` | When the task was created |
| `updatedAt` | When the task was last changed |

## Notes and Behavior

- IDs are never reused. If you delete task 3 and add a new task, it gets the next unused number.
- `tasks.json` is created the first time you add a task.
- Empty descriptions are rejected, and extra spaces around descriptions are trimmed.
- Unknown IDs print `id not found` instead of crashing.
- Invalid statuses (such as `Done` or `finished`) are rejected with a list of valid choices.
- If `tasks.json` is empty or not valid JSON, it is treated as an empty task list, and the next save overwrites it.

## Project Structure

```
.
├── task_cli.py   # the application
└── tasks.json    # task data (created automatically)
```
