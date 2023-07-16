{
    'name': 'sehha management',
    'version': '1.0',
    'summary': 'Track leads and close opportunities',
    'description': "",
    'category': 'Sehha Management',
    'depends': [
        'project','sale','crm'
    ],
    'data': [
        

        'views/sale_order_template_views.xml',
        
        "data/custom_email.xml",
        'views/project_views.xml',

    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False
}