# -*- encoding: utf-8 -*-

from openerp.report import report_sxw
from openerp.osv import osv


class reportes_estudiantes(report_sxw.rml_parse):
    def __init__(self,cr,uid,name,context):
        super(reportes_estudiantes,self).__init__(cr,uid,name,context)

class reporte_alumnos(osv.AbstractModel):
    _name="report.unefa.estudiante_unefa"
    _inherit="report.abstract_report"
    _template="unefa.estudiante_unefa"
    _wrapped_report_class=reportes_estudiantes
    
