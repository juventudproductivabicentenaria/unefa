# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class parroquias(osv.osv):
    _name='unefa.parroquias'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre de la Parroquias',size=80,required=True,help='Nombre de la parroquias a registrar'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
    }
    
    _defaults={
        'active':True,
    }
