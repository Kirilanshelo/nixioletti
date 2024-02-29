import logging
import coloredlogs

def init_log(logfile, loglevel):
    format_string = '%(asctime)s [%(process)d] [%(levelname)s] (%(name)s:%(funcName)s) %(message)s'
    time_string = "%y-%m-%d %H:%M:%S"
    console_formatter = coloredlogs.ColoredFormatter(format_string, time_string)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    handlers = [console_handler]

    time_formatter = logging.Formatter(format_string, time_string)
    time_handler = logging.FileHandler(f'{logfile}')
    time_handler.setFormatter(time_formatter)
    handlers += [time_handler]

    # steal uvicorn logger
    logging.getLogger("uvicorn").handlers.clear()
    access_log = logging.getLogger("uvicorn.access")
    access_log.handlers.clear()
    access_log.addHandler(console_handler)
    access_log.addHandler(time_handler)

    # steal gunicorn logger
    logging.getLogger("gunicorn").handlers.clear()
    access_log = logging.getLogger("gunicorn.access")
    access_log.handlers.clear()
    access_log.addHandler(console_handler)
    access_log.addHandler(time_handler)

    # current level
    loglevel = logging.getLevelName(loglevel)
    if type(loglevel) != int:
        loglevel = logging.DEBUG

    # load config
    logging.basicConfig(
        level=loglevel,
        handlers=handlers,
    )