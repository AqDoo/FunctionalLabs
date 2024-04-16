import tkinter as tk

# Функции для операций с задачами
def create_task(task):
    def inner_create_task(tasks):
        return tasks + [task]
    return inner_create_task

def delete_task(index):
    def inner_delete_task(tasks):
        return tasks[:index] + tasks[index+1:]
    return inner_delete_task

def update_task(index, updated_task):
    def inner_update_task(tasks):
        tasks[index] = updated_task
        return tasks
    return inner_update_task

# Функция композиции
def compose(*functions):
    def composed(*args):
        result = args[0]  # Принимаем только один аргумент - список задач
        for f in functions:
            result = f(result)
        return result
    return composed

# Инициализация графического интерфейса
root = tk.Tk()
root.title("Управление задачами")

# Примеры задач
task1 = {"title": "Покупка молока", "description": "Купить молоко в магазине", "completed": False}
task2 = {"title": "Прочитать книгу", "description": "Прочитать новую книгу по программированию", "completed": True}

# Создание списка задач
tasks = [task1, task2]

# Функция для отображения списка задач в текстовом виджете
def display_tasks():
    text.delete(1.0, tk.END)
    for task in tasks:
        text.insert(tk.END, f"Заголовок: {task['title']}\nОписание: {task['description']}\nСтатус: {'Завершено' if task['completed'] else 'Не завершено'}\n\n")

# Обработчики событий для кнопок
def create_task_handler():
    new_task = {"title": title_entry.get(), "description": description_entry.get(), "completed": False}
    pipeline = compose(create_task(new_task))
    global tasks
    tasks = pipeline(tasks)
    display_tasks()

def delete_task_handler():
    index = int(index_entry.get())
    pipeline = compose(delete_task(index))
    global tasks
    tasks = pipeline(tasks)
    display_tasks()

def update_task_handler():
    index = int(index_entry.get())
    updated_task = {"title": title_entry.get(), "description": description_entry.get(), "completed": False}
    pipeline = compose(update_task(index, updated_task))
    global tasks
    tasks = pipeline(tasks)
    display_tasks()

# Создание виджетов интерфейса
title_label = tk.Label(root, text="Заголовок:")
title_label.grid(row=0, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

description_label = tk.Label(root, text="Описание:")
description_label.grid(row=1, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1)

index_label = tk.Label(root, text="Индекс:")
index_label.grid(row=2, column=0)
index_entry = tk.Entry(root)
index_entry.grid(row=2, column=1)

create_button = tk.Button(root, text="Создать задачу", command=create_task_handler)
create_button.grid(row=3, column=0, columnspan=2, sticky="we")

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task_handler)
delete_button.grid(row=4, column=0, columnspan=2, sticky="we")

update_button = tk.Button(root, text="Обновить задачу", command=update_task_handler)
update_button.grid(row=5, column=0, columnspan=2, sticky="we")

text = tk.Text(root, height=10, width=40)
text.grid(row=6, column=0, columnspan=2)

# Показать начальный список задач
display_tasks()

# Запуск главного цикла обработки событий
root.mainloop()
