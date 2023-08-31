import conn_poo_pymysql

db = conn_poo_pymysql.Database()

staff = db.getData("SELECT * FROM student")

for x in staff:
    #print(x[0])
    print(x)