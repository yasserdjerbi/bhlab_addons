# Copyright 2014 Numérigraphe
# Copyright 2016 Sodexis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'bhlab Stock available',
    'version': '12.0.1.0.1',
    'author': 'nadir BHLab',
    'development_status': 'Production/Stable',
    'category': 'Warehouse',
    'depends': ['stock'],
    'license': 'AGPL-3',
    'data': [
        'views/product_template_view.xml',
        'views/product_product_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
}