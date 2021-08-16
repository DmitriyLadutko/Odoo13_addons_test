# -*- coding: utf-8 -*-

from odoo import models, fields, api


class test_product(models.Model):
    _name = 'test_product.test_product'
    _description = 'test_product.test_product'
    manufacturer = fields.Many2many('manufacturer.manufacturer')

    name = fields.Char()
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
