class Task:
    def __init__(self, task_name,due_date):
        self.task_name = task_name
        self.due_date = due_date

class TaskMenager:
    def __init__(self):
        self.tasks = []

    def add_task(self,task_name,due_date):
        task = Task(task_name, due_date)
        self.tasks.append(task)

    def remove_task(self,task_name):
        task_exists = False

        for task in self.tasks:
            if task.task_name == task_name:
                self.tasks.remove(task)
                task_exists = True
                break
        if not task_exists:
            print("Nie można odnależć zadania o podanej nazwie: ", task_name)

    def display_tasks(self):
        if not self.tasks:
            print("Bral zadań.")
        else:
            print("lista zadań: ")
            for task in self.tasks:
                print(f"{task.task_name} | Termin: {task.due_date}")

    def change_due_date(self, task_name, new_due_date):
        task_exists = False
        for task in self.tasks:
            if task.task_name == task_name:
                task.due_date = new_due_date     
                task_exists = True
                print("Termin zadania został zmieniony")
                break
        if not task_exists:
            print("Nie można znalezc zadania") 

task_menager = TaskMenager()
task_menager.add_task("Umyj naczynia","01.12.2023")
task_menager.add_task("wynieś śmieci","07.12.2023")
task_menager.add_task("Odpoczynek","03.12.2023")
print("Dodano elementy-----------------------------------")
task_menager.display_tasks()

print("Zmiana Daty elementu---------------------------------")
task_menager.change_due_date("wynieś śmieci","02.12.2023")
task_menager.display_tasks()

print("wyjebanie jednego----------------------------------")
task_menager.remove_task("Odpoczynek")
task_menager.display_tasks()