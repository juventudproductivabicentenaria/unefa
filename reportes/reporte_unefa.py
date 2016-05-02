 # -*- encoding: utf-8 -*-

from openerp.osv import osv
import time
from openerp.report import report_sxw

class Reportes_Unefa(report_sxw.rml_parse):
    def __init__(self , cr, uid, name, context):
        super(Reportes_Unefa,self).__init__(cr,uid,name,context)
        self.localcontext.update({
            'time':time,
            'get_data': self.get_data,
        })
        self.context = context
    
    def get_data(self):
        return 'hola mundo'

        
class reportEstudiantesUnefa(osv.AbstractModel):
    _name = "report.unefa.reporte_estudiante_unefa_qweb"
    _inherit = "report.abstract_report"
    _template = "unefa.reporte_estudiante_unefa_qweb"
    _wrapped_report_class = Reportes_Unefa
# report_sxw.report_sxw('report.reportEstudiantesUnefa', 'unefa.estudiantes', 'local_unefa/unefa/report/reportEstudiantesUnefa.rml', parser=Reportes_Unefa,header=False)
