# *- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Reservation(models.Model):
    _name = 'library.reservation'
    _description = 'Reservation info'
    
    book_id=fields.Many2one(comodel_name='library.book',string='Book', ondelete='cascade', required=True)
    
    name=fields.Char(string='Title',related='book_id.name')
    
    reservation_operator_id = fields.Many2one(comodel_name='res.partner',string='Reservation Operator')
    member_ids = fields.Many2many(comodel_name='res.partner',string='Reservation Member')
    
    
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    
    duration = fields.Integer(string='Reservation Days', default=1)
    
    end_date = fields.Date(string='End Date',compute='_compute_end_date',inverse='_inverse_end_date',store=True)
    
    
    
    
    total_price = fields.Float(string='Total Price',
                              related='book_id',total_price)
    
    
    @api.depends('start_date','duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
            else:
                duration = timedelta(days=record.duration)
                record.end_date = record.start_date + duration
                
    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration = (record.end_date - record.start_date).days + 1
            else:
                continue
