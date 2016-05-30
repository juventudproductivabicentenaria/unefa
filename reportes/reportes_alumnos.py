# -*- encoding: utf-8 -*-

from openerp.report import report_sxw
from openerp.osv import osv


class reportes_estudiantes(report_sxw.rml_parse):
    def __init__(self,cr,uid,name,context):
        super(reportes_estudiantes,self).__init__(cr,uid,name,context)
        self.localcontext.update({
            'get_data_estudiantes':self.get_data_estudiantes
            })
    
    def get_data_estudiantes(self,id_wizard):
        wizard_obj=self.pool.get('unefa.reporte_alumnos_wizard')
        wizard_data=wizard_obj.browse(self.cr,self.uid,id_wizard)
        return wizard_data.alumnos_ids
class reporte_alumnos(osv.AbstractModel):
    _name="report.unefa.estudiante_unefa"
    _inherit="report.abstract_report"
    _template="unefa.estudiante_unefa"
    _wrapped_report_class=reportes_estudiantes
    
class reporte_alumnos_wizard(osv.AbstractModel):
    _name="report.unefa.estudiante_unefa_wizard_qweb"
    _inherit="report.abstract_report"
    _template="unefa.estudiante_unefa_wizard_qweb"
    _wrapped_report_class=reportes_estudiantes
    
    
