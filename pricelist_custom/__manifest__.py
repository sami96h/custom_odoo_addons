{
    'name': 'pricelist custom',
    'version': '1.0',
    'summary': 'Track leads and close opportunities',
    'description': "",
    'category': 'Sehha Management',
    'depends': [
        'project','sale','crm'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/pricelist_item_view.xml',
        'views/customer_views.xml',
        
        
        'views/product_template_views.xml',
        
        
        
        

    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False
}