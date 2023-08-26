from glitter_sdk.client.lcd import LCDClient
from glitter_sdk.util.parse_sql import prepare_sql
from config import *


def query():

    lcd_client = LCDClient(
        chain_id=chain_id,
        url=url,
        gas_prices=gas_prices,
        gas_adjustment=gas_adjustment)
    #  new client
    db_client = lcd_client.db(MnemonicKey(mnemonic_key, 0, 0))

    # query
    print("=====query:")
    sql = prepare_sql("select * from {}.{} where author=%s ".format(db_name, user_tb_name),
                      ["0xbDc4199575A5FA3F19e9888C5d51Bde798F404Cc"])
    print(sql)
    rst = db_client.query(sql)
    print(rst)

    sql = "select max(entry_num) from {}.{}".format(db_name, user_tb_name)
    print(sql)
    rst = db_client.query(sql)
    print(rst)


if __name__ == "__main__":
    query()
