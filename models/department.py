from odoo import models, fields

class HospitalDepartment(models.Model):
	_name='hospital.department'
	_description='Hospital department'

	name=fields.Char(string="Department name",required=True)
	description=fields.Char(string="Department details")
	appointments=fields.One2many('hospital.appointment','appointment_id',string='appointments')
	doctor_id=fields.Many2one('hospital.doctor',string='doctor')

	
	



	