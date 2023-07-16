{
    'name': 'lead targeting periods',
    'version': '1.0',
    'summary': 'Track leads and close opportunities',
    'description': "",
    'category': 'Sehha Management',
    'depends': [
        'sale_crm'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/lead_form_views.xml',
        'views/targeted_period_view.xml',

    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False
}