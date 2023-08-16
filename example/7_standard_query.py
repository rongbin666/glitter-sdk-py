from glitter_sdk.client.lcd import LCDClient
from glitter_sdk.core import Numeric, Coins
from glitter_sdk.key.mnemonic import MnemonicKey
from glitter_sdk.util.parse_sql import prepare_sql


def query():
    lcd_client = LCDClient(
        chain_id="glitter_12000-2",
        # url="https://api.xian.glitter.link",
        url="http://sg3.testnet.glitter.link:41317/",
        gas_prices=Coins.from_str("1agli"),
        gas_adjustment=Numeric.parse(2.5))
    mk = "lesson police usual earth embrace someone opera season urban produce jealous canyon shrug usage subject cigar imitate hollow route inhale vocal special sun fuel"
    #  new client
    db_client = lcd_client.db(MnemonicKey(mk, 0, 0))
    db_name = "library_test"
    tb_name = "user"

    # query
    print("=====query:")
    sql = prepare_sql("select * from {}.{} where author=%s ".format("index3", tb_name),
                      ["0xbDc4199575A5FA3F19e9888C5d51Bde798F404Cc"])
    print(sql)
    rst = db_client.query(sql)
    print(rst)

    sql = "select max(entry_num) from {}.{}".format(db_name, tb_name)
    print(sql)
    rst = db_client.query(sql)
    print(rst)


if __name__ == "__main__":
    query()
