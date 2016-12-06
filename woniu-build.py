
# coding=utf-8
import os,sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
from config import db_config,page_config
import sys
from flask_web import db

head = '''
{% extends "layout.html" %}
{% block body %}
{% endblock %}
    
{% block js %}
    <script>	
        $(function() {
            $.rebootOps(
'''

foot = '''
            )
        })
    </script>
{% endblock %}

'''

def gen_file(config):
    with open('templates/page/'+config['name']+'.html','w') as f:
    	f.write(head)
    	f.write('              '+json.dumps(config))
    	f.write(foot)
        print config['name']+' build success'

def gen_config(config):
    for c in config:
        gen_file(c)

def del_table(name):
    sql = 'drop table if exists '+name
    print sql
    db.execute(sql)
def create_table(name,data):
    tmp = []
    for v in data:
        tmp.append('%s varchar(200)'%v['name'])
    sql = 'create table %s (id int not null auto_increment primary key,%s)' % (name,','.join(tmp))
    print sql
    db.execute(sql)
    print 'table %s is created' % (name)
def init_database(config):

    for c in config:
        name = c['name']
        del_table(name)
        create_table(name,c['data'])

if __name__ == '__main__':
    config = []
    for page in page_config['menu']:
        if 'sub' in page:
            for s in page['sub']:
                config.append(s)
        else:
            config.append(page)
    print config
    if len(sys.argv)>1 and sys.argv[1]=='init':
        init_database(config)
        db.execute('insert into user (username,password) values ("51reboot","51reboot")')
    gen_config(config)