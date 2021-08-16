# -*- coding: utf-8 -*-
from odoo import http


class ModelsProduct(http.Controller):
    @http.route('/models_product/models_product/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/models_product/models_product/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('models_product.listing', {
            'root': '/models_product/models_product',
            'objects': http.request.env['models_product.models_product'].search([]),
        })

    @http.route('/models_product/models_product/objects/<model("models_product.models_product"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('models_product.object', {
            'object': obj
        })
