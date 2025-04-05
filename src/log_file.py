from icecream import ic, install # type: ignore
#-----------------------------------------------------------------------------------------------------------------------
from os import path, mkdir


#=======================================================================================================================
# File Actions
#=======================================================================================================================
def log_to_file(log_data: str) -> None:
    log_file_path: str = "src/logs/log_file.txt"
    create_log_file()
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

def no_log(log_data: str) -> None:
    pass

#=======================================================================================================================
# Logging Configuration
#=======================================================================================================================
def start_logging_to_file() -> None:
    install()
    ic.configureOutput(
        prefix="pyOrgan: ",
        includeContext=True,
        contextAbsPath=False,
        outputFunction=log_to_file
    )
    clear_log()

def start_logging_to_console() -> None:
    install()
    ic.configureOutput(
        prefix="pyOrgan: ",
        includeContext=True,
        contextAbsPath=False,
        outputFunction=print
    )

def no_logging() -> None:
    install()
    ic.configureOutput(
        prefix="pyOrgan: ",
        includeContext=True,
        contextAbsPath=False,
        outputFunction=no_log
    )

#=======================================================================================================================
# Executable
#=======================================================================================================================
if __name__ == "__main__":
    log_to_file("This is a test log entry.")
