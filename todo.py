from os import path


class TaskNotFoundException(Exception):
    def __init__(self, idx: int, message: str = "Task with given index doesn't exists"):
        self.idx = idx
        self.message = message
        super().__init__(self.message)


class Task:
    def __init__(self, idx: int, title: str, user: str, is_done: bool = False):
        self.idx = int(idx)
        self.title = title
        self.user = user
        self.is_done = is_done

    @classmethod
    def from_file(cls, text_string: str):
        idx, title, user, is_done = text_string.strip().split(';')
        return cls(idx, title, user, (is_done == 'True'))

    def mark_done(self) -> None:
        self.is_done = True

    def nice_text(self) -> str:
        return f'Id: {self.idx}\nTitle: {self.title}\nUser: {self.user}\nDone: {'✅' if self.is_done else '❌'}\n'

    def __str__(self):
        return f'{self.idx};{self.title};{self.user};{self.is_done}\n'


class Todo:
    def __init__(self):
        self.todo_file_path = path.join('todo.txt')

    def get_next_idx(self):
        try:
            with open(self.todo_file_path, "r") as todo_file:
                return len(todo_file.readlines()) + 1
        except Exception as e:
            print(f'Error occurred: {e}')

    def display_tasks(self) -> None:
        try:
            with open(self.todo_file_path, "r") as todo_file:
                for task_str in todo_file:
                    task = Task.from_file(task_str)
                    print(task.nice_text())
        except Exception as e:
            print(f'Error occurred: {e}')

    def add_task(self, task: Task) -> None:
        try:
            with open(self.todo_file_path, "a") as todo_file:
                task.idx = self.get_next_idx()
                todo_file.write(str(task))
        except Exception as e:
            print(f'Error occurred: {e}')

    def get_task_by_id(self, idx: int) -> Task | None:
        try:
            with open(self.todo_file_path, "r") as todo_file:
                for task_str in todo_file:
                    task = Task.from_file(task_str)
                    if task.idx == idx:
                        return task
                raise TaskNotFoundException(idx)
        except Exception as e:
            print(f'Error occurred: {e}')

    def save_updated_task(self, task_to_update: Task) -> None:
        try:
            new_content = ""
            with open(self.todo_file_path, "r") as todo_file:
                for task_str in todo_file:
                    task = Task.from_file(task_str)
                    if task.idx == task_to_update.idx:
                        task_str = task_str.replace(str(task), str(task_to_update))
                    new_content += task_str
            with open(self.todo_file_path, "w") as todo_file:
                todo_file.write(new_content)
        except Exception as e:
            print(f'Error occurred: {e}')


if __name__ == '__main__':
    todo_app = Todo()
    task = Task(0, "First Task", "Patryk")
    todo_app.add_task(task)
    todo_app.display_tasks()

    task_to_mark_done = todo_app.get_task_by_id(1)
    task_to_mark_done.mark_done()
    todo_app.save_updated_task(task_to_mark_done)

    print(todo_app.get_task_by_id(8))

    todo_app.display_tasks()
