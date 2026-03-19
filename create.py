import connection
cursor=connection.conn.cursor()
sql="create table student (id int,name varchar(20),age int)"
cursor.execute(sql)
print("table created successfully")