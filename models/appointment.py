from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
   _name = 'hospital.appointment'
   _description = 'Hospital Appointments'

   appointment_id=fields.Char(string='id',copy=False)
   patient_id=fields.Many2one('hospital.patient',string='patient',readonly=False)
   gender=fields.Selection([('male','male'),('female','female')],string='gender')
   appointment_date=fields.Date(string='appointment date' , default=date.today())
   booking_date=fields.Date(string='booking date',required=True)
   description=fields.Char(string='description')
   state=fields.Selection([
      ('draft','Draft'),
      ('in_consultation','In_Consultation'),
      ('done','Done'),
      ('cancelled','Cancelled'),
   ],string='state',required=True,default='draft')
   doctor_id=fields.Many2one('hospital.doctor',string='doctor')

   @api.constrains('appointment_date', 'booking_date')
   def _check_date_validation(self):
      for record in self:
         if record.booking_date < record.appointment_date:
            raise ValidationError('Booking date should not be previous date.')

   def action_cancel (self):
      self.state  ='cancelled'

   def action_in_consultation (self):
      self.state  ='in_consultation'

   def action_done(self):
   	self.state = 'done'


