from odoo import models, fields, api
import logging
from datetime import date
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class Lead(models.Model):

    _inherit = 'crm.lead'

    targeted_period = fields.Many2one(
        'lead.targeted.period',

        string='Targeted Period'
    )

    targeting_date = fields.Datetime('Targeting Date', copy=False)
    sales_team_leader = fields.Integer(string='leader', compute='_compute_sales_leader',store=True)

    @api.depends('team_id','user_id')
    def _compute_sales_leader(self):
        for lead in self:
            team = self.env['crm.team'].search([
                ('id', '=', lead.team_id.id),
                
                
            ])
            # _logger.info('lengthdhhhhh is '+str(len(team.user_id.name)))
            if len(team):
                
                lead.sales_team_leader= team.user_id.id
            else:
                lead.sales_team_leader= 0
    # @api.model
    # def _default_type(self):
    #     _logger.info('xoxoxoxoffxo'+self.type)
    #     # return True

    #     for record in self:
    #         _logger.info('userid===*'+str(record.team_id))


        
            
    #     return True
        # for record in self:

        #     if record.env.uid == record.team_id.user_id.id:
        #         _logger.info('x/x/xx/x/xx/***leader')
        #         if record.env['res.users'].has_group('crm.group_use_lead'):
        #             return 'lead'
        #         else:
        #             return 'opportunity'
        #     else:
        #         _logger.info('x/x/fxx/xp/xx/***not leader   '+str(record.env.uid))
        #         _logger.info(record.team_id.user_id)
        #         return 'new'


    type = fields.Selection([('new','New'),
        ('lead', 'Lead'), ('opportunity', 'Opportunity')], tracking=15, index=True,default=False
        
        )

    # trigger = fields.Boolean('Trigger')
    
    # @api.depends('team_id','user_id')
    # def _default_type(self):
    #     _logger.info('xoxoxoxoffrdfwddfxo')
    #     # return True

    #     for record in self:

    #         if record.env.uid == record.team_id.user_id.id:
    #             _logger.info('a leader')
    #             if record.env['res.users'].has_group('crm.group_use_lead'):
    #                 record.type = 'lead'
    #             else:
    #                 record.type = 'opportunity'
    #         else:
    #             _logger.info('not leader')
    #             # _logger.info(record.team_id.user_id)
    #             record.type = 'new'


    @api.model
    def create(self,vals):

        team = self.env['crm.team'].browse(vals['team_id'])
        team_lead_id = team.user_id.id
        _logger.info('/x/xx/xxx/xxxx/'+str(self.env.uid))
        
        if self.env.uid == team_lead_id:
            _logger.info('a x leader')
            if self.env['res.users'].has_group('crm.group_use_lead'):
                vals['type']= 'lead'
            else:
                vals['type']= 'opportunity'
        else:
            vals['type']= 'new'
            _logger.info('not x leader')
            # _logger.info(record.team_id.user_id)




        # for offer in offers:
        #     if  offer.price > vals['price']:
        #         raise UserError('An offer with higher price already existed !')

        # property.state = 'offer_received'
        return super().create(vals)
    
    def do_it(self):
        for record in self:
            if self.env.uid != record.team_id.user_id.id:
                raise UserError('Only the sales team leader can confirm leads')
            else:
                record.type = 'lead'



            
            _logger.info('/x/xx/xcxxxjust clicked'+str(record.type))
        return True
    