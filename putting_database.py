import psycopg2
import os
from dotenv import load_dotenv

class Postgres_connection():

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect_database(self):
        self.connected = psycopg2.connect(host=self.host, database=self.database, user=self.user,
                                  password=self.password)
        self.cursor = self.connected.cursor()

    def disconnect_database(self):
        self.cursor.close()
        self.connected.close()

    def query_execute(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        self.outrow = []
        while row is not None:
            self.outrow.append(row)
            row = self.cursor.fetchone()
        return self.outrow

load_dotenv()
print(os.environ.get('dbuser'))
print(os.environ.get('dbpassword'))

# username = os.environ.get('dbuser')
# password = os.environ.get('dbpassword')
#
# mydb = Postgres_connection(host="192.168.56.114", database="magazines", user="dbproduction",
#                            password="!@#$%Qwerty12345")
# mydb.connect_database()
# query1 = mydb.query_execute('select ar.id, ma.name, ty.type, au.author '
#                    'from public."Articles" as ar '
#                    'inner join magazines as ma '
#                    'on ar.magazines_id = ma.id '
#                    'inner join article_types as ty '
#                    'on ar.article_type_id = ty.id '
#                    'inner join author as au '
#                    'on ar.author_id = au.id;')
# query2 = mydb.query_execute('select author from author;')
# mydb.disconnect_database()
# # for i in query1:
# #    print(i[1] + ', ' + i[2] + ', ' + i[3])
# #
# # for i in query2:
# #    print(i[0])
#
# authors = {}
# for i in range(len(query2)):
#     authors[i] = query2[i][0]
