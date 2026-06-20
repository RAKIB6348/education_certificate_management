# -*- coding: utf-8 -*-
from odoo import models, fields


class CertificateType(models.Model):
    _name = 'certificate.type'
    _description = 'Certificate Type'
    _order = 'sequence, name'

    name = fields.Char('Certificate Type', required=True)
    sequence = fields.Integer('Sequence', default=10)
    code = fields.Char('Code', size=16)
    description = fields.Text('Description')
    active = fields.Boolean('Active', default=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Certificate type name must be unique!'),
    ]