# *- coding: utf-8 -*-

from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'library.reservation'
    _description = 'Reservation info'
    
    book_id=fields.Many2one(comodel_name='library.book',string='Book', ondelete='cascade', required=True)
    
    name=fields.Char(string='Title',related='book_id.name')
    reservation_operator_id = fields.Many2one(comodel_name='res.partner',string='Reservation Operator')
    member_ids = fields.Many2many(comodel_name='res.partner',string='Reservation Member')
