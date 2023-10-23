from mysql.connector import connect, Error

'''
Файлик с подключением по строкам:
    1 - ip:port
    2 - username
    3 - password
'''

connect_data : list[str]

with open("connect_data.txt") as data:
    connect_data = data.readlines()

try:
    with connect(
        host = connect_data[0],
        user = connect_data[1],
        password = connect_data[2],
    ) as connection:
        print(connection)
except Error as e:
    print(e)