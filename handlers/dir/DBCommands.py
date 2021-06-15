import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    connection = psycopg2.connect(user="postgres",
                                  password="1111",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute("""CREATE DATABASE freelance_bot""")
    print('База данных "freelance_bot" создана' )
    cursor.close()
    connection.close()
except:
    pass
connection = psycopg2.connect(user="postgres",
                              password="1111",
                              host="127.0.0.1",
                              port="5432",
                              database = 'freelance_bot')
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

class DBCommands:
    def create(self):
        CREATE_FREELANCERS = """CREATE TABLE IF NOT EXISTS freelancers(id INTEGER UNIQUE, username TEXT, name TEXT, description TEXT, city TEXT, number BIGINT, status TEXT);"""
        CREATE_CUSTOMERS = """CREATE TABLE IF NOT EXISTS customers(id INTEGER UNIQUE, username TEXT, name TEXT, city TEXT, cost INTEGER, bonus INTEGER, n INTEGER);"""
        CREATE_REFLINKS = """CREATE TABLE IF NOT EXISTS reflinks (reflink TEXT UNIQUE, name TEXT,count INTEGER);"""

        cursor.execute(CREATE_FREELANCERS)
        cursor.execute(CREATE_CUSTOMERS)
        cursor.execute(CREATE_REFLINKS)
        connection.commit()



    def select_freelancer(self, chatid):
        SELECT_FREELANCER = f"""SELECT count(*) FROM freelancers WHERE id={chatid}"""
        command = SELECT_FREELANCER
        cursor.execute(command)
        return cursor.fetchone()[0]


    def select_all_freelancer(self):
        SELECT_ALL_FREELANCER = """SELECT * FROM freelancers"""
        command = SELECT_ALL_FREELANCER
        cursor.execute(command)
        return cursor.fetchall()


    def add_freelancer(self, par):
        ADD_FREELANCER = f"""INSERT INTO freelancers (id, username, name, status) VALUES ({par[0]}, '{par[1]}', '{par[2]}', '{par[3]}')"""
        command = ADD_FREELANCER
        cursor.execute(command, par)


    def update_username(self, par):
        UPDATE_USERNAME = f"""UPDATE freelancers SET username = '{par[0]}' WHERE id = {par[1]}"""
        command = UPDATE_USERNAME
        cursor.execute(command, par)


    def update_city(self, par):
        UPDATE_CITY = f"""UPDATE freelancers SET city = '{par[0]}' WHERE id = {par[1]}"""
        command = UPDATE_CITY
        cursor.execute(command, par)


    def update_number(self, par):
        UPDATE_NUMBER = f"""UPDATE freelancers SET number = {par[0]} WHERE id = {par[1]}"""
        command = UPDATE_NUMBER
        cursor.execute(command, par)


    def update_status(self, par):
        UPDATE_STATUS = f"""UPDATE freelancers SET status = '{par[0]}' WHERE id = {par[1]}"""
        command = UPDATE_STATUS
        cursor.execute(command, par)


    def select_name(self, chatid):
        SELECT_NAME = f"""SELECT name FROM freelancers WHERE id = {chatid}"""
        command = SELECT_NAME
        cursor.execute(command, chatid)
        return cursor.fetchone()[0]


    def select_city(self, chatid):
        SELECT_CITY = f"""SELECT city FROM freelancers WHERE id = {chatid}"""
        command = SELECT_CITY
        cursor.execute(command, chatid)
        return cursor.fetchone()[0]


    def select_number(self, chatid):
        SELECT_NUMBER = f"""SELECT number FROM freelancers WHERE id = {chatid}"""
        command = SELECT_NUMBER
        cursor.execute(command, chatid)
        return cursor.fetchone()[0]


    def select_status(self, chatid):
        SELECT_STATUS = f"""SELECT status FROM freelancers WHERE id = {chatid}"""
        command = SELECT_STATUS
        cursor.execute(command, chatid)
        return cursor.fetchone()[0]

    def delete_freelancer(self, chatid):
        DELETE_FREELANCER = f"""DELETE FROM freelancers WHERE id = {chatid}"""
        command = DELETE_FREELANCER
        cursor.execute(command, chatid)


    def update_description(self, par):
        UPDATE_DESCRIPTION = f"""UPDATE freelancers SET description = '{par[0]}' WHERE id = {par[1]}"""
        command = UPDATE_DESCRIPTION
        cursor.execute(command, par)


    def select_description(self, chatid):
        SELECT_DESCRIPTION = f"""SELECT description FROM freelancers WHERE id = {chatid}"""
        command = SELECT_DESCRIPTION
        cursor.execute(command, chatid)
        return cursor.fetchone()[0]






    def add_customer(self, par):
        ADD_CUSTOMER = f"""INSERT INTO customers (id, username, name, cost, bonus, n) VALUES ({par[0]}, '{par[1]}', '{par[2]}', 0, 0, 0)"""
        command = ADD_CUSTOMER
        cursor.execute(command, par)


    def select_all_customer(self):
        SELECT_ALL_CUSTOMER = """SELECT * FROM customers"""
        command = SELECT_ALL_CUSTOMER
        cursor.execute(command)
        return cursor.fetchall()



    def select_city_customer(self, chatid):
        SELECT_CITY_CUSTOMER = f"""SELECT city FROM customers WHERE id = {chatid}"""
        command = SELECT_CITY_CUSTOMER
        cursor.execute(command, chatid)
        return cursor.fetchone()[0]

    def update_city_customer(self, par):
        UPDATE_CITY_CUSTOMER = f"""UPDATE customers SET city = '{par[0]}' WHERE id = {par[1]}"""
        command = UPDATE_CITY_CUSTOMER
        cursor.execute(command, par)


    def update_n(self, par):
        UPDATE_N = f"""UPDATE customers SET n = {par[0]} WHERE id = {par[1]}"""
        command = UPDATE_N
        cursor.execute(command, par)


    def select_n(self, chatid):
        SELECT_N = f"""SELECT n FROM customers WHERE id = {chatid}"""
        command = SELECT_N
        cursor.execute(command, chatid)
        return cursor.fetchone()[0]

    def update_bonus(self, par):
        UPDATE_BONUS = f"""UPDATE customers SET bonus = {par[0]} WHERE id = {par[1]}"""
        command = UPDATE_BONUS
        cursor.execute(command, par)


    def select_bonus(self, chatid):
        SELECT_BONUS = f"""SELECT bonus FROM customers WHERE id = {chatid}"""
        command = SELECT_BONUS
        cursor.execute(command, chatid)
        return cursor.fetchone()[0]





    def select_all_reflinks(self):
        SELECT_ALL_REFLINKS = """SELECT * FROM reflinks"""
        command = SELECT_ALL_REFLINKS
        cursor.execute(command)
        return cursor.fetchall()


    def add_reflink(self, par):
        ADD_REFLINK = f"""INSERT INTO reflinks (reflink, name, count) VALUES ('{par[0]}', '{par[1]}', 0)"""
        command = ADD_REFLINK
        cursor.execute(command, par)


    def delete_reflink(self, name):
        DELETE_REFLINK = f"""DELETE FROM reflinks WHERE name = '{name}' """
        command = DELETE_REFLINK
        cursor.execute(command, name)

    def select_count_reflinks(self, args):
        SELECT_COUNT_REFLINKS = f"""SELECT count FROM reflinks WHERE reflink = {args}"""
        command = SELECT_COUNT_REFLINKS
        cursor.execute(command, args)
        return cursor.fetchone[0]

    def update_reflinks(self, n, args):
        UPDATE_REFLINKS = f"""UPDATE reflinks SET count  = {n + 1}  WHERE reflink = {args}"""
        command = UPDATE_REFLINKS
        cursor.execute(command, n, args)
