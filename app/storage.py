import json
from pathlib import Path


def save_tasks(tasks, filename="tasks.json"):
    data = [
        {
            "task_id": task.task_id,
            "title": task.title,
            "completed": task.completed,
        }
        for task in tasks
    ]

    Path(filename).write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )
