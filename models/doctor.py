from odoo import models,fields

class HospitalDoctor(models.Model):
   _name='hospital.doctor'
   _description='Hospital Doctors'
   

   name=fields.Char(string='Name',required=True)
   doctor_id=fields.Char('Id',copy=False)
   gender=fields.Selection([('male','male'),('female','female')],string='gender')
   specialization=fields.Char('specialization')
   appointments=fields.One2many('hospital.appointment','doctor_id',string='appointments')
   appointment_count_dector=fields.Integer(string='appointment count',compute="_compute_appointment_count_dector")
   state=fields.Selection([
      ('draft','Draft'),
      ('in_consultation','In_Consultation'),
      ('done','Done'),
      ('cancelled','Cancelled'),
   ],string='state',required=True,default='draft')

   def _compute_appointment_count_dector(self):
      self.appointment_count_dector = self.env['hospital.appointment'].search_count([('doctor_id', '=', self.id)])
