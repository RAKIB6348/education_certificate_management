# -*- coding: utf-8 -*-
{
    'name': "Education Certificate Management",
    'version': '17.0.1.0.0',
    'category': 'Education',
    'summary': 'Generate Professional Certificates for Students, Faculty and Employees',
    'description': """
        Complete Certificate Management System for Education.
        Features:
        - Multiple Certificate Templates with Background
        - QR Code Support
        - Digital Signature Integration (from school_idcard_signature module)
        - Certificate for Student (education.student), Faculty (education.faculty) & Employee
        - Auto Certificate Number
        - Professional PDF Report
    """,
    'author': "Your Name",
    'website': "https://www.yourcompany.com",

    'depends': [
        'base',
        'hr',
        'education_core',

    ],

    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/certificate_menu.xml',
        'views/certificate_type_views.xml',
        'views/certificate_template_views.xml',
        'views/certificate_issued_views.xml',
        'reports/certificate_report.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}