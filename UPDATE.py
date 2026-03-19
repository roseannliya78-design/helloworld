import connection
cursor=connection.conn.cursor()
sql= "update student set name ='anu' where id=3"
cursor.execute(sql)
print("Update Sucessfully")
connection.conn.commit()
