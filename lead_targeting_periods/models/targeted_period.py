from odoo import models, fields, api
import logging
from datetime import date

_logger = logging.getLogger(__name__)

class TargetedPeriod(models.Model):
    _name = 'lead.targeted.period'
    current_year = date.today().year
    year_selection = [(str(year), str(year)) for year in range(current_year, current_year + 11)]
    name = fields.Char(compute='_compute_name')
    year = fields.Selection(year_selection, string='Year')


    @api.depends('quarter','year')
    def _compute_name(self):
        for period in self:

            quarter_label = dict(period._fields['quarter'].selection).get(period.quarter)
            period.name = quarter_label + '/' + period.year

    quarter = fields.Selection([
        ('1', 'Q1'),
        ('2', 'Q2'),
        ('3', 'Q3'),
        ('4', 'Q4')
    ], string="Quarter")

    lead_ids = fields.One2many(
        'crm.lead',
        'targeted_period',
        string='leeds'
    )
    
    _sql_constraints = [
        ('quarter_year_unique', 'unique(quarter, year)', 'The combination of quarter and year must be unique!')
    ]
