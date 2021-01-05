#-*- coding: utf-8 -*-
{
    'name': 'Odoo Library',
    'Summary':"""Academy app to manage Training""",
    'description':"""
        Academy module to manage Training:
        - Course
        - Sessions
        - Attendees
    """,
    'author':'Elabs',
    'website':'https://www.elabs.de',
    'category': 'Training',
    'version':'0.1',
    'depends':['base'],
    
    'data':[
        'views/book_views.xml'
    ],
    
    'demo': [
        'demo/library_demo.xml'
    ],
}