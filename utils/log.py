import logging


def setup_logger(name):
    # Create the logger object.
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create stream handler for the logger and the level of logging.
    stream_handler = logging.StreamHandler
    stream_handler.setLevel(logging.DEBUG)

    # Specify a format for the log stream handler.
    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Set the format for the log stream.
    stream_handler.setFormatter(log_formatter)

    # Add the stream handler to the logger.
    logger.addHandler(stream_handler)
