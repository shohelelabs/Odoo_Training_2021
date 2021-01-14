#-*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    reservation_id = fields.Many2one(comodel_name='library.reservation',string='Related Reservation',ondelete='set null')
    
    reservation_operator_id=fields.Many2one(string='Reservation Operator', related='reservation_id.reservation_operator_id')
    
    member_ids= fields.Many2many(string='Members',related='reservation_id.member_ids')