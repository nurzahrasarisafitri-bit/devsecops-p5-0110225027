class Task:
    def __init__(self, task_id, title):
        if not title or not title.strip():
            raise ValueError("Judul tugas tidak boleh kosong")

        self.task_id = task_id
        self.title = title.strip()
        self.completed = False

    def mark_completed(self):
        self.completed = True
