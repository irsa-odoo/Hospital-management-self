from odoo import models, fields, api,_
 
class PatientReportWizard(models.TransientModel):
    _name = 'patient.report.wizard'
    _description= 'create report wizard'

    age=fields.Integer(string='age')
    gender = fields.Selection([('male', 'male'), ('female', 'female')], string='gender')

    def patient_reports_action(self):
        domain=[]
        if self.gender:
            domain=[('gender','=',self.gender)]
        if self.age:
            domain=[('age','=',self.age)]

        data={

            'kk':self.env['hospital.patient'].search(domain),
        }
        action = self.env.ref('hospital.patient_reports_action').report_action(self,data=data)
        return action
      
