from odoo import api,fields, models
import logging
_logger = logging.getLogger(__name__)

class Pricelist(models.Model):
    _inherit = 'product.pricelist'


    def _get_applicable_rules_domain(self, products, date, **kwargs):
        _logger.info('x/x/fddgffgdchccffddfd')
        _logger.info(products.name)
        _logger.info(self._context)
        

        _logger.info(self.env.context)
        # active_id = self.env.context.get('active_id')
        customer_id = self.env.context['partner_id']
        customer = self.env['res.partner'].search([('id', '=', customer_id)])
            # Do something with the active_id
        # for s in self.env.context:

        _logger.info(customer.sector_id)
                
        

        array =super()._get_applicable_rules_domain(products, date, **kwargs)
        array.extend(['|',('customer_sector', '=', False), ('customer_sector', 'in', customer.sector_id.ids)])
        # # print('/xx/xx/xx/xx/xx/xx/xx')
        # for ele in array:
        #     _logger.info('x/x/testttt'+str(ele))
        return array
        


