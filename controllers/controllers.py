# -*- coding: utf-8 -*-
# from odoo import http


# class EducationCertificateManagement(http.Controller):
#     @http.route('/education_certificate_management/education_certificate_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/education_certificate_management/education_certificate_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('education_certificate_management.listing', {
#             'root': '/education_certificate_management/education_certificate_management',
#             'objects': http.request.env['education_certificate_management.education_certificate_management'].search([]),
#         })

#     @http.route('/education_certificate_management/education_certificate_management/objects/<model("education_certificate_management.education_certificate_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('education_certificate_management.object', {
#             'object': obj
#         })

