from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'eagle.estate.tag'
    _description = 'Eagle Estate Tag'

    name = fields.Char()
    color = fields.Integer('Color')
