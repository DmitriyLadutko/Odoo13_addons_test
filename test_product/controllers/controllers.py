# -*- coding: utf-8 -*-
from odoo import http


class TestProduct(http.Controller):
    @http.route('/test_product/test_product/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/test_product/test_product/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('test_product.listing', {
            'root': '/test_product/test_product',
            'objects': http.request.env['test_product.test_product'].search([]),
        })

    @http.route('/test_product/test_product/objects/<model("test_product.test_product"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('test_product.object', {
            'object': obj
        })
