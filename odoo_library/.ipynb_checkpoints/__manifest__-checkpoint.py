#-*- coding: utf-8 -*-
#'demo/library_demo.xml',
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
    
    'depends':['base'],
    
    'data':[
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/library_menuitems.xml',
    ],
    
    'demo': [
        'demo/library_demo.xml',
    ],
}