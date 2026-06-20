# -*- coding: utf-8 -*-
from odoo import models, fields


class CertificateTemplate(models.Model):
    _name = 'certificate.template'
    _description = 'Certificate Template'
    _order = 'name'

    name = fields.Char('Template Name', required=True)
    background_image = fields.Image(
        string='Background Image',
        max_width=1200,
        max_height=850,
        help="Upload certificate background (Recommended size: 1200x850 px)"
    )
    certificate_type_id = fields.Many2one(
        'certificate.type',
        string='Default Certificate Type'
    )
    signatory_title = fields.Char(
        'Signatory Title',
        default="Principal",
        help="Example: Principal, Director, Dean, Head of Department"
    )
    is_active = fields.Boolean('Active', default=True)
    description = fields.Text('Description')

    # Optional: You can add header text, footer text, font color etc. later