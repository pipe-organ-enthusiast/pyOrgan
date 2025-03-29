from icecream import ic, install # type: ignore


def save_log(log_data: str) -> None:
    """
    Save the log file to a specified location.
    """
    # Implementation of log saving
    log_file_path: str = "src/logs/log_file.txt"
    with open(log_file_path, "a") as log_file:
        log_data += "\n"
        log_file.write(log_data)

def clear_log() -> None:
    """
    Clear the log file.
    """
    # Implementation of log clearing
    log_file_path: str = "src/logs/log_file.txt"
    with open(log_file_path, "w") as log_file:
        log_file.write("")

def start_logging() -> None:
    install()
    ic.configureOutput(
        prefix="pyOrgan: ",
        includeContext=True,
        contextAbsPath=False,
        outputFunction=save_log
    )
    clear_log()
