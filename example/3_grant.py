import time
from glitter_sdk.client.lcd import LCDClient
from glitter_sdk.core import Numeric, Coins
from glitter_sdk.key.mnemonic import MnemonicKey
from config import *


def grant_demo():
    lcd_client = LCDClient(
        chain_id=chain_id,
        url=url,
        gas_prices=gas_prices,
        gas_adjustment=gas_adjustment)
    #  new client
    db_client = lcd_client.db(MnemonicKey(mnemonic_key, 0, 0))
    address = MnemonicKey(mnemonic_key, 0, 0).acc_address
    print(address)

    # grant table writer role to address
    print("=====grant table writer:")
    rst = db_client.grant_writer(address, db_name, book_tb_name)
    print(rst)

    # grant database admin role to address
    print("=====grant database admin")
    rst = db_client.grant_admin(address, db_name)
    print(rst)


if __name__ == "__main__":
    grant_demo()
