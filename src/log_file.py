from icecream import ic, install # type: ignore
#---------------------------------------------------------------------------------------------------
from os import path, mkdir


def save_log(log_data: str) -> None:
    log_file_path: str = "src/logs/log_file.txt"
    create_log_file()
    if not path.exists("src/logs/"):
        mkdir("src/logs")
    with open(log_file_path, "a") as log_file:
        log_data += "\n"
        log_file.write(log_data)

def clear_log() -> None:
    log_file_path: str = "src/logs/log_file.txt"
    create_log_file()
    with open(log_file_path, "w") as log_file:
        log_file.write("")

def create_log_file() -> None:
    log_file_path: str = "src/logs/"
    if not path.exists(log_file_path):
        mkdir(log_file_path)

def start_logging() -> None:
    install()
    ic.configureOutput(
        prefix="pyOrgan: ",
        includeContext=True,
        contextAbsPath=False,
        outputFunction=save_log
    )
    clear_log()


if __name__ == "__main__":
    save_log("This is a test log entry.")
