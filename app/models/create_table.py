import psycopg2

connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")

cursor = connection.cursor()


# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name text, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS requests (id INTEGER PRIMARY KEY, item text, typ text, description text, satatus text)"
cursor.execute(create_table)

connection.commit()

connection.close()
