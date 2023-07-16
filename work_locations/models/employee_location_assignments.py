from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class EmployeeLocationAssignment(models.Model):
    _name = 'hr.employee.location.assignment'
    _description = 'Employee Location Assignment'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    location_id = fields.Many2one('hr.work.location', string='Location', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    @api.constrains('employee_id', 'start_date', 'end_date')
    def check_assignment_constraints(self):
        for assignment in self:
            # Check for overlapping assignments
            domain = [
                ('employee_id', '=', assignment.employee_id.id),
                ('start_date', '<', assignment.end_date),
                ('end_date', '>', assignment.start_date),
                ('id', '!=', assignment.id),
            ]
            overlapping_assignments = self.search_count(domain)
            if overlapping_assignments > 0:
                raise UserError("Employee already has an overlapping assignment.")

            # Check if location is at full capacity
            if assignment.location_id.capacity > 0:
                domain = [
                    ('location_id', '=', assignment.location_id.id),
                    ('start_date', '<', assignment.end_date),
                    ('end_date', '>', assignment.start_date),
                    ('id', '!=', assignment.id),
                ]
                overlapping_assignments = self.search_count(domain)
                if overlapping_assignments >= assignment.location_id.capacity:
                    raise UserError("Location is already at full capacity for the specified period.")

