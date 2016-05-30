{
    'name':'Estudiantes Unefa',
    'version': '1.0',
    'depends': ['base_setup','website'],
    'author': 'IRP unefa (Comunidad Bachaco.ve)',
    'category': '',
    'description': """
    Nuestro primer modulo de estudiantes unefa
    """,
    'update_xml': [],
    "data" : [
        "views/estudiantes_views.xml",
        "views/res_company.xml",
        "views/estados_views.xml",
        "views/municipios_views.xml",
        "views/parroquias_views.xml",
        "views/deportes_views.xml",
        "views/familiares_contactos_views.xml",
        "views/template_reporte_alumnos.xml",
        "views/template_reporte_alumnos_wizard.xml",
        "wizard/reporte_alumnos_wizard.xml",
        "reportes/reportes_alumnos.xml",
        ],
    'installable': True,
    'auto_install': False,
}
