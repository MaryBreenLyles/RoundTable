import pymysql
from flask import render_template

from flask import Flask     # > Import Flask class
app = Flask(__name__)       # > Create *instance* of Flask Class obj 
                            #   - (will be our WSGI application)*
                         
# Connect to the database with the pymysql library (make connection obj)
connection = pymysql.connect(host='localhost',
                             user='RoundTable',
                             password='kurtandmollie123',
                             db='RoundTable',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


#For playing around
@app.route("/")
def template_test():
    # Create new Jinja template (template.html), w/ keyword arg option
    return render_template('template.html', my_string="Scareh stuff.", my_list=[0,1,2,3,4,5])

#if __name__ == '__main__':
#    app.run(debug=True)


@app.route("/About")
def about_page():
    # Create new Jinja template
    return render_template('About.html')



@app.route('/showMsg')           # > Uses route() decorator to tell Flask
                                 #   what URL should trigger our func
def hello_world():               # > Name our function (also used to generate URL's for 
                                 #   this particular function)

    with connection.cursor() as cursor:  # cursor obj is created
        # Read a single record
        sql = "SELECT `msg_id`, `msg` FROM `Test` "
        cursor.execute(sql)
        results = cursor.fetchall() #list of dictionaries
        
        allMsgList = []

        for result in results:
            allMsgList.append(result['msg'])

        return render_template('template.html', my_string="Database Messages.", my_list=allMsgList)


@app.route('/addMsg/<msg>')

def add_message(msg):


    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `Test` (`msg_id`, `msg`) VALUES (0, %s)"
        cursor.execute(sql, (msg))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        return "You added \"" + msg + "\" to the database!"





''' * --  1st arg is name of app's module/package
          We use single module, so we use __name__ b/c
          __name__ is different depending on if started
          as app or imported as module. '__main__' for app
          vs. actual import name. (Flask needs name to know
          where to look for tmeplates, static files, etc.
          See Flask documentation for more.

'''
