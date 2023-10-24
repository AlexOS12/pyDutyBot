from mysql.connector import connect, Error

'''
Файлик с подключением по строкам:
    1 - ip:port
    2 - username
    3 - password
    4 - database
'''

def sql_executor(sql_query : str):
    global sql
    try:
        sql.execute(sql_query)
        return "asd"
    except:
        return False

def shutdown():
    global connection
    connection.commit()

connect_data : list[str]

with open("connect_data.txt") as data:
# with open("C:\\Users\\mayor\\Documents\\GitHub\\pyDutyBot\\app\\connect_data.txt") as data:
    connect_data = data.readlines()
    connect_data = [i.replace('\n', '') for i in connect_data]

print('\n'.join(connect_data))

sql = ''

try:
    # with connect(
    #     host = connect_data[0],
    #     user = connect_data[1],
    #     password = connect_data[2],
    #     database = connect_data[3],
    # ) as connection:
    #     print("Успешный подсос к БД")
    #     if __name__ == "__main__":
    #         while 1:
    #             query = input(">>> ")
    #             if query == 'none':
    #                 connection.commit()
    #                 exit()
    #             try:
    #                 with connection.cursor() as cursor:
    #                     cursor.execute(query)
    #                     for db in cursor:
    #                         print(db)
    #             except:
    #                 print("Что-то пошло не так")
    #     else:
    #         sql = connection.cursor()
    connection = connect(
        host = connect_data[0],
        user = connect_data[1],
        password = connect_data[2],
        database = connect_data[3],
    )
    print("Успешный подсос к бд")
    sql = connection.cursor()
except Error as e:
    print(e)
    exit()

connection.commit()