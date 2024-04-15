import mysql.connector

insert_query = "insert into country values(5,'Turkey','Ankara')"
update_query = "update country set capital='Istanbul' where id=5"
delete_query = "delete from country where id=2"

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    curs = con.cursor()
    curs.execute(update_query)
    con.commit()
    con.close()
except:
    print("Connection is unsuccessful")
print("Finished")

