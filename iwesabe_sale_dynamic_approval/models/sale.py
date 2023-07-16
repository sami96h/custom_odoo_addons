# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    can_confirm_order = fields.Boolean('', compute="_can_confirm_order")
    sale_approver_line = fields.One2many('sale.approver', 'sale_id', copy=False)
    is_it = fields.Boolean('check',default=False)
    approver_ids=fields.Boolean('', compute="_compute_ids",readonly=False)


    @api.depends_context('uid')
    @api.depends('team_id','team_id.sale_approver_line',
                'team_id.sale_approver_line.sequence',
                'state','sale_approver_line',
                'sale_approver_line.approved_order')


    def _compute_ids(self):
        _logger.info('nononomomomonxxxononomomo')
        for record in self:
            
            isIt = False
            for line in record.sale_approver_line:
                

                
                # filtered_lines = line.search([('user_id', '=', self.env.uid)])
                if line.user_id.id == self.env.uid and not line.approved_order:

                    _logger.info('nooxoivce'+str(line.user_id.name))
                    isIt = True
                    # _logger.info('/ooooxxxoooo/'+str(line.user_id.id)+str(line.approved_order)+str(self.env.uid))
            record.approver_ids = isIt
            record.is_it=isIt


            # ids = record.sale_approver_line.mapped('user_id.name')
            # idss = record.sale_approver_line.mapped('id')
            # _logger.info('/xxx/xox/xxx/'+str(ids)+str(idss))
        #     _logger.info('/*****/'+str(ids))
        #     record.approver_ids='/xxxxxxx/'
        




    @api.depends_context('uid')
    @api.depends('team_id','team_id.sale_approver_line',
                'team_id.sale_approver_line.sequence',
                'state','sale_approver_line',
                'sale_approver_line.approved_order')
    def _can_confirm_order(self):
        for record in self:
            can_confirm_order = True
            if record.team_id.sale_approver_line and record.state in ['draft','sent']:
                line_vals = []
                for line in record.team_id.sale_approver_line:
                    condition = record.sale_approver_line.filtered(lambda x:x.user_id == line.user_id)
                    if not condition:
                        line_vals.append({
                            'sequence':line.sequence,
                            'user_id':line.user_id.id,
                        })
                    elif condition.filtered(lambda x:not x.approved_order):
                        condition.update({
                            'sequence':line.sequence,
                        })
                if line_vals:
                    record.sale_approver_line = [(0,0,val) for val in line_vals]
            sale_approver_line = record.sale_approver_line.filtered(lambda x:not x.approved_order)
            if sale_approver_line:
                if self.env.user == sale_approver_line[0].user_id:
                    can_confirm_order = True
                else:
                    can_confirm_order = False
            record.can_confirm_order = can_confirm_order
    
    def action_confirm(self):
        result = False
        if not self.sale_approver_line:
            result = super().action_confirm()
        elif self.sale_approver_line:
            UserNotMatched = self.sale_approver_line.filtered(lambda x:x.user_id != self.env.user)
            if not UserNotMatched:
                raise UserError(_("Sorry!!.. You're not allowed to confirm this order."))
            sale_approver_line = self.sale_approver_line.filtered(lambda x:x.user_id == self.env.user and not x.approved_order)
            if sale_approver_line:
                sale_approver_line.update({
                    'approved_order':True,
                })
                if all(sale_approver_line.approved_order for sale_approver_line in self.sale_approver_line):
                    result = super().action_confirm()
                else:
                    notification = {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'title': ('Notify'),
                            'message': 'Approved Order successfully',
                            'type':'success',
                            'sticky': True,
                        },
                    }
                    result = notification
        self._can_confirm_order()
        return result
        



                    



