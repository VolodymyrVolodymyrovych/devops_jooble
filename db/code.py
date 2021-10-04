from config import host, user, password, db_name
import psycopg2

try:
    # connect to database
    connection = psycopg2.connect(
            host=host,
            user=user,
            port=25060,
            password=password,
            database=db_name
    )

    connection.autocommit = True

    # the cursor for performing database operations
    with connection.cursor() as cursor:
        cursor.execute(
                "SELECT version();"
        )
        print(f"version: {cursor.fetchone()}")

     # Create a new table
    with connection.cursor() as cursor:
         cursor.execute(
                """CREATE TABLE users(
                    id serial PRIMARY KEY,
                    first_name varchar(50) NOT NULL,
                    second_name varchar(50) NOT NULL);"""
        )
    print("[INFO] Table created seccussfully")

     # Insert data to TABLE
    with connection.cursor() as cursor:
        cursor.execute(
                """INSERT INTO users (first_name, second_name) VALUES
                ('Vova', 'Albertovich'),
                ('Oleg', 'Olegovich'),
                ('Olena', 'Olenovna'),
                ('Tom', 'Olegovich'),
                ('Vadym', 'Zhmurovich'),
                ('Vlad', 'Dracula'),
                ('Inokentiy', 'Popolo'),
                ('Lavrentiy', 'Pavlovich'),
                ('Pavel', 'Vladimirovich')
                """
        )
    print("[INFO] Data seccussfully inserted.")


    answer = 100000
    while answer != 0:
        print("==============================")
        print("0. Exit")
        print("1.Show the table")
        print("2.Delete the row")
        print("3.Add row")
        print("==============================")

        answer = int(input("Your decision: "))

        if answer == 1:
            id_ = input("write ID: ")
            with connection.cursor() as cursor:
                cursor.execute(
                        """SELECT * FROM users where id = %s;"""
                ,[id_])
                print(cursor.fetchone())

        if answer == 2:
            id_del = input("write ID: ")
            with connection.cursor() as cursor:
                cursor.execute(
                        """DELETE FROM users where id =%s;""",[id_del])
                print("[INFO] Delted")

        if answer == 3:
            name_add = input("write name: ")
            second_add = input("second name: ")
            with connection.cursor() as cursor:
                cursor.execute(
                        """INSERT INTO users (first_name, second_name)
                        VALUES
                        (%s, %s)"""
                ,(name_add, second_add)
                )

except Exception as _ex:
    print ("[ERROR] Error while working with Postgresql.", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] Postgresql connection closed.")
