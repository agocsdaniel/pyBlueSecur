import logging


class Logger(object):
    def __init__(self, name="__name__"):
        self.name = name
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - {}: %(message)s'.format(name))
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)

        self.logger = logging.getLogger(self.name)
        loglevel = logging.INFO
        self.logger.setLevel(loglevel)
        self.logger.addHandler(self.handler)

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.handler)
        return logger
