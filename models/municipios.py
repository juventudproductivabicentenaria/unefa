# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class municipios(osv.osv):
    _name='unefa.municipios'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre del Municipios',size=80,required=True,help='Nombre del municipio a registrar'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
        'estado_id':fields.many2one('unefa.estados','Estado')
  
    }
    
    _defaults={
        'active':True,
    }
