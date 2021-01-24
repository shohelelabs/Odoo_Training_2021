#-*- coding: utf-8 -*-

from odoo import http


class Library(http.Controller):
    @http.route('/library/',auth='public',website=True)
    def index(self, **kw):
        return "Hello World"
    
    @http.route('/library/books/',auth='public',website=True)
    def books(self, **kw):
        books = http.request.env['library.book'].serch([])
        return http.request.render('odoo_library.book_website',{'books': books,})
    
    @http.route('/library/<model("library.reservation"):reservation>/',auth='public',website=True)
    def reservation(self,reservation):
        return http.request.render('odoo_library.reservation_website',{'reservation':reservation,})