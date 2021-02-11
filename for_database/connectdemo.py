# first import the mysql connector
import mysql.connector

# import the error module from mysql connector
from mysql.connector import Error


# define the connector function
def connect_fetch():
    ''' function to connect and fetch rows in a database '''
    # pass

    # create a variable for the connector object
    conn = None

    try:
        conn = mysql.connector.connect(host='localhost',
                                       # database='cape_codd',
                                       database='first_table',
                                       user='solutionCraftsman',
                                       password='#7&det5$oi*!jhd@p!',
                                       # auth_plugin='mysql_native_password'
                                       )
        print('Connected to the database')
        db_cursor = conn.cursor()

        sql_select(db_cursor)

        # create a variable to contain the sql query to be executed
        sql = "INSERT INTO Human (name, color, gender, blood_group) VALUES (%s, %s, %s, %s)"

        # create a list variable to contain all the values we want to insert into the database
        val = [
            ('Hannah', 'White', 'Female', 'B-'),
            # ('1009', 'Michael', 'Brown', 'Male', 'O-'),
            # ('1010', 'Sandy', 'Black', 'Male', 'O+'),
            # ('1011', 'Green', 'Yellow', 'Male', 'AB'),
            # ('1012', 'Richard', 'Black', 'Male', 'B+')
        ]

        # execute the query using the executemany() function
        db_cursor.executemany(sql, val)

        # commit to the database
        conn.commit()

        # print a success message
        print(db_cursor.rowcount, "rows was inserted.")

        # db_cursor.

        # close the cursor
        db_cursor.close()

    except Error as e:
        print('Not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database shutdown!!')


def sql_select(db_cursor):
    # select query
    sql_select_query = "select * from Human"
    # cursor variable
    db_cursor.execute(sql_select_query)
    records = db_cursor.fetchall()
    # print select output
    print("\nPrinting each buyer record")
    for rows in records:
        print("Buyer name:", rows[0])
        print("Department:", rows[0])
        print("Position:", rows[0])
        print("Supervisor:", rows[0])
        print()


connect_fetch()
