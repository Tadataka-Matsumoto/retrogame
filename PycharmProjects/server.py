from flask import Flask, make_response, jsonify, request, render_template
import os

# dbとのコネクション
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

        # ps_cursor.execute("delete * from invader")#多分invaderのtableからgetする


        ps_cursor.close()

        #Use this method to release the connection object and send back to connection pool
        postgreSQL_pool.putconn(ps_connection)
        print("Put away a PostgreSQL connection")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while connecting to PostgreSQL", error)

# finally:
#     #closing database connection.
#     # use closeall method to close all the active connection if you want to turn of the application
#     if (postgreSQL_pool):
#         postgreSQL_pool.closeall
#     print("PostgreSQL connection pool is closed")


#flaskがexpressと同じような役割を果たしてサーバーを立ち上げる
app = Flask(__name__)#何している? expressと同じだろうな。。。


# http://127.0.0.1:5000をルートとして、("")の中でアクセスポイント指定＝＞なんで5000？？？
# @app.route("hoge")などで指定すると、http://127.0.0.1:5000/hogeでの動作を記述できる。
@app.route('/')
def hello_world():
    return "hello world!"

@app.route("/scores", methods=["GET", "POST"])
def get_scores():
    print("きたぞ！！！！！")
    if request.method == "POST":
        print(request.method)
        # ps_cursor.execute("INSERT INTO invader VALUES ${point}")
        return res
    elif request.method == "GET":  
        print(request.method)
        print(invader_records)
        return invader_records
        # return res
        # return render_template()

@app.route("/scores/<collection>", methods=["DELETE"])
def delete_collection(collection):

    # """ If the collection exists, delete it """

    # if collection in scores:
    # if collection in scores:
        # del scores[collection]
    # res = make_response(jsonify({}), 204)
    # return res
    print(collection)
    return collection

    # res = make_response(jsonify({"error": "Collection not found"}), 404)
    # return res

# @app.route('/scores', methods=['POST'])
# def add_scores():
#     results.append(request.get_json())
#     return '', 204


if __name__ == "__main__":

#    port = int(os.getenv("PORT", 8000))
#    app.run(host="0.0.0.0", port=port) 
    # 127.0.0.1:5000☜がdefaultみたい
    # webサーバー立ち上げ
    app.run()

#create 


#get


#delete









