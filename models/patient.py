from odoo import models, fields, api
from datetime import date
import math

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
  

   @api.depends('birth_date')
   def _compute_age(self):
   	for rec in self:
   		d_now=date.today()
   		if rec.birth_date:
   			rec.age=d_now.year - rec.birth_date.year
   		else:
   			rec.age=0

   


   









   
