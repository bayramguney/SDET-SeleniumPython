# we need to install mysql  and create database and table and all
# then install mysql-connector-python from setting
import mysql.connector

select_query = "select * from country"


try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    curs = con.cursor()
    curs.execute(select_query)
    for row in curs:
        print(row[0],row[1],row[2])

    con.commit()
    con.close()
except:
    print("Connection is unsuccessful")
print("Finished")
