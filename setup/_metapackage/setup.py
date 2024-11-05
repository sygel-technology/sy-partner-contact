import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-partner-contact",
    description="Meta package for sygel-technology-sy-partner-contact Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-contact_referred>=15.0dev,<15.1dev',
        'odoo-addon-partner_contact_old_acc_number>=15.0dev,<15.1dev',
        'odoo-addon-partner_contact_old_migration_fields>=15.0dev,<15.1dev',
        'odoo-addon-partner_vat_required>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
