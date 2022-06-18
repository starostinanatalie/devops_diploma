import psycopg2
import os
from flask import render_template, Flask
from datetime import datetime
import database_request

app = Flask(__name__)
password = os.getenv('password')

@app.route('/')
def home_page():
    current_date_time = datetime.now()
    password = os.environ.get('dbpassword')
    mydb = database_request.Postgres_connection(host="192.168.56.114", database="magazines", user="dbproduction",
                               password="!@#$%Qwerty12345")
    mydb.connect_database()
    query1 = mydb.query_execute('select ar.id, ma.name, ty.type, au.author '
                                'from public."Articles" as ar '
                                'inner join magazines as ma '
                                'on ar.magazines_id = ma.id '
                                'inner join article_types as ty '
                                'on ar.article_type_id = ty.id '
                                'inner join author as au '
                                'on ar.author_id = au.id;')
    query2 = mydb.query_execute('select author from author;')
    mydb.disconnect_database()
    authors = {}
    for i in range(len(query2)):
        authors[i] = query2[i][0]

    return render_template('index.html', current_date_time=current_date_time, author1=authors[1])


if __name__ == '__main__':
    app.run(host='localhost', port=5555, debug=True)
