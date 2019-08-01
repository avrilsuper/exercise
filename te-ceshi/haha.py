import  pymssql
serverName = "10.0.1.113"
userName = "sa"
passWod = "123456"
#conn = pymssql.connect(serverName,userName,passWod,"tempdb")
#conn = pymssql.connect(server = serverName,user = userName,password =passWod,database = "tempdb")
conn = pymssql.connect(serverName,userName,passWod,"JeezZKSG")
def runsql(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data

sql = "select name from sysobjects where xtype= 'U'  order by name"
a = runsql(sql)
for row in a:
    #print(row[0])
    #continue
    # cursor.execute("select top 10 * from"+row[0]+";")
    sql2 = "select * from"+ " "+ row[0]+";"
    b = runsql(sql2)
    for row2 in b:
        for single in row2:
            try:
                if str(single) == "139":
                    print(row)
            except:
                pass
            #if str(single).find("") > 0:
            #    print(row)
            #    print("=" * 10)

