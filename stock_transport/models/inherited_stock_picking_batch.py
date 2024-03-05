from odoo import api,models,fields
class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("stock.transport.dock", string="Dock")
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category", string="Vehicle Category")

    batch_weight = fields.Float(compute="_compute_batch_weight")

    @api.depends('move_line_ids')
    def _compute_batch_weight(self):
        for move in self.move_line_ids:
            product = move.product_id
            if product:
                wt = product.weight
                print("==================",wt)
                self.batch_weight += wt
            else:
                self.batch_weight += 0


