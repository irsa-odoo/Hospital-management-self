from odoo import models, fields

class HospitalDepartment(models.Model):
	_name='hospital.department'
	_description='Hospital department'

	name=fields.Char(string="Department name",required=True)
	description=fields.Char(string="Department details")
	



	