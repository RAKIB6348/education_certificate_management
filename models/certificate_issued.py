from odoo import models, fields, api
import qrcode
import base64
from io import BytesIO


class CertificateIssued(models.Model):
    _name = 'certificate.issued'
    _description = 'Issued Certificate'
    _rec_name = 'certificate_number'
    _order = 'issue_date desc'

    certificate_number = fields.Char('Certificate No', readonly=True, copy=False,
                                     default=lambda self: self.env['ir.sequence'].next_by_code('certificate.issued'))

    name = fields.Char('Certificate Title', required=True)

    recipient_type = fields.Selection([
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('employee', 'Employee'),
    ], string="Recipient Type", required=True, default='student')

    student_id = fields.Many2one('education.student', string="Student")
    faculty_id = fields.Many2one('education.faculty', string="Faculty")
    employee_id = fields.Many2one('hr.employee', string="Employee")

    recipient_name = fields.Char('Recipient Name', compute='_compute_recipient_name', store=True)

    certificate_type_id = fields.Many2one('certificate.type', string="Certificate Type")
    template_id = fields.Many2one('certificate.template', string="Template", required=True)

    issue_date = fields.Date('Issue Date', default=fields.Date.today())
    expiry_date = fields.Date('Valid Until')
    description = fields.Html('Achievement / Reason')

    signatory_id = fields.Many2one(
        'hr.employee',
        string="Signatory",
        domain="[('signature_image', '!=', False)]",
        help="Person whose signature will appear"
    )

    qr_code = fields.Binary('QR Code', compute='_compute_qr_code', store=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('issued', 'Issued'),
        ('cancel', 'Cancelled')
    ], default='draft', string="Status", tracking=True)

    @api.depends('student_id', 'faculty_id', 'employee_id', 'recipient_type')
    def _compute_recipient_name(self):
        for rec in self:
            if rec.recipient_type == 'student' and rec.student_id:
                rec.recipient_name = rec.student_id.name
            elif rec.recipient_type == 'faculty' and rec.faculty_id:
                rec.recipient_name = rec.faculty_id.name
            elif rec.recipient_type == 'employee' and rec.employee_id:
                rec.recipient_name = rec.employee_id.name
            else:
                rec.recipient_name = False

    @api.depends('certificate_number')
    def _compute_qr_code(self):
        for rec in self:
            if rec.certificate_number:
                qr = qrcode.QRCode(version=1, box_size=10, border=4)
                qr.add_data(rec.certificate_number)
                qr.make(fit=True)
                img = qr.make_image(fill_color="#2C3E50", back_color="white")
                temp = BytesIO()
                img.save(temp, format="PNG")
                rec.qr_code = base64.b64encode(temp.getvalue())
            else:
                rec.qr_code = False

    def action_issue(self):
        self.write({'state': 'issued'})