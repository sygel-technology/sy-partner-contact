# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging


def _edit_address_format(country, inserted_field, reference_field, mode="after"):
    """Inserts a text in the address format of a country
    country
    inserted_field: field to insert.'
    reference_field: reference address field
    mode: after or before. Insert text after or before the reference field
    returns: True if sucess. False if failure
    """
    country.ensure_one()
    if mode not in ["after", "before"]:
        raise Exception("Mode should be 'after' or 'before'")
    if ")s" not in inserted_field:
        inserted_field = f"%({inserted_field})s"
    if ")s" not in reference_field:
        reference_field = f"({reference_field})s"

    separator = "\n"
    address_splitted = country.address_format.split(separator)
    try:
        position = next(
            i for i, v in enumerate(address_splitted) if reference_field in v
        )
    except Exception:
        return False
    if mode == "after":
        position += 1
    address_splitted.insert(position, inserted_field)
    country.address_format = separator.join(address_splitted)
    return True


def post_init_hook(env):
    inserted_field = "code_program_territory_name"
    operations = [
        ("code_program_name", "before"),
    ]
    countries = env["res.country"].search([])
    for country in countries:
        sucess = False
        i = 0
        while not sucess and i < len(operations):
            sucess = _edit_address_format(
                country, inserted_field, operations[i][0], operations[i][1]
            )
            i += 1
        if not sucess:
            logging.error("{country.name}'s address could not be edited")


def uninstall_hook(env):
    fields = ["code_program_territory_name", "code_program_territory_id"]
    countries = env["res.country"].search([])
    for country in countries:
        country_address = country.address_format
        for field in fields:
            formatted_field = f"%({field})s"
            country_address = country_address.replace(formatted_field, "")
            country_address = country_address.replace("\n\n", "\n")
        country.address_format = country_address
