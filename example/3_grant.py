import time
from glitter_sdk.client.lcd import LCDClient
from glitter_sdk.core import Numeric, Coins
from glitter_sdk.key.mnemonic import MnemonicKey


def grant_demo():
    db = "library_test"
    table = "ebook"

    lcd_client = LCDClient(
        chain_id="glitter_12000-2",
        # url="https://api.xian.glitter.link",
        url="http://sg3.testnet.glitter.link:41317/",
        gas_prices=Coins.from_str("1agli"),
        gas_adjustment=Numeric.parse(2.5))
    mk = "lesson police usual earth embrace someone opera season urban produce jealous canyon shrug usage subject cigar imitate hollow route inhale vocal special sun fuel"
    #  new client
    db_client = lcd_client.db(MnemonicKey(mk, 0, 0))
    address = MnemonicKey(mk, 0, 0).acc_address
    print(address)

    # grant table writer role to address
    print("=====grant table writer:")
    rst = db_client.grant_writer(address, db, table)
    print(rst)

    # grant database admin role to address
    print("=====grant database admin")
    rst = db_client.grant_admin(address, db)
    print(rst)


if __name__ == "__main__":
    grant_demo()
