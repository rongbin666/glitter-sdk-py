import time
from glitter_sdk.client.lcd import LCDClient
from glitter_sdk.core import Numeric, Coins
from glitter_sdk.key.mnemonic import MnemonicKey
from config import *


def insert():

    lcd_client = LCDClient(
        chain_id=chain_id,
        url=url,
        gas_prices=gas_prices,
        gas_adjustment=gas_adjustment)
    #  new client
    db_client = lcd_client.db(MnemonicKey(mnemonic_key, 0, 0))
    db_name = "library_test"
    user_tb_name = "user"

    # batch insert
    print("=====insert multi rows:")
    rows = [{
        '_id': 'mirror_0xbDc4199575A5FA3F19e9888C5d51Bde798F404Cc',
        '_tx_id': '',
        'author': '0xbDc4199575A5FA3F19e9888C5d51Bde798F404Cc',
        'avatar_url': 'https://mirror-media.imgix.net/publication-images/fB3kzXkesQJbPVhKlTc86.png?h=592&w=592',
        'display_name': 'Mirror Development',
        'domain': '',
        'entry_num': 100,
        'handle': 'dev.mirror.xyz',
        'source': 'mirror',
        'status': 0
    }, {
        '_id': 'mirror_0x51448923d8a215a5A8cd872a51f22c2f5c43b444',
        '_tx_id': '',
        'author': '0x51448923d8a215a5A8cd872a51f22c2f5c43b444',
        'avatar_url': 'https://mirror-media.imgix.net/publication-images/6000699e-e77e-4216-b44c-872eafc466de.jpeg?h=2064&w=2000',
        'display_name': 'Chase Chapman',
        'domain': '',
        'entry_num': 50,
        'handle': 'chase.mirror.xyz',
        'source': 'mirror',
        'status': 0
    }]
    rst = db_client.batch_insert(db_name, user_tb_name, rows)
    print(rst)

    # update
    print("=====update:")
    cols = {"status": 1}
    where = {"author": "0xbDc4199575A5FA3F19e9888C5d51Bde798F404Cc"}
    # valid only for standard engine
    rst = db_client.update(db_name, user_tb_name, cols, where)
    print(rst)


if __name__ == "__main__":
    insert()
