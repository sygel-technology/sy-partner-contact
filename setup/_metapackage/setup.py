import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-partner-contact",
    description="Meta package for sygel-technology-sy-partner-contact Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-base_partner_sequence_contacts>=16.0dev,<16.1dev',
        'odoo-addon-partner_communication>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_old_acc_number>=16.0dev,<16.1dev',
        'odoo-addon-partner_contact_old_migration_fields>=16.0dev,<16.1dev',
        'odoo-addon-partner_identification_disable>=16.0dev,<16.1dev',
        'odoo-addon-partner_invoicing_frequency>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
