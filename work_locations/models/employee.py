from odoo import api,fields, models

class Project(models.Model):
    _inherit = 'hr.employee'

    location_assignment_ids = fields.One2many('hr.employee.location.assignment','employee_id')
    employee_count = fields.Integer(string='Employee Count', compute='_compute_employee_count',store=True)
    # location_id = fields.Many2one('hr.work.location', string='Location', required=True)

    @api.depends('work_location_id')
    def _compute_employee_count(self):
        for employee in self:
            employee.employee_count = self.env['hr.employee'].search_count([('work_location_id', '=', employee.work_location_id.id)])