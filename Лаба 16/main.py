from datetime import date, datetime, timedelta


class Task:
    def __init__(self, title: str, description: str, due_date: date, priority: str = "Medium", notes: str = "",
                 duration: int = 0, recurrence: str = "", status: str = "Pending", dependencies: list = []):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence
        self.status = status
        self.dependencies = dependencies

    def is_due_today(self) -> bool:
        return self.due_date == date.today()


class Schedule:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task_title: str):
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)
                break

    def get_task(self, task_title: str) -> Task:
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    def list_overdue_tasks(self) -> list:
        return [task for task in self.tasks if task.due_date < date.today()]

    def list_tasks_due_today(self) -> list:
        return [task for task in self.tasks if task.is_due_today()]

    def sort_tasks_by_due_date(self) -> list:
        return sorted(self.tasks, key=lambda task: task.due_date)

    def update_task(self, task_title: str, **kwargs):
        task = self.get_task(task_title)
        if task:
            for key, value in kwargs.items():
                setattr(task, key, value)

    def weekly_schedule(self, start_date: date) -> list:
        end_date = start_date + timedelta(days=7)
        return [task for task in self.tasks if start_date <= task.due_date < end_date]

    def monthly_schedule(self, year: int, month: int) -> list:
        first_day = date(year, month, 1)
        last_day = date(year, month + 1, 1) - timedelta(days=1)
        return [task for task in self.tasks if first_day <= task.due_date <= last_day]

    def list_tasks_by_priority(self, priority: str) -> list:
        return [task for task in self.tasks if task.priority == priority]

    def save_to_file(self, filename: str):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(
                    f"{task.title},{task.description},{task.due_date},{task.priority},{task.notes},{task.duration},{task.recurrence},{task.status},{';'.join([dep.title for dep in task.dependencies])}\n")

    def load_from_file(self, filename: str):
        self.tasks = []
        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                title = task_data[0]
                description = task_data[1]
                due_date = datetime.strptime(task_data[2], "%Y-%m-%d").date()
                priority = task_data[3]
                notes = task_data[4]
                duration = int(task_data[5])
                recurrence = task_data[6]
                status = task_data[7]
                dependencies = [self.get_task(dep_title) for dep_title in task_data[8].split(";") if dep_title]
                task = Task(title, description, due_date, priority, notes, duration, recurrence, status, dependencies)
                self.add_task(task)

    def list_tasks_with_notes(self) -> list:
        return [task for task in self.tasks if task.notes]

    def mark_as_completed(self, task_title: str):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"
    def list_completed_tasks(self) -> list:
        return [task for task in self.tasks if task.status == "Completed"]

    def find_task_by_keyword(self, keyword: str) -> list:
        return [task for task in self.tasks if
                keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]


    def check_deadlines(self) -> list:
        return [task for task in self.tasks if task.due_date == date.today() + timedelta(days=1)]

    def list_all_tasks(self) -> list:
        return self.tasks

    def list_tasks_by_duration(self, min_duration: int, max_duration: int) -> list:
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]

    def task_history(self) -> list:
        history = []
        for task in self.tasks:
            if task.status == "Completed":
                history.append(("completed", task))
            elif task.status == "Pending":
                history.append(("added", task))
            else:
                history.append(("updated", task))
        return history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]

    def list_recurring_tasks(self) -> list:
        return [task for task in self.tasks if task.recurrence]

    def set_reminder(self, task_title: str, reminder_date: date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date

    def completion_percentage(self) -> float:
        if not self.tasks:
            return 0.0
        completed_tasks = len(self.list_completed_tasks())
        total_tasks = len(self.tasks)
        return (completed_tasks / total_tasks) * 100

# Создание задачи
task1 = Task(
    title="Task 1",
    description="Description for task 1",
    due_date=date(2024, 6, 10),
    priority="High",
    notes="Important task",
    duration=120,
    recurrence="",
    status="Pending",
    dependencies=[]
)

task2 = Task(
    title="Task 2",
    description="Description for task 2",
    due_date=date(2024, 6, 11),
    priority="Medium",
    notes="",
    duration=60,
    recurrence="",
    status="Pending",
    dependencies=[]
)

# Создание расписания и добавление задач
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)

# Печать всех задач
print("All tasks:")
for task in schedule.list_all_tasks():
    print(f"Title: {task.title}, Due Date: {task.due_date}, Status: {task.status}")

# Печать задач, срок выполнения которых сегодня
print("\nTasks due today:")
for task in schedule.list_tasks_due_today():
    print(f"Title: {task.title}, Due Date: {task.due_date}, Status: {task.status}")

# Печать просроченных задач
print("\nOverdue tasks:")
for task in schedule.list_overdue_tasks():
    print(f"Title: {task.title}, Due Date: {task.due_date}, Status: {task.status}")

# Обновление задачи
schedule.update_task("Task 1", status="Completed", notes="Task 1 is completed")
updated_task = schedule.get_task("Task 1")
print(f"\nUpdated Task 1: Title: {updated_task.title}, Status: {updated_task.status}, Notes: {updated_task.notes}")

# Печать завершённых задач
print("\nCompleted tasks:")
for task in schedule.list_completed_tasks():
    print(f"Title: {task.title}, Due Date: {task.due_date}, Status: {task.status}")

# Печать задач по приоритету
print("\nTasks with high priority:")
for task in schedule.list_tasks_by_priority("High"):
    print(f"Title: {task.title}, Due Date: {task.due_date}, Priority: {task.priority}")

# Печать недельного расписания
print("\nWeekly schedule from today:")
for task in schedule.weekly_schedule(date.today()):
    print(f"Title: {task.title}, Due Date: {task.due_date}")

# Печать задач с заметками
print("\nTasks with notes:")
for task in schedule.list_tasks_with_notes():
    print(f"Title: {task.title}, Notes: {task.notes}")

# Печать истории задач
print("\nTask history:")
for action, task in schedule.task_history():
    print(f"Action: {action}, Title: {task.title}, Status: {task.status}")
