import sqlite3
import tempfile
from sqlite3 import Error


class DfusePersist:
    def __init__(self):
        pass

    def create_connection(self, db_file=__DB_NAME):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(
                db_file, detect_types=sqlite3.PARSE_DECLTYPES)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)
            return None

    def create_table(self, conn, sql: str = __CREATE_TBL_SQL):
        """ create a table from the sql statement
        :param conn: Connection object
        :param sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)
        # finally:
        #     conn.close()

    def insert_token(self, conn, data):
        """
        Create a new token into the tokens table
        :param conn:
        :param data:
        :return: token
        """

        cur = conn.cursor()
        cur.execute("INSERT INTO tokens(token,created) VALUES(?,?)", data)
        return cur.lastrowid

    def drop_entries(self, conn):
        if conn:
            sql = 'DELETE FROM tokens'
            cur = conn.cursor()
            cur.execute(sql)
        return True