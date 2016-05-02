# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class familiares_contactos(osv.osv):
    _name='unefa.familiares_contactos'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre',size=80,required=True,help='Aquí se coloca el nombre del estudiante'),
        'apellido':fields.char('Apellido',size=80,required=True,help='Aquí se coloca el apellido del estudiante'),
        'cedula':fields.integer('Cédula',size=10,required=True,help='Aquí se coloca el Cédula del estudiante'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
        'estado_id':fields.many2one('unefa.estados','Nombre del Estado',ondelete="restrict"),
        'municipio_id':fields.many2one('unefa.municipios','Nombre del Municipio',ondelete="restrict"),
        'parroquia_id':fields.many2one('unefa.parroquias','Nombre de la Parroquia',ondelete="restrict"),
        'sector':fields.char('Sector',size=100),
        'calle':fields.char('Calle/Avenida',size=100),
        'estudiante_id':fields.many2one('unefa.estudiantes','Estudiante')
        
    }
    
    _defaults={
        'active':True,
    }
    
    def pulsar_estado(self,cr,ids,context=None):
		return {'value':{'municipio_id':'','parroquia_id':''}}
		
    def pulsar_municipio(self,cr,ids,context=None):
		return {'value':{'parroquia_id':''}}
    
