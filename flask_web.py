from flask import Flask,request,render_template,redirect,url_for,session
from config import db_config,page_config
from dbutil.dbutil import DB
# import requests
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
app = Flask(__name__)
app.secret_key = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
db = DB(host=db_config['host'], mysql_user=db_config['user'], mysql_pass=db_config['passwd'], \
                mysql_db=db_config['db'])
page_config.setdefault('favicon','/static/img/favicon.ico')
page_config.setdefault('title','Woniu-cmdb')
page_config.setdefault('brand_name','Woniu-cmdb')

@app.route('/login',methods=['GET','POST'])
def login():
    if 'username' in session:
        return redirect('/')
    if request.method == "POST":
        name = request.form.get('username')
        passwd = request.form.get('password')
        print name
        print passwd
        obj = {"result":1}
        if name and passwd:
            sql = 'select * from user where username="%s" and password="%s"'%(name,passwd)
            print sql
            cur = db.execute(sql)
            # print cur.fetchone()
            if cur.fetchone():
                obj["result"] = 0
                session['username'] = name
        return json.dumps(obj)                
    else:
        return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/login')

@app.route('/page/<template>')
def render(template):
    if 'username' in session:
        return render_template('page/'+template+'.html',data=page_config,username=session['username'])
    else:
        return redirect('/login')
@app.route('/addapi', methods=['POST'])
def addapi():

    obj = request.form.to_dict()
    table = obj.pop('action_type')
    keys = obj.keys()
    values = obj.values()

    sql = 'insert into %s (%s) values ("%s")' % (table,','.join(keys),'","'.join(values))
    print sql
    db.execute(sql)
    res = {'result':'ok'}
    return json.dumps(res)
@app.route('/delapi', methods=['POST'])
def delapi():

    obj = request.form.to_dict()
    table = obj.pop('action_type')
    table_id = obj.pop('id')
    sql = 'delete from %s where id=%s' %(table,table_id)
    # sql = 'insert into %s (%s) values ("%s")' % (table,','.join(keys),'","'.join(values))
    print sql
    db.execute(sql)
    res = {'result':'ok'}
    return json.dumps(res)

@app.route('/listapi')
def listapi():
    action_type = request.args.get('action_type')
    sql = 'select * from '+action_type
    cur = db.execute(sql)
    res = {"result":cur.fetchall()}
    return json.dumps(res)

@app.route('/updateapi',methods=['POST'])
def updateapi():
    obj = request.form.to_dict()
    table = obj.pop('action_type')
    table_id = obj.pop('id')
    arr = []
    for key,val in obj.items():
        arr.append('%s="%s"'%(key,val))
    print arr
    keys = obj.keys()
    values = obj.values()
    sql = 'update %s set '%(table)

    sql += ','.join(arr)
    sql += ' where id='+table_id
    print sql
    db.execute(sql)
    res = {'result':'ok'}
    return json.dumps(res)

@app.route('/')
def index():
    return redirect('/page/user')
    # return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,port=9092,host='0.0.0.0')







