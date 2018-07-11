from app.core import init_app, connect_db
import logging
import sys

app = init_app()
if __name__ == '__main__':
    try:
        app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=int(app.config['PORT']))
    except Exception:
        logging.error("Cannot start Flask app:  {} {}".format(
                                                            sys._getframe().f_code.co_name,
                                                            str(sys.exc_info())
                                                        ))
