import pymysql

def main():
    #1.连接数据库
    coon = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='test',charset='utf8')
    try:
        # 2.获得游标对象
        with coon.cursor() as cur:
            # 执行SQL获得结果
            result = cur.execute("insert into py_coon values(3,'cat','123456')")
            if result == 1:
                print('ok')
            # 4. 提交操作
            coon.commit()
    except pymysql.MySQLError as error :
        print(error)
        # 回滚
        coon.rollback()
    finally:
        coon.close()
    # print(coon)

if __name__ == '__main__':
    main()