import tornado.web
import tornado.ioloop
import pymysql
import numpy as np


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        conn = pymysql.connect(host='localhost',port=3306,user='bruce',password='#Gg10106')
        with conn.cursor() as cursor:
            cursor.execute('create database new_db')
            cursor.execute('use new_db')
            cursor.execute('create table students (id int unsigned not null auto_increment primary key,name char(8) not null,sex char(6) not null)')
            cursor.execute('insert into students values (6,"Chang","male")')
            cursor.execute('insert into students values (3,"Lin","female")')
            cursor.execute('delete from students where id =6')
            cursor.execute('update students set name ="Wu" where id =3')
            new_db.commit()
            cursor.execute('select * from students')
            result = cursor.fetchall()  
        self.write(str(np.array(result)))
     
        
application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
