#-*- coding: utf-8 -*-

{
    'name': 'Odoo Library',
    'Summary':"""Library app to manage organizational books""",
    'description':"""
        Library module to manage learning and Training:
        - Course
        - Sessions
        - Attendees
    """,
    'author':'Elabs',
    'website':'https://www.elabs.de',
    
    'category': 'Learning and Training',
    'version':'0.1',
    
    'depends':['sale','website','sale_subscription',],
    
    'data':[
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/library_menuitems.xml',
        'views/reservation_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'reports/reservation_report_templates.xml',
        'views/library_web_templates.xml',
        'views/sale_subscription_view_inherit.xml',
    ],
    
    'demo': [
        'demo/library_demo.xml',
    ],
}