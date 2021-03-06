# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Gallery For Community Portal',
    'category': 'website',
    'summary': 'Gallery management',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'maintainer': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'http://www.serpentcs.com',
    'depends': [
        'cp_event',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/gallery_view.xml',
        'views/menu_details.xml',
        'views/template_list_events.xml',
        'views/template_show_event_photos.xml'
    ],
    'installable': True,
    'application': True,
}
