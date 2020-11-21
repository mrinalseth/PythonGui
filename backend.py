import mysql.connector

def connect():
    conn = mysql.connector.connect(user='root', password="infant@123",
    database = 'telusko',
    port=3306,
    host="localhost",
    auth_plugin='mysql_native_password'
    )
    cur = conn.cursor()
    cur.execute(
        "create table if not exists book("
        "id integer primary key auto_increment,"
        "title varchar(100),"
        "author varchar(20)," 
        "year integer,"
        "isbn integer)"
    )
    conn.commit()
    conn.close()

def insert(a,b,c,d):
    conn = mysql.connector.connect(user='root', password="infant@123",
    database='telusko',
    port=3306,
    host="localhost",
    auth_plugin='mysql_native_password'
    )
    connect()
    cur = conn.cursor()
    cur.execute(f'''insert into book values(null,"{a}","{b}",{c},{d})''')
    conn.commit()
    conn.close()


def view():
    conn = mysql.connector.connect(user='root', password="infant@123",
    database='telusko',
    port=3306,
    host="localhost",
    auth_plugin='mysql_native_password'
    )
    cur = conn.cursor()
    cur.execute('''select * from book''')
    row = cur.fetchall()
    return row
    conn.close()


def search(title="",author="",year=-1,isbn=-1):
    conn = mysql.connector.connect(user='root', password="infant@123",
    database='telusko',
    port=3306,
    host="localhost",
    auth_plugin='mysql_native_password'
    )
    cur = conn.cursor()
    cur.execute(f'''select * from book
    where title="{title}" or author="{author}" or year={year} or isbn={isbn}''')
    row = cur.fetchall()
    return row
    conn.close()

def delete(id):
    conn = mysql.connector.connect(user='root', password="infant@123",
    database='telusko',
    port=3306,
    host="localhost",
    auth_plugin='mysql_native_password'
    )
    cur = conn.cursor()
    cur.execute(f'''delete from book where id = {id}''')
    conn.commit()
    conn.close()


def update(id,title,author,year,isbn):
    conn = mysql.connector.connect(user='root', password="infant@123",
    database='telusko',
    port=3306,
    host="localhost",
    auth_plugin='mysql_native_password'
    )
    cur = conn.cursor()
    cur.execute(f'''update book set title="{title}",author="{author}", year={year}, isbn={isbn} where id={id}''')
    conn.commit()
    conn.close()
