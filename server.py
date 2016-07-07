import os
import psycopg2
import psycopg2.extras

import sys
reload(sys)
sys.setdefaultencoding("UTF8")


from flask import Flask, render_template, request
app = Flask(__name__)

def connectToDB():
    connectionString = 'dbname=[INSERT DB] user=[INSERT USER] password=[INSERT PASSWORD] host=localhost'
    print connectionString
    try:
        return psycopg2.connect(connectionString)
    except:
        print("Can't Connect to the Database")


@app.route('/')
def mainIndex():
    return render_template('index.html', selectedMenu='Home')

@app.route('/searchresults', methods=['GET','POST'])
def searchResults():
    con = connectToDB()
    cur = con.cursor()
    entry = request.form['worldSearch']
    

    if request.method =='POST':
        print("Inside first If statment!")
        dict = request.form
        for key in dict:
            print 'form key '+dict[key] , key
        
        print([request.form['worldSearch']])
        cur.execute("SELECT name,region,population FROM country WHERE name = %s or continent = %s or code = %s", (request.form['worldSearch'],request.form['worldSearch'],request.form['worldSearch']))
            

                    
    results = cur.fetchall()
    return render_template('searchresults.html', entryfield=entry, names=results)
    
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
