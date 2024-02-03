# Python3 -v venv virt
# Source virt/bin/activate
# Pip install django
# Pip install mysql
# Pip install mysql-connector-python
# Pip install mysql-connector
import mysql.connector
dataBase = mysql.connector.connect(user='root', password='password', host='localhost',
auth_plugin='mysql_native_password')
cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE dentist")
print('All done!')