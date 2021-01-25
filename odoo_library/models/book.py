# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Book(models.Model):
    
    _name = 'library.book'
    _description = 'Book Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level',
                            selection=[('beginner','Beginner'),
                                       ('intermediate','Intermediate'),
                                       ('advanced','Advanced')
                                       ],copy=False)
    
    active = fields.Boolean(string='Active',default=True) 
    
    base_price = fields.Float(string='Base Price', default=0.00)
    
    additional_fee = fields.Float(string='Additional Fee', default=10.00)
    
    total_price = fields.Float(string='Total Price', readonly=True)
    
    reservation_ids = fields.One2many(comodel_name='library.reservation',inverse_name='book_id',string='Reservations')
    
    @api.onchange('base_price','additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError(_('Base Price cannot be set as Negative.'))
        
        
        self.total_price = self.base_price + self.additional_fee
        
        
    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError(_('Addiotional Fees cannot be less than 10.00: %s' % record.additional_fee))