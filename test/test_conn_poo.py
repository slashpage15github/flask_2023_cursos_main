import conn_poo

db = conn_poo.database()

staff = db.getData("SELECT * FROM student")

for x in staff:
    print(x["name"])