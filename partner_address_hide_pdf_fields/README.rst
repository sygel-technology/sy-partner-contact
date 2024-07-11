.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

===============================
Partner Address Hide PDF Fields
===============================

This module adds base methods in res partner to hide new address fields in PDF
but not in the res_partner_many_to_one internal widget


Installation
============

To install this module, you need to:

#. Only install


Configuration
=============

To configure this module, you need to:

#. Only install


Usage
=====

Suppose you have a new module that adds two fields: 'field_id' and 'field_name'

To use this module, you need to inherit it in your new module, and add the new fields to the 
_hided_in_pdf_address_fields() function of 'res.partner':

.. code-block:: python

   class ResPartner(models.Model):
      _inherit = 'res.partner'

      @api.model
      def _hided_in_pdf_address_fields(self):
         return super()._hided_in_pdf_address_fields() + [
            'field_id',
            'field_name'
         ]



Bug Tracker
===========

Bugs and errors are managed in `issues of GitHub <https://github.com/sygel-technology/sy-partner-contact/issues>`_.
In case of problems, please check if your problem has already been
reported. If you are the first to discover it, help us solving it by indicating
a detailed description `here <https://github.com/sygel-technology/sy-partner-contact/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* Sygel, Odoo Community Association (OCA)


Contributors
~~~~~~~~~~~~

* Valentin Vinagre <valentin.vinagre@sygel.es>
* Alberto Martínez <alberto.martinez@sygel.es>


Maintainer
~~~~~~~~~~

This module is maintained by Sygel.

.. image:: https://www.sygel.es/logo.png
   :alt: Sygel
   :target: https://www.sygel.es

This module is part of the `Sygel/sy-partner-contact <https://github.com/sygel-technology/sy-partner-contact>`_.

To contribute to this module, please visit https://github.com/sygel-technology/.

