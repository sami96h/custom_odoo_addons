from odoo import api,fields, models
from datetime import datetime, timedelta
import logging
from odoo.exceptions import UserError, AccessError


_logger = logging.getLogger(__name__)

class Sector(models.Model):
    
    _name = "res.partner.sector"

    name =  fields.Char('Sector')

    
