import pymysql
from flask import Flask, render_template
app = Flask(__name__)
 

connect = pymysql.connect(host='mydbinstance2.ciybnofnxn18.us-east-1.rds.amazonaws.com',
                       user='root', password='atglab3893', db='forest_data_dwi', charset='utf8')

cur = connect.cursor()

query = "SELECT * FROM forest_data_dwi WHERE (obsname,tm) IN (SELECT obsname, MAX(tm) AS tm FROM forest_data_dwi GROUP BY obsname)ORDER BY tm desc" # 마지막 날짜 최신 데이터 가져오는 쿼리

cur.execute(query)

data_list = cur.fetchall()



#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')     #접속하는 url
def index():
    
    query = "SELECT * FROM forest_data_dwi WHERE (obsname,tm) IN (SELECT obsname, MAX(tm) AS tm FROM forest_data_dwi GROUP BY obsname)ORDER BY tm desc" # 마지막 날짜 최신 데이터 가져오는 쿼리
    cur.execute(query)
    data_list = cur.fetchall()

    return render_template('index.html', data_list=data_list)
 


if __name__ == '__main__':
    #app.run()
    #호스트등을 직접 지정하고 싶을 경우.
    app.run(host="0.0.0.0", port="5000", debug=True)