from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    email_cc = fields.Char(compute='_compute_email_cc', string='CC')

    @api.depends('order_line')
    def _compute_email_cc(self):
        
        for order in self:
            _logger.info('////////////'+str(order.team_id.user_id.email))
            # email_cc = []
            # for line in order.order_line:
            #     _logger.info('****************'+line.product_id.type)
            #     if not (line.product_id.type == 'service'):
            #         order.email_cc = ''
            #         return
            #     if line.product_id.project_template_id.user_id.email:
            #         email_cc.append(line.product_id.project_template_id.user_id.email)
            order.email_cc = order.team_id.user_id.email
