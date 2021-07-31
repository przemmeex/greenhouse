import logging
import os
import psycopg2
import time
from helpers import read_config


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class LogDBHandler(logging.Handler):
    def __init__(self, sql_conn, sql_cursor, db_table):
        logging.Handler.__init__(self)
        self.sql_cursor = sql_cursor
        self.sql_conn = sql_conn
        self.db_table = db_table

    def emit(self, record):
        # Set current time
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))
        # Clear the log message so it can be put to db via sql (escape quotes)
        self.log_msg = record.msg
        self.log_msg = self.log_msg.strip()
        self.log_msg = self.log_msg.replace('\'', '\'\'')
        # Make the SQL insert
        if (self.db_table == "measurements"):
            measured_data = record.msg.split('--')
            sql = f'INSERT INTO {self.db_table} (time, temp_dig, temp_analog, humidity_analog, is_day, is_fan_on) VALUES (\'{current_time}\', {measured_data[0]}, {measured_data[1]}, {measured_data[2]}, {measured_data[3]}, {measured_data[4]})'
        else:
            sql = f'INSERT INTO {self.db_table} (body) VALUES (\'{record.created} - {record.levelname} - {record.msg}\')'
        try:
            self.sql_cursor.execute(sql)
            self.sql_conn.commit()

        except Exception as e:
            pass


class Logger(metaclass=Singleton):
    logging.root.setLevel(logging.NOTSET)
    conf = read_config()
    try:
        connection = psycopg2.connect(
                f'''host={conf["connectionString"]["host"]}
                user={conf["connectionString"]["user"]}
                password={conf["connectionString"]["password"]}
                dbname={conf["connectionString"]["dbname"]}''')
        cursor = connection.cursor()
        logdb = LogDBHandler(connection, cursor, "measurements")
        log_errors = LogDBHandler(connection, cursor, "errors")

        logger = logging.getLogger(f"{__name__}_measurements")
        logger.addHandler(logdb)
        logger.setLevel('DEBUG')

        logger_errors = logging.getLogger(__name__)
        logger_errors.addHandler(log_errors)
        logger_errors.setLevel('DEBUG')


    except:
        script_dir = os.path.dirname(__file__)
        log_file = os.path.join(script_dir, "main.log")
        f_handler = logging.FileHandler(log_file, mode='a')
        f_handler.setLevel(logging.DEBUG)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        f_handler.setFormatter(f_format)

        logger = logging.getLogger(__name__)
        logger.addHandler(f_handler)

        # logger_error = logging.getLogger(__name__)
        # logger_error.addHandler(f_handler)


    def debug(self, msg):
        self.logger_errors.debug(msg)

    def error(self, msg):
        self.logger_errors.error(msg)

    def info(self, msg):
        self.logger_errors.info(msg)

    def warning(self, msg):
        self.logger_errors.warning(msg)

    def measurements(self, msg):
        self.logger.info(msg)
