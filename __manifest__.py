{
    'name' : 'Hospital Management',
    'summary': "Hospital Management App",
    'author': "Odoo",

    'application': True,
    'installable':True,

    'data':[
     'security/ir.model.access.csv',
     'views/doctor.xml',
     'views/appointment.xml',
     'views/patient.xml',
     'views/department.xml',
     'views/menu.xml'
     
    ]
}