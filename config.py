# coding=utf-8


# 数据库配置


db_config = {
	'host':'localhost',
	'user':'root',
	'passwd':"123456",
	'db':'cmdb'
}


page_config = {
    "brand_name":'51Reboot',
    'title':'hello reboot',
    "favicon":'https://pic1.zhimg.com/6d660dd4156c64bfad13ff97d79c2f98_l.jpg',
    "menu":[
        {
            # user配置最好不要修改，是和登陆认证相关的，直接在下面加配置即可
            "name": 'user',
            "title": '用户管理',
            "data": [{
                "name": 'username',
                "title": '用户名'
            },{
                "name":'password',
                "title":'密码'
            }]
        },
        {
            # user配置最好不要修改，是和登陆认证相关的，直接在下面加配置即可
            "name": 'test',
            "title": '测试',
            "data": [{
                "name": 'username',
                "title": '用户名'
            },{
                "name":'password',
                "title":'密码',
                "empty":"yes"

            }]
        },
        {
            "name":'caninet',
            "title":'机柜',
            "data":[{
                "name":"name",
                "title":'机柜名'
            }]
        },
        {
            "name":"host",
            "title":"服务器",
            "data":[{
                "name":"caninet",
                "title":'机柜',
                "type":'select',
                "select_type":'caninet'
            },{
                "name":"hostname",
                "title":'主机名'
            },{
                'name':'asset_no',
                'title':'资产号'
            },{
                "name":'end_time',
                "title":"过期日期",
                "type":'date'
            },{
                "name":'ups',
                "title":'是否开启',
                "type":'select',
                "value":{0:'开启',1:'关闭'}
            }]
        }
    ]
}





# ,{
#         "name": 'host',
#         "title": '服务器',
#         "data": [{
#             "name": 'cabinet',
#             "title": '机柜'
#         },{
#             "name":'hostname',
#             "title":'主机名'
#         }]
#     },{
#         "title": '业务',
#         "sub":[
#             {
#                 'name': 'product',
#                 'title': '业务线',
#                 'data': [{
#                     'name': 'service_name',
#                     'title': '服务名'
#                 },{
#                     'name':'module_letter',
#                     'title':'模块简称'
#                 },{
#                     'name':'dev_interface',
#                     'title':'开发者'
#                 },{
#                     'name':'op_interface',
#                     'title':'运维接口人'
#                 }]
#             },
#             {
#                 'name': 'raidtype',
#                 'title': 'Raid厂商',
#                 'data': [{
#                     'name': 'name',
#                     'title': 'Raid厂商'
#                 }]
#             }


#         ]
#     }