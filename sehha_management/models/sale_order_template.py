from odoo import api,fields, models

class Project(models.Model):
    _inherit = 'sale.order.template'

    requirements = fields.Html(string="Functional Requirements", translate=True)
    non_functional_requirements = fields.Html(string="Non Functional Requirements", translate=True)

