import logging

from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class EagleProperty(models.Model):
    _name = "eagle.estate.property"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "name"
    _order = "date DESC, id"

    name = fields.Char("Title", required=True)
    date = fields.Char("Date", required=True, default=fields.Date.today)
    surface_area = fields.Integer("Area (sq ft.)")
    room_ids = fields.One2many("eagle.estate.property.room", "property_id")
    tag_ids = fields.Many2many("eagle.estate.tag")
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'eagle_estate_property_attachment_rel',
        'eagle_estate_property_id',
        'attachment_id',
        string='Attachments'
    )

    @api.model_create_multi
    def create(self, vals):
        # Call the original create method
        record = super(EagleProperty, self).create(vals)
        _logger.info("Creating record %s", vals)

        return record
