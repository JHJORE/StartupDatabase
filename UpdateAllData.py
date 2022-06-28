from BrRegTilsagn import brreg_tilsagn_to_db
from EnhetBrReg import company_info_brreg
from Aid import innovation_norway_help


def update_data():
    print("This will take some time")
    brreg_tilsagn_to_db()
    innovation_norway_help()
    company_info_brreg()

update_data()

    