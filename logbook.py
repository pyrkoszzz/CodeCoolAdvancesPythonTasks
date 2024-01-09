import os
from datetime import datetime


class Log:
    def __init__(self, user, message):
        self.user = user
        self.message = message
        self.timestamp = datetime.now().timestamp()

    def __str__(self):
        return f'Log:{self.message}|User:{self.user}|Timestamp:{self.timestamp}\n'


class Logbook:
    def __init__(self):
        self.log_file_path = os.path.join("data","logbook.log")

    def display_logs(self) -> None:
        try:
            with open(self.log_file_path, "r") as log_file:
                for log in log_file:
                    print(log, end="")
        except Exception as e:
            print(f'Error during reading log file: {e}')

    def add_log(self, log: Log) -> None:
        try:
            with open(self.log_file_path, "a") as log_file:
                log_file.writelines(str(log))
        except Exception as e:
            print(f'Error during adding log to file: {e}')


if __name__ == '__main__':
    logbook = Logbook()
    log = Log("Patryk", "Created Logbook")
    logbook.add_log(log)
    logbook.add_log(log)
    logbook.add_log(log)
    logbook.display_logs()
