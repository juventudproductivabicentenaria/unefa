# -*- coding: utf-8 -*-
import inspect, os
from openerp.osv import fields, osv

class re_company(osv.osv):
    _name='res.company'
    _inherit=['res.company']
    
    def _get_logo(self, cr, uid, ids):
        ruta_actual=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        ruta_actual=ruta_actual.split('models')
        ruta_actual=''.join(ruta_actual)
        return open(os.path.join(
                                    ruta_actual,
                                    'static' ,
                                    'img' ,
                                    'res_company_logo.png'
                                ), 'rb') .read().encode('base64')
    
    _columns={
        'rif':fields.char('Rif',size=9,required=True,help='Aquí se coloca el Rif del la universidad'),
    }
    
    _defaults={
        'logo':_get_logo
    }
