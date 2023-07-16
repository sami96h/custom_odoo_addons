{
    'name': 'work locations',
    'version': '1.0',
    'summary': 'Track leads and close opportunities',
    'description': "",
    'category': 'Sehha Management',
    'depends': [
        'project','hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_form_views.xml',
        'views/work_location_views.xml',

    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False
}