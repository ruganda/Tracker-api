import psycopg2
class Request:
    table_title = 'requests'
    def __init__(self, id, item, typ, description, status ="new"):
        self.id = id 
        self.item =item
        self.typ =typ
        self.description = description
        self.status = status

    @classmethod
    def find_by_id(cls, id):
        connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.table_title)
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()

        if row:
            return row


    @classmethod
    def insert(cls, request):
        connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?,?,?,?)".format(table=cls.table_title)
        cursor.execute(query, (request['item'], request['typ'],request['description'],request['status']))

        connection.commit()
        connection.close()


    @classmethod
    def update(cls, request):
        connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()

        query = "UPDATE {table} SET item=?, typ=?, description=? WHERE id=?".format(table=cls.table_title)
        cursor.execute(query, (request['item'], request['typ'], request['description']))

        connection.commit()
        connection.close()

    @classmethod
    def fetch_all(self):
        connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.table_title)
        result = cursor.execute(query)
        requests = []
        for row in result:
            requests.append({'item': row[0], 'typ': row[1], 'description': row[2], 'status': row[3] })
        connection.close()