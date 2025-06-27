This module adds base methods in res partner to hide new address fields in PDF
but not in the res_partner_many_to_one internal widget.

It is a technical module meant to be used by developers: it does not change any behavior on its own.
When combined with another module that adds new fields to the partner address,
it allows those fields to be shown in the UI but hidden from the address printed in documents like invoices or quotations.
