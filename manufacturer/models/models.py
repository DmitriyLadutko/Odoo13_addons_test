# -*- coding: utf-8 -*-

from odoo import models, fields, api


class manufacturer(models.Model):
    _name = 'manufacturer.manufacturer'
    _description = 'manufacturer.manufacturer'
    models = fields.Many2many('models_product.models_product')

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
