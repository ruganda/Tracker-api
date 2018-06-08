from .create_table import connection
import psycopg2


class Request:
    table_title = 'requests'

    def __init__(self, id, item, typ, description, status="pending"):
        self.id = id
        self.item = item
        self.typ = typ
        self.description = description
        self.status = status

    @classmethod
    def find_by_id(cls, uid):
        connection = psycopg2.connect(
            "dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM requests WHERE Id = %(id)s", {'id': uid})
        row = cursor.fetchone()
        connection.close()

        if row:
            print(row)
            return row

    @classmethod
    def insert(cls, request, owner):
        connection = psycopg2.connect(
            "dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()
        query = "INSERT INTO requests (item, typ, description, status, owner) VALUES(%s, %s, %s, %s, %s)"
        cursor.execute(query, (request['item'], request['typ'],
                               request['description'], request['status'], owner))

        connection.commit()
        connection.close()

    @classmethod
    def update(cls, rId, request):
        connection = psycopg2.connect(
            "dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()
        cursor.execute("UPDATE requests SET item=%s, typ=%s, description=%s WHERE id=%s",
                       (request['item'], request['typ'], request['description'], rId))

        connection.commit()
        connection.close()

    @classmethod
    def fetch_all(self, owner):
        connection = psycopg2.connect(
            "dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM requests WHERE owner = %(owner)s", {'owner': owner})
        rows = cursor.fetchall()
        requests = []
        for row in rows:
            print(row)
            requests.append({'id': row[0], 'item': row[1], 'typ': row[2],
                             'description': row[3], 'status': row[4], "Requester": row[5]})
        connection.close()
        return requests
    ######################################################################################################
