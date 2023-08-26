import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database="pop"
)
 
print(dataBase)


# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database
#cursorObject.execute("CREATE DATABASE pop")

# # creating table
# studentRecord = """CREATE TABLE STUDENT (
#                    NAME  VARCHAR(20) NOT NULL,
#                    BRANCH VARCHAR(50),
#                    ROLL INT NOT NULL,
#                    SECTION VARCHAR(5),
#                    AGE INT
#                    )"""
  
# table created
#cursorObject.execute(studentRecord)


# sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
# VALUES (%s, %s, %s, %s, %s)"
# val = ("Ram", "CSE", "85", "B", "19")
   
# cursorObject.execute(sql, val)
# dataBase.commit()

 
# #inserta varios registro
# sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
# VALUES (%s, %s, %s, %s, %s)"
# val = [("Nikhil", "CSE", "98", "A", "18"),
#        ("Nisha", "CSE", "99", "A", "18"),
#        ("Rohan", "MAE", "43", "B", "20"),
#        ("Amit", "ECE", "24", "A", "21"),
#        ("Anil", "MAE", "45", "B", "20"),
#        ("Megha", "ECE", "55", "A", "22"),
#        ("Sita", "CSE", "95", "A", "19")]
   
# cursorObject.executemany(sql, val)
# dataBase.commit() 

# query = "SELECT NAME, ROLL FROM STUDENT"
# cursorObject.execute(query)
   
# myresult = cursorObject.fetchall()
   
# for x in myresult:
#     print(x)
 

# query = "SELECT * FROM STUDENT where AGE >=20"
# cursorObject.execute(query)
   
# myresult = cursorObject.fetchall()
   
# for x in myresult:
#     print(x)

# #update
# query = "UPDATE STUDENT SET AGE = 100 WHERE Name ='Ram'"
# cursorObject.execute(query)
# dataBase.commit()


query = "DELETE FROM STUDENT WHERE NAME = 'Ram'"
cursorObject.execute(query)
dataBase.commit()
  
# Disconnecting from the server
dataBase.close()