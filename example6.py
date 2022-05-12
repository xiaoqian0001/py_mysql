import pymysql

class Dect(object):

    def __init__(self,id,user,passwd):
        self.id = id
        self.user = user
        self.passwd = passwd
    
    def print_show(self):
        print('id='+str(self.id),end=' ')
        print('user='+self.user,end=' ')
        print('passwd='+self.passwd,end=' ')
        print('\t')

def main():
    coon = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='test',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    try:
        with coon.cursor() as cur:
            cur.execute(f"select Id as id ,username as user ,password as passwd from py_coon")
            # for row in cur.fetchall():
            #     print(f'Id:{row[0]},username:{row[1]},password:{row[2]}')
            #     print('~' * 20)
            for row in cur.fetchall():
                # print(f'Id:{row["id"]},username:{row["user"]},password:{row["passwd"]}')
                # print('~' * 20)
                dict = Dect(**row)
                dict.print_show()
                # dict = Dect(id=1,user='tom',passwd='123456')
    except pymysql.MySQLError as error :
        print(error)
    finally:
        coon.close()
    # print(coon)

if __name__ == '__main__':
    main()