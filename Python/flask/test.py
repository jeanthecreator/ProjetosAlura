import mysql.connector
from mysql.connector import errorcode

print('Connecting ...')

try:

    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'admin'
    )
   

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuario ou senha invalida')
    else:
        print(err)


