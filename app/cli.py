from app.manager import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Hapus tugas")
        print("4. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            title = input("Judul tugas: ")
            try:
                task = manager.add_task(title)
                print(f"Tugas ditambahkan: {task.title}")
            except ValueError as error:
                print(error)

        elif choice == "2":
            for task in manager.list_tasks():
                print(f"{task.task_id}. {task.title}")

        elif choice == "3":
            try:
                task_id = int(input("ID tugas: "))
                print("Berhasil dihapus" if manager.delete_task(task_id)
                      else "Tugas tidak ditemukan")
            except ValueError:
                print("ID harus berupa angka")

        elif choice == "4":
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
