from odoo import api,fields,models

class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(default=10.0)
    max_volume = fields.Float(default=10.0)

    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name + str(record.max_weight) + " kg / " + str(record.max_volume) + " m3"
            # name = f"{name}({record.max_weight}kg, {record.max_volume}m\u00B3)"