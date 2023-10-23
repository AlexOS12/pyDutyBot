from mysql.connector import connect, Error

'''
Файлик с подключением по строкам:
    1 - ip:port
    2 - username
    3 - password
    4 - database
'''

connect_data : list[str]

with open("connect_data.txt") as data:
    connect_data = data.readlines()
    connect_data = [i.replace('\n', '') for i in connect_data]

print('\n'.join(connect_data))


try:
    with connect(
        host = connect_data[0],
        user = connect_data[1],
        password = connect_data[2],
        database = connect_data[3],
    ) as connection:
        print("Успешный подсос к БД")
        while 1:
            query = input(">>> ")
            if query == 'none':
                connection.commit()
                exit()
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    for db in cursor:
                        print(db)
            except:
                print("Что-то пошло не так")
except Error as e:
    print(e)