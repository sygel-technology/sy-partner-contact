Suppose you have a new module that adds two fields: 'field_id' and 'field_name'

To use this module, you need to inherit it in your new module, and add the new fields to the
_hided_in_pdf_address_fields() function of 'res.partner':

    @api.model
    def _hided_in_pdf_address_fields(self):
        return super()._hided_in_pdf_address_fields() + [
          'field_id',
          'field_name'
        ]
