from odoo import fields, models

class EagleEstateRoom(models.Model):
    _name = "eagle.estate.property.room"
    _description = "Eagle Estate Property Room"

    type = fields.Selection([
        ("garage", "Garage"),
        ("living", "Living"),
        ("dining", "Dining"),
        ("bathroom", "Bathroom"),
        ("bedroom", "Bedroom"),
        ("other", "Other")
    ])

    area = fields.Float("Area (sqft)")
    property_id = fields.Many2one("eagle.estate.property")
