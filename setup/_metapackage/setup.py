import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-sygel-technology-sy-partner-contact",
    description="Meta package for sygel-technology-sy-partner-contact Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-partner_contact_old_acc_number',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
