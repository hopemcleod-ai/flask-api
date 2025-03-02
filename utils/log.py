import logging


def setup_logger(name):
    """
    Set up a logger with a specified name. The logger will log debug level
    and higher messages to the concole.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: The configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Configure logging to output to the console (stdout)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    stream_handler.setFormatter(log_formatter)

    # Add the formatted stream handler to the logger.
    logger.addHandler(stream_handler)

    return logger



