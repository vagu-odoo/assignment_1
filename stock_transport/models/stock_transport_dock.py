from odoo import fields,models

class TransportDock(models.Model):
    _name = "stock.transport.dock"
    _description = "Stock Transport Dock description"

    name = fields.Char()