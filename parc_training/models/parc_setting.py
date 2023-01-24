# -*- coding: utf-8 -*-
from openerp import api, fields, models
from openerp.tools.translate import _

class parc(models.Model):
    _name = 'parc'
    name = fields.Char(string="Nom",required=True)
    detail=fields.Char(string="Detail")