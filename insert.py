import connection
cursor=connection.conn.cursor()
sql="insert into student value (%s,%s,%s)"
value=[(1,'ammu',15),(2,'rosu',66),(3,'annamma',90)]
cursor.executemany(sql,value)
print("Insert Sucessfully")
connection.conn.commit()