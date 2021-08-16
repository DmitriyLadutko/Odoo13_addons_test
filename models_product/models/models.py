# -*- coding: utf-8 -*-

from odoo import models, fields, api


class models_product(models.Model):
    _name = 'models_product.models_product'
    _description = 'models_product.models_product'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
