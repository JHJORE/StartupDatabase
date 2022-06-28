from BrRegTilsagn import brreg_tilsagn_to_db
from CapitalRaises import capital_raises_to_db
from EnhetBrReg import company_info_brreg
from Aid import innovation_norway_help


def update_data():
    brreg_tilsagn_to_db()
    innovation_norway_help()
    company_info_brreg()

update_data()
    