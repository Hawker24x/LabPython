Лабораторна робота №16: Advanced TODO List
___
Мета роботи:
Розробити Python-програму для управління завданнями через створення двох основних класів: Task та Schedule.
___
Опис завдання:
```Python
Task 1: Create Task Class
Create a Python class named Task with the following attributes:
Example of class usage:
Task 2: Add Method to Task Class
Add a method named is_due_today() to the Task class that checks if the task
is due today and returns a boolean.
Example of class usage:
Task 3: Create Schedule Class
Create a class named Schedule that manages multiple tasks. It should have the
following methods:
title
description
due_date (use datetime.date )
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
from datetime import date
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())
task.is_due_today() # Expected output: True if today is the due
date
add_task(task: Task)
Example of class usage:
Task 4: List Overdue Tasks
Add a method named list_overdue_tasks() to the Schedule class that returns
a list of tasks that are overdue.
Example of class usage:
Task 5: List Tasks Due Today
Add a method named list_tasks_due_today() to the Schedule class that
returns a list of tasks that are due today.
Example of class usage:
remove_task(task_title: str)
get_task(task_title: str) -> Task
schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.get_task("Buy groceries") # Expected output: Task
object
from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() - timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=2))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_overdue_tasks() # Expected output: [task1]
from datetime import date
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today())
Task 6: Sort Tasks by Due Date
Add a method named sort_tasks_by_due_date() to the Schedule class that
returns a list of tasks sorted by their due dates.
Example of class usage:
Task 7: Update Task
Add a method named update_task(task_title: str, **kwargs) to the
Schedule class that updates the attributes of a task.
Example of class usage:
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today())
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_due_today() # Expected output: [task1,
task2]
from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date.today() + timedelta(days=2))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date.today() + timedelta(days=1))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.sort_tasks_by_due_date() # Expected output: [task2,
task1]
schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.update_task("Buy groceries", description="Milk, Bread,
Eggs, Cheese", due_date=date(2024, 5, 26))
schedule.get_task("Buy groceries") # Expected output: Task
object with updated attributes
Task 8: Task Status
Add a status attribute to the Task class which can be 'Pending', 'In Progress', or
'Completed'. Modify Task and Schedule to handle task status updates.
Example of class usage:
Task 9: Weekly Schedule
Create a method weekly_schedule(start_date: date) in the Schedule class
that returns a list of tasks for the week starting from the provided date.
Example of class usage:
Task 10: Monthly Schedule
Create a method monthly_schedule(year: int, month: int) in the Schedule
class that returns a list of tasks for the specified month.
Example of class usage:
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Pending")
schedule = Schedule()
schedule.add_task(task)
task.status = "In Progress"
schedule.update_task("Buy groceries", status="Completed")
schedule.get_task("Buy groceries").status # Expected output:
"Completed"
from datetime import date, timedelta
schedule = Schedule()
task1 = Task(title="Task 1", description="First task",
due_date=date(2024, 5, 21))
task2 = Task(title="Task 2", description="Second task",
due_date=date(2024, 5, 23))
schedule.add_task(task1)
schedule.add_task(task2)
start_date = date(2024, 5, 20)
schedule.weekly_schedule(start_date) # Expected output: [task1,
task2]
Task 11: Task Priority
Add a priority attribute to the Task class which can be 'Low', 'Medium', or 'High'.
Modify Task and Schedule to handle task priority.
Example of class usage:
Task 12: List Tasks by Priority
Add a method list_tasks_by_priority(priority: str) to the Schedule
class that returns a list of tasks with the specified priority.
Example of class usage:
from datetime import date
schedule = Schedule()
task1 = Task(title="Task 1", description="First task",
due_date=date(2024, 5, 21))
task2 = Task(title="Task 2", description="Second task",
due_date=date(2024, 6, 1))
schedule.add_task(task1)
schedule.add_task(task2)
schedule.monthly_schedule(2024, 5) # Expected output: [task1]
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), priority="High")
schedule = Schedule()
schedule.add_task(task)
task.priority # Expected output: "High"
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), priority="High")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), priority="Low")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_by_priority("High") # Expected output:
[task1]
Task 13: Save Schedule to File
Add a method save_to_file(filename: str) to the Schedule class that saves
the schedule to a file.
Example of class usage:
Task 14: Load Schedule from File
Add a method load_from_file(filename: str) to the Schedule class that
loads the schedule from a file.
Example of class usage:
Task 15: Task Notes
Add a notes attribute to the Task class that can store additional information about
the task. Modify Task and Schedule to handle task notes.
Example of class usage:
Task 16: List Tasks with Notes
Add a method list_tasks_with_notes() to the Schedule class that returns a
list of tasks that have notes.
schedule = Schedule()
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task)
schedule.save_to_file("schedule.txt")
schedule = Schedule()
schedule.load_from_file("schedule.txt")
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), notes="Use the discount
coupon")
schedule = Schedule()
schedule.add_task(task)
task.notes # Expected output: "Use the discount coupon"
Example of class usage:
Task 17: Mark Task as Completed
Add a method mark_as_completed(task_title: str) to the Schedule class
that marks the specified task as completed.
Example of class usage:
Task 18: List Completed Tasks
Add a method list_completed_tasks() to the Schedule class that returns a
list of completed tasks.
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), notes="Use the discount
coupon")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_tasks_with_notes() # Expected output: [task1]
task = Task(title="Buy groceries", description="Milk, Bread, Eggs
", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.mark_as_completed("Buy groceries")
task.status # Expected output: "Completed"
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
Task 19: Find Task by Keyword
Add a method find_task_by_keyword(keyword: str) to the Schedule class
that returns a list of tasks that contain the specified keyword in their title or
description.
Example of class usage:
Task 20: Task Deadline Notification
Add a method check_deadlines() to the Schedule class that returns a list of
tasks that are due in the next 24 hours.
Example of class usage:
Task 21: List All Tasks
schedule.add_task(task2)
schedule.list_completed_tasks() # Expected output: [task1]
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.find_task_by_keyword("assignment") # Expected output:
[task2]
from datetime import datetime, timedelta
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=datetime.now().date() + timedelta(days=1))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=datetime.now().date() + timedelta(days=2))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.check_deadlines() # Expected output: [task1]
Add a method list_all_tasks() to the Schedule class that returns a list of all
tasks.
Example of class usage:
Task 22: Task Duration
Add a duration attribute to the Task class which specifies the expected time to
complete the task in hours. Modify Task and Schedule to handle task duration.
Example of class usage:
Task 23: List Tasks by Duration
Add a method list_tasks_by_duration(min_duration: int, max_duration:
int) to the Schedule class that returns a list of tasks whose duration falls within
the specified range.
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_all_tasks() # Expected output: [task1, task2]
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
schedule = Schedule()
schedule.add_task(task)
task.duration # Expected output: 2
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), duration=2)
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), duration=4)
schedule = Schedule()
schedule.add_task(task1)
Task 24: Task History
Add a method task_history() to the Schedule class that returns a history of
tasks added, removed, and updated in the schedule.
Example of class usage:
Task 25: Clear Completed Tasks
Add a method clear_completed_tasks() to the Schedule class that removes
all completed tasks from the schedule.
Example of class usage:
Task 26: Task Recurrence
Add a recurrence attribute to the Task class that specifies if the task is recurring
(daily, weekly, monthly). Modify Task and Schedule to handle task recurrence.
Example of class usage:
schedule.add_task(task2)
schedule.list_tasks_by_duration(1, 3) # Expected output: [task1]
schedule = Schedule()
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule.add_task(task1)
schedule.remove_task("Buy groceries")
schedule.task_history() # Expected output: [("added", task1),
("removed", task1)]
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.clear_completed_tasks()
schedule.list_all_tasks() # Expected output: [task2]
Task 27: List Recurring Tasks
Add a method list_recurring_tasks() to the Schedule class that returns a
list of recurring tasks.
Example of class usage:
Task 28: Task Reminders
Add a method set_reminder(task_title: str, reminder_date: date) to the
Schedule class that sets a reminder for a specific task.
Example of class usage:
Task 29: Task Completion Percentage
Add a method completion_percentage() to the Schedule class that returns the
percentage of completed tasks.
task = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
schedule = Schedule()
schedule.add_task(task)
task.recurrence # Expected output: "weekly"
task1 = Task(title="Water plants", description="Water the plants
in the garden", due_date=date(2024, 5, 25), recurrence="weekly")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26))
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.list_recurring_tasks() # Expected output: [task1]
task = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
schedule = Schedule()
schedule.add_task(task)
schedule.set_reminder("Buy groceries", date(2024, 5, 24))
Example of class usage:
Task 30: Task Dependency
Add a dependencies attribute to the Task class that specifies other tasks that
need to be completed before the task can start. Modify Task and Schedule to
handle task dependencies.
Example of class usage:
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25), status="Completed")
task2 = Task(title="Submit assignment", description="Math
assignment", due_date=date(2024, 5, 26), status="Pending")
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
schedule.completion_percentage() # Expected output: 50.0
task1 = Task(title="Buy groceries", description="Milk, Bread,
Eggs", due_date=date(2024, 5, 25))
task2 = Task(title="Prepare breakfast", description="Use
groceries to prepare breakfast", due_date=date(2024, 5, 26),
dependencies=[task1])
schedule = Schedule()
schedule.add_task(task1)
schedule.add_task(task2)
task2.dependencies # Expected output: [task1]
```
___
Виконання роботи:
```Python
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

```
___
Результати:
```Python
All tasks:
Title: Task 1, Due Date: 2024-06-10, Status: Pending
Title: Task 2, Due Date: 2024-06-11, Status: Pending

Tasks due today:

Overdue tasks:
Title: Task 1, Due Date: 2024-06-10, Status: Pending
Title: Task 2, Due Date: 2024-06-11, Status: Pending

Updated Task 1: Title: Task 1, Status: Completed, Notes: Task 1 is completed

Completed tasks:
Title: Task 1, Due Date: 2024-06-10, Status: Completed

Tasks with high priority:
Title: Task 1, Due Date: 2024-06-10, Priority: High

Weekly schedule from today:

Tasks with notes:
Title: Task 1, Notes: Task 1 is completed

Task history:
Action: completed, Title: Task 1, Status: Completed
Action: added, Title: Task 2, Status: Pending
```
___
Висновки: Цей проєкт навчає організації та управлінню складними структурами даних, роботі з датами, об'єктно-орієнтованому програмуванню та створенню ефективних інструментів для повсякденного використання.
___