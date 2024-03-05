from odoo import api,fields,models

class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Integer()
    max_volume = fields.Integer()

    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = str(record.max_weight) + " kg / " + str(record.max_volume) + " m3"