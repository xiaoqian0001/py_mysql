import pymysql

def main():
    id = int(input())
    passwd = input()
    coon = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='test',charset='utf8')
    try:
        with coon.cursor() as cur:
            result = cur.execute(f"update py_coon set password = {passwd} where Id ={id}")
            if result == 1:
                print('ok')
            coon.commit()
    except pymysql.MySQLError as error :
        print(error)
        coon.rollback()
    finally:
        coon.close()
    # print(coon)

if __name__ == '__main__':
    main()