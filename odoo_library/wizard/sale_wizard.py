#-*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleWizard(models.TransientModel):
    _name='library.sale.wizard'
    _description = 'Wizard: Quick Sale Orders for Reservation Members'
    
    def _default_reservation(self):
        return self.env['library.reservation'].browse(self._context.get('active_id'))
    
    reservation_id = fields.Many2one(comodel_name='library.reservation',
                                    string='Reservation',
                                    required=True,
                                    default=_default_reservation)
    
    reservation_member_ids = fields.Many2many(comodel_name='res.partner',
                                             string='Members in current reservation',
                                             related='reservation_id.member_ids',
                                             help='These are the members currently reserve books')
    member_ids=fields.Many2many(comodel_name='res.partner',
                               string='Members for Sales Order')
    
    def create_sale_orders(self):
        reservation_product_id=self.env['product.product'].search([('is_reservation_product','=' , True)], limit=1)
        if reservation_product_id:
            for member in self.member_ids:
                order_id=self.env['sale.order'].create({
                    'partner_id':member_id,
                    'reservation_id':self.session.id,
                    'order_line':[(0,0, {'product_id': reservation_product_id.id,'price_unit': self.reservation_id.total_price})]
                })
        