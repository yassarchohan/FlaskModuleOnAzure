import mysql.connector

myconnection = mysql.connector.connect(
            host='localhost',
            user='',
            password='',
            database='test'
        )

# def getMysqlData():
#     myconnection = mysql.connector.connect(
#         host='localhost',
#         user='',
#         password='',
#         database='test'
#     )
#     cursor = myconnection.cursor()
#     return cursor


def searchall():
    list2 = []
    try:
        cursor = myconnection.cursor()
        query = "select * from Employee"
        cursor.execute(query)
        results = cursor.fetchall()

        i = 0
        for items in results:
            finaldict = {'First_Name': items[1], 'Last_Name': items[2], 'Age': items[3]}
            list2.append(finaldict)

    except Exception as e:
        print(e)

    return list2


def searchempbyname(name):
    list2 = []
    try:
        cursor = myconnection.cursor()
        if name:
            query = "select * from Employee where First_Name like '%{}%'".format(name)

        else:
            query = "select * from Employee"
        cursor.execute(query)
        results = cursor.fetchall()

        i = 0
        for items in results:
            finaldict = {'First_Name': items[1], 'Last_Name': items[2], 'Age': items[3]}
            list2.append(finaldict)

    except Exception as e:
        print(e)

    return list2

