{
    'name': 'Gomez POS Receipt Custom',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Personalización de recibos POS para Gomez',
    'description': """
        Módulo de personalización para los recibos del POS de Gomez.

        Características principales:
        - Personalización del header del recibo
        - Personalización del footer del recibo con mensajes personalizados
        - Estilo tipográfico Courier New para todo el recibo
        - Eliminación del logo de Odoo
        - Compatible con Odoo 18
    """,
    'author': 'Gomez',
    'depends': ['point_of_sale'],
    'data': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'gomez_pos_receipt_custom/static/src/xml/receipt_templates.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
