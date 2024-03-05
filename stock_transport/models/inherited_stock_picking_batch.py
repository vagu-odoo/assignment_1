from odoo import api,models,fields
class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("stock.transport.dock", string="Dock")
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category", string="Vehicle Category")

    batch_weight = fields.Float(compute="_compute_batch_weight_volume" ,store=True)
    batch_volume = fields.Float(compute="_compute_batch_weight_volume" ,store=True)
    volume_percentage = fields.Float(compute="_compute_batch_weight_volume")
    weight_percentage = fields.Float(compute="_compute_batch_weight_volume")
    lines = fields.Integer(compute="_compute_lines", store=True)
    transfers = fields.Integer(compute="_compute_transfers", store=True)

    @api.depends('move_line_ids')
    def _compute_lines(self):
        for batch in self:
            batch.lines = len(batch.move_line_ids)

    @api.depends('picking_ids')
    def _compute_transfers(self):
        for batch in self:
            batch.transfers = len(batch.picking_ids)        

    @api.depends('move_line_ids')
    def _compute_batch_weight_volume(self):
        for batch in self:
            for move in batch.move_line_ids:
                product = move.product_id
                if product:
                    wt = product.weight
                    vol = product.volume
                    # print("==================",wt)
                    batch.batch_weight += wt
                    batch.batch_volume += vol
                else:
                    batch.batch_weight += 0
                    batch.batch_volume +=0
            # print("max vol :",batch.vehicle_category_id.max_volume)
            # print("max wt :",batch.vehicle_category_id.max_weight)
            if batch.vehicle_category_id.max_volume != 0:
                batch.volume_percentage = (batch.batch_volume/batch.vehicle_category_id.max_volume)*100
            else:
                batch.volume_percentage = 0

            if batch.vehicle_category_id.max_weight != 0:   
                batch.weight_percentage = (batch.batch_weight/batch.vehicle_category_id.max_weight)*100
            else:
                batch.weight_percentage = 0

    @api.depends('batch_weight', 'batch_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name + str(record.batch_weight) + " kg / " + str(record.batch_volume) + " m3"