import connection
cursor=connection.conn.cursor()
sql="delete from student where name='ammu'"
cursor.execute(sql)
print("Delete Sucessfully")
connection.conn.commit()