"""
Dfuse DB Connection Module
"""

import sqlite3
from sqlite3 import Error
from typing import Any

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

    def create_connection(self, db_file=DB_NAME) -> Any:
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(
                db_file, detect_types=sqlite3.PARSE_DECLTYPES)
            return conn
        except Error as error:
            print(error)
            return None

    def create_table(self, conn, sql: str = CREATE_TBL_SQL) -> Any:
        """ create a table from the sql statement
        :param conn: Connection object
        :param sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(sql)
        except Error as error:
            print(error)
        return None
        # finally:
        #     conn.close()

    def insert_token(self, conn, data: tuple) -> Any:
        """
        Create a new token and insert it into the tokens table
        :param conn:
        :param data:
        :return: token
        """

        cur = conn.cursor()
        self.drop_entries(conn)
        cur.execute("INSERT INTO tokens(token,created) VALUES(?,?)", data)
        conn.commit()
        return cur.lastrowid

    def drop_entries(self, conn) -> Any:
        """
        Deletes all entries from the tokens table.
        """
        if conn:
            sql = 'DELETE FROM tokens'
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        return True

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
                tokens.append(row)
        else:
            return None
        return tokens


persist = DfusePersist()
