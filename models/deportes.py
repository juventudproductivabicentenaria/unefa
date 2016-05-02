# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class deportes(osv.osv):
    _name='unefa.deportes'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre del deporte',size=80,required=True,help='Nombre del deporte a registrar'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
  
    }
    
    _defaults={
        'active':True,
    }
