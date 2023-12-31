{
    'name' : 'Hospital Management',
    'category':'Hospital/appointment',
    'summary': "Hospital Management App",
    'author': "Odoo",

    'application': True,
    'installable':True,

    'data':[
     'security/security.xml',
     'security/ir.model.access.csv',
     'wizard/create_appointment_view.xml',
     'wizard/patient_report_view.xml',
     'views/doctor.xml',
     'views/appointment.xml',
     'views/patient.xml',
     'views/department.xml',
     'views/menu.xml',
     'report/patient_report.xml',
     'report/doctor_report.xml',
     'report/report.xml'
     
    ]
}