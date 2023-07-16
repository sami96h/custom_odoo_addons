from odoo import api,fields, models

class Customer(models.Model):
    _inherit = 'res.partner'

    sector_id = fields.Many2one('res.partner.sector')

    