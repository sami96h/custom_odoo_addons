from odoo import api,fields, models
from odoo.exceptions import UserError, ValidationError

class Location(models.Model):
    _inherit = 'hr.work.location'

    employee_ids = fields.One2many('hr.employee','work_location_id')
    location_assignment_ids = fields.One2many('hr.employee.location.assignment','location_id')
    capacity = fields.Integer(string='Capacity')
    assignments_count = fields.Integer(compute='_compute_assignments_count', string='Employees',store=True)
    

    @api.constrains('capacity')
    def check_capacity(self):
        for location in self:
            if location.capacity < 0:
                raise UserError("Location capacity cannot be negative.")
            
    @api.depends('location_assignment_ids')
    def _compute_assignments_count(self):
        for location in self:
            assignments = self.env['hr.employee.location.assignment'].search([
                ('location_id', '=', location.id),
                ('start_date', '<=', fields.Date.today()),
                ('end_date', '>=', fields.Date.today())
            ])
            location.assignments_count = len(assignments)