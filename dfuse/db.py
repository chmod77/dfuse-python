import sqlite3
import tempfile
from sqlite3 import Error
import datetime

DB_NAME: str = 'dfusepy.sqlite3'
CREATE_TBL_SQL = """
                CREATE TABLE IF NOT EXISTS tokens (token TEXT, 
                created TIMESTAMP)
                """

INSERT_TOKEN_SQL = """ INSERT INTO tokens(token,created) VALUES(?,?) """

class DfusePersist:
    """
    Persists token to local sqlite3 database.
    """
    def create_connection(self, db_file=DB_NAME):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(
                db_file, detect_types=sqlite3.PARSE_DECLTYPES)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)
            return None

    def create_table(self, conn, sql: str = CREATE_TBL_SQL):
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
        return None
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
        conn.commit()
        return cur.lastrowid

    def drop_entries(self, conn):
        if conn:
            sql = 'DELETE FROM tokens'
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        return True

    def check_token_expiry(self):
        conn = persist.create_connection()
        current_time = datetime.datetime.now()

        if conn is not None:
            resp = self.read_token(conn)[0]
            token = resp[1]
            if datetime.timedelta(token, current_time) > 20:
                return True
            return False
            

    def read_token(self, conn) -> list:
        """
        Query all rows in the token table
        :param conn: the Connection object
        :return: list of token elements
        """

        cur = conn.cursor()

        cur.execute("SELECT * FROM tokens")

        rows = cur.fetchall()
        tokens = []
        if rows:
            for row in rows:
                print(f'row {row}')
                tokens.append(row)
        else:
            print(f'No rows. {rows}')
            return None
        return tokens

persist = DfusePersist()