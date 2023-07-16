from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):

    _inherit = 'product.template'

    target_sectors = fields.Many2many('res.partner.sector')

    status = fields.Selection(
        selection=[('introduction', 'Introduction'),
                   ('growth', 'Growth'),
                   ('declined', 'Declined'),
                   ('mature', 'Mature')],
        string='Status'
    )