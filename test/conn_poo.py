import mysql.connector

class database :
    conn = ""
    cursor = ""

    def __init__(self):
        self.conn = mysql.connector.connect(user='root',
                                       password='',
                                       host='localhost',
                                       database='pop',
                                       port='3306')

        self.cursor = self.conn.cursor()

        print("Done")

    def getData(self, query):

        #Checking if the user has applied a string
        if isinstance(query, str):
            cursor = self.conn.cursor(dictionary=True)
            self.cursor.execute(query)
        else:
            return "You have provided a request that can't be processed"

        #Fetching all the results
        result = self.cursor.fetchall()

        #Returning back to the user
        return result

    def postData(self):
        print("Coming soon")


    def close(self):
        self.conn.close()