# welcome
print("Welcome to the Task Manager!")

# initial states
tasks = []

# function add task
def add_task():

    # get the new task
    task = input("Masukan tugas baru anda: ")

    if (not task):
        raise ValueError("Task cannot be empty.")

    # append
    tasks.append(task)

    print(f"{task} successfully added")
    print("---------------------")

    show_program()

# function remove task
def remove_task():

    # get the index of task
    index = int(input("Masukan nomor tugas yang ingin dihapus: "))

    if (len(tasks) == 0):
        raise ValueError("Task is still empty, add new task first")

    # removing
    removed = tasks.pop(index)

    print(f"removed: {removed}")
    print("---------------------")

    show_program()

# function show all tasks
def show_tasks():

    print("Daftar tugas anda:")

    for task in tasks:
        print(f"{tasks.index(task) + 1}. {task}")

    print("---------------------")

    show_program()

# function show program
def show_program():
    print("Pilih tindakan:")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Hapus tugas")
    print("0. Keluar")

    # get the program
    program = int(input("Pilihan anda: "))

    print("---------------------")

    if (program == 1): add_task()
    if (program == 2): show_tasks()
    if (program == 3): remove_task()
    if (program == 0): 
        print("Thank you for using the Task Manager!")
        exit()
    else:
        raise ValueError("Invalid input, please try again")

# Show the program
show_program()