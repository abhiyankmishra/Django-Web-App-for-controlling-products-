import pymysql as mysql
def connection():
    db=mysql.connect(host="localhost",user="root",password="8520",port=3306,db="iotproject")
    cmd=db.cursor()
    return db,cmd