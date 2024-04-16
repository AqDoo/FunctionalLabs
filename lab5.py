import threading
from rx.subject import Subject
from collections import Counter
import tkinter as tk


class VotingSystem:
    def __init__(self, options, root):
        self.options = options
        self.votes_counter = Counter()  # Инициализация счетчика голосов
        self.root = root

        # Создаем поток для подсчета голосов
        self.vote_stream = Subject()

        # Создаем метку для отображения результатов
        self.result_label = tk.Label(root, text="Результаты голосования:")
        self.result_label.pack()

        # Создаем метку для отображения результатов голосования
        self.result_text = tk.StringVar()
        self.result_display = tk.Label(root, textvariable=self.result_text)
        self.result_display.pack()

    def start_voting(self):
        # Подписываемся на поток голосов
        self.subscription = self.vote_stream.subscribe(
            on_next=lambda vote: self.process_vote(vote),
            on_error=lambda e: print(f"Ошибка при обработке голоса: {e}")
        )

    def process_vote(self, vote):
        # Обработка голоса
        if vote in self.options:
            self.votes_counter[vote] += 1  # Используем общий счетчик голосов
            self.update_result_display()

    def update_result_display(self):
        # Обновление отображения результатов голосования
        result_str = "\n".join([f"{option}: {count}" for option, count in self.votes_counter.items()])
        self.result_text.set(result_str)

    def stop_voting(self):
        # Отписываемся от потока голосов
        self.subscription.dispose()


def read_input(voting_system):
    while True:
        vote = input("Введите ваш голос: ")
        voting_system.vote_stream.on_next(vote)


if __name__ == "__main__":
    options = ["Вариант 1", "Вариант 2", "Вариант 3"]

    root = tk.Tk()
    root.title("Система голосования")

    voting_system = VotingSystem(options, root)
    voting_system.start_voting()

    input_thread = threading.Thread(target=read_input, args=(voting_system,))
    input_thread.daemon = True
    input_thread.start()

    root.mainloop()
    voting_system.stop_voting()
