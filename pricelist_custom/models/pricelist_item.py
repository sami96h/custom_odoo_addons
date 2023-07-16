from odoo import api,fields, models

class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    customer_sector = fields.Many2one('res.partner.sector')


