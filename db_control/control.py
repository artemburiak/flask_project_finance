import sqlite3
from db_control import queries

class DbControl:
    connection = sqlite3.connect('db.db', check_same_thread=False)
    cursor = connection.cursor()

    def __init__(self):
        self.cursor.execute(queries.TABLE_CREATION_QUERY)
        self.cursor.execute(queries.TRANSACTION_CREATION_QUERY)
        print('Database connected')

    def reg_new_user(self, username, password):
        try:
            self.cursor.execute(queries.REG_USER_QUERY, [username, password])
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_user_by_login(self, username):
        user_info = self.cursor.execute(queries.GET_USER_BY_NAME, [username]).fetchone()
        return user_info

    def add_new_trans(self, amount, comment, type, id):
        self.cursor.execute(queries.TRANSACTION_ADD, [id, amount, comment, type])
        self.connection.commit()

    def get_transactions(self, id):
        r = self.cursor.execute(queries.GET_TRANSACTION_QUERY, [id]).fetchall()
        return r

data = DbControl()

if __name__ == "__main__":

    # if not db.reg_new_user("Anton", "123"):
    #     print("Username not unique!")
    data.add_new_trans(200, 'test from python', False, 1)