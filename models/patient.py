from odoo import models, fields, api
from datetime import date
import math
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
   _name = 'hospital.patient'
   _description = "Hospital Patients"

   p_id=fields.Char(string='p_id',copy=False)
   name = fields.Char(string='name',required=True)
   age = fields.Integer(string='age',compute='_compute_age',readonly=False)
   gender=fields.Selection([('male','male'),('female','female')],string='gender')
   birth_date=fields.Date(string='date of birth')
   active=fields.Boolean(string='Active',default=True)
   appointments=fields.One2many('hospital.appointment','patient_id',string='appointments')
   appointment_count=fields.Integer(string='appointment count', compute='_compute_appointment_count')
  

   @api.depends('birth_date')
   def _compute_age(self):
   	for rec in self:
   		d_now=date.today()
   		if rec.birth_date:
   			rec.age=d_now.year - rec.birth_date.year
   		else:
   			rec.age=0

   @api.constrains('age')
   def _check_doctor_age(self):
      for record in self:
         if record.age <= 0:
            raise ValidationError('Age must be greater than 0')



   def _compute_appointment_count(self):
      for rec in self:
         if rec.id:
            rec.appointment_count = rec.env['hospital.appointment'].search_count([('p_id', '=', rec.id)])
         else:
            rec.appointment_count = 0


   









   
