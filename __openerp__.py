{
    'name':'Estudiantes Unefa',
    'version': '1.0',
    'depends': ['base_setup'],
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
        ],
    'installable': True,
    'auto_install': False,
}
