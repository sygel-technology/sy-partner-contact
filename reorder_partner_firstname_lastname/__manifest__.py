# Copyright 2020 Valentin Vinagre <valentin.vinagre@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Reorder partner firstname lastname',
    'version': '11.0.1.0.0',
    'category': 'Contact',
    'summary': 'Reorder firstname and lastname fields in the views.',
    'author': 'Sygel',
    'website': 'https://www.sygel.es',
    'license': 'AGPL-3',
    'depends': [
        'partner_firstname',
    ],
    'data': [
        'views/res_partner.xml',
        'views/res_user.xml'
    ],
    'installable': True,
}
