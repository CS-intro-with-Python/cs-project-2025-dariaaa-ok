import logging


def setup_logger(app):
    app.logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
    logging.getLogger("werkzeug").setLevel(logging.WARNING)




