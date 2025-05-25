from odoo import fields, models, api


class EagleEstateTag(models.Model):
    _name = 'eagle.estate.tag'
    _description = 'Eagle Estate Tag'

    name = fields.Char()
    color = fields.Integer('Color')
