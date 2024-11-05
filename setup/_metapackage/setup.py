import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-sygel-technology-sy-partner-contact",
    description="Meta package for sygel-technology-sy-partner-contact Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-reorder_partner_firstname_lastname',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
