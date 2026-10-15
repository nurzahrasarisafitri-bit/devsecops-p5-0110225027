import unittest

from app.manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Belajar DevSecOps")
        self.assertEqual(task.title, "Belajar DevSecOps")
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_delete_task(self):
        task = self.manager.add_task("Tes aplikasi")
        self.assertTrue(self.manager.delete_task(task.task_id))
        self.assertEqual(len(self.manager.list_tasks()), 0)

    def test_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")


if __name__ == "__main__":
    unittest.main()
