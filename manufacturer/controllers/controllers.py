# -*- coding: utf-8 -*-
from odoo import http


class Manufacturer(http.Controller):
    @http.route('/manufacturer/manufacturer/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/manufacturer/manufacturer/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('manufacturer.listing', {
            'root': '/manufacturer/manufacturer',
            'objects': http.request.env['manufacturer.manufacturer'].search([]),
        })

    @http.route('/manufacturer/manufacturer/objects/<model("manufacturer.manufacturer"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('manufacturer.object', {
            'object': obj
        })
