# -*- coding: utf-8 -*-


from openerp.osv import fields, osv

class reporte_alumnos_wizard(osv.TransientModel):
    """
        Esta clase es para generar los reporte de los alumnos
    """
    _name="unefa.reporte_alumnos_wizard"
    _description="Reportes de alumnos con un wizard"
    
    _columns={
        'reporte_nombre':fields.char('Nombre del Reporte',required=True),
        'alumnos_ids':fields.many2many(
                            'unefa.estudiantes',
                            'unefa_estudiante_reporte_wizard_rel',
                            'estudiante_id',
                            'reporte_id',
                            'Estudiantes')
        }

    def reporte_alumnnos_pdf(self,cr,uid,ids,context=None):
        reporte_data=self.browse(cr,uid,ids,context=context)
        data={'titulo':reporte_data.reporte_nombre,'ids':ids}
        return self.pool['report'].get_action(cr,uid,[],'unefa.estudiante_unefa_wizard_qweb',data=data,context=context)
        
