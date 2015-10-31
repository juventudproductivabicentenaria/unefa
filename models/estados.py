# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class estados(osv.osv):
    _name='unefa.estados'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre del Estado',size=80,required=True,help='Nombre del estado a registrar'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
    }
    
    _defaults={
        'active':True,
    }
