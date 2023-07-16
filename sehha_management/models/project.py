from odoo import api,fields, models

class Project(models.Model):
    _inherit = 'project.project'

    
    def attachment_tree_view(self):

        domain = ["&", ("res_model", "=", "project.project"), ("res_id", "in", self.ids)]

        return {
            "name": ("Attachments"),
            "domain": domain,
            "res_model": "ir.attachment",
            "type": "ir.actions.act_window",
            "view_id": False,
            "view_mode": "kanban,tree,form",
            "view_type": "form",
            "limit": 80,
            "context": "{{'default_res_model': '{}','default_res_id': {}}}".format(self._name, self.id),
        }

    def knowledge_tree_view(self):

        domain = [("parent_id.name", "=", self.name)]

        return {
                "name": ("Lessons Learned"),
                # "domain": domain,
                "res_model": "document.page",
                "type": "ir.actions.act_window",
                # "view_id": False,
                "view_mode": "tree,form",
                # "view_type": "tree",
        }


