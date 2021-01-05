# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    
    _name = 'library.book'
    _description = 'Book Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level',
                            selection=[('beginner','Beginner'),
                                       ('intermediate','Intermediate'),
                                       ('advanced','Advanced'),
                                       ],copy=False)
    active = fields.Boolean(string='Active',default=True) 