import psycopg2
from psycopg2 import pool
try:
    postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20,user = "postgres",
                                              password = "tdtk1538",
                                              host = "127.0.0.1",
                                              port = "5432",
                                              database = "game")
    if(postgreSQL_pool):
        print("Connection pool created successfully")

    # Use getconn() to Get Connection from connection pool
    ps_connection  = postgreSQL_pool.getconn()

    if(ps_connection):
        print("successfully recived connection from connection pool ")
        ps_cursor = ps_connection.cursor() # SQL実行のためカーソルを作成
        ps_cursor.execute("select * from invader")#多分invaderのtableからgetする
        invader_records = ps_cursor.fetchall()

        print ("Displaying rows from invader table")
        for row in invader_records: # 結果をフェッチ、今回は1行のみ
            print (row)

        ps_cursor.close()

        #Use this method to release the connection object and send back to connection pool
        postgreSQL_pool.putconn(ps_connection)
        print("Put away a PostgreSQL connection")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
    # use closeall method to close all the active connection if you want to turn of the application
    if (postgreSQL_pool):
        postgreSQL_pool.closeall
    print("PostgreSQL connection pool is closed")