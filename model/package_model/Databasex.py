import pymysql
class Databasex :
    conn = ""
    cursor=""

    def __init__(self):
       try: 
            self.conn = pymysql.connect(host='localhost',
                                       port=3306,
                                       user='root',
                                       passwd='',
                                       db='pop')
            self.cursor=self.conn.cursor()
            #print("ok") 
       except Exception as e:
           print(e)

    def close(self):
        self.conn.close()