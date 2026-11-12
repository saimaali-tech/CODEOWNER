tasks = []

def add_task(title):
    if not title:
        raise ValueError("Task title cannot be empty")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    return task


def get_tasks():
    return tasks


def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task

    raise ValueError("Task not found")