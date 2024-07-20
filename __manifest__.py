{
    'name' : "App One",
    'author': "Ahmed Qerba",
    'category': '',
    'version': "16.0.0.1.0",
    'depends': ['base','sale_management','mail'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_views.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order.xml',
        'views/property_history.xml',
        'wizard/change_state_wizard_view.xml',
        'data/sequence.xml',
        'reports/property_report.xml',
    ],
    'assets':{
        'web.assets_backend' : ['app_one/static/src/css/property.css']
    },
    'application': True,
}


