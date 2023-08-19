import time
from glitter_sdk.client.lcd import LCDClient
from glitter_sdk.core import Numeric, Coins
from glitter_sdk.key.mnemonic import MnemonicKey
from glitter_sdk.util.parse_sql import prepare_sql
from glitter_sdk.util.parse_query_str import *
from glitter_sdk.util.highlight import *


def search():
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
    tb_name = "ebook"

    # query all
    print("=====query all:")
    rst = db_client.query("select * from library_test.ebook where _id=? limit 10",['7f2b6638ab9ec6bfeb5924bf8e7f17e1'])
    print(rst)
    return

    # full text search
    print("=====match query:")
    title = "Potter Harry"  # same as Harry Potter
    title = "Harry Potter"
    author = "J.K. Rowling"
    queries = []
    queries.append(MatchQuery("title", title, 1))
    queries.append(MatchQuery("author", author, 0.5))
    query_str = query_string_prepare(queries)
    highlight = highlight_prepare(["author", "title"])
    sql = "select  {} _score, * from {}.{} where  query_string(%s)  limit 0,10".format(highlight, db_name, tb_name)
    sql = prepare_sql(sql, [query_str])
    print(sql)
    rst = db_client.query(sql)
    print(rst)

    print("=====match phrase query:")
    title = "Potter Harry"  # no result return
    title = "Harry Potter"
    queries = []
    queries.append(MatchPhraseQuery("title", title, 1))
    query_str = query_string_prepare(queries)
    highlight = highlight_prepare(["title"])
    sql = "select  {} _score, * from {}.{} where  query_string(%s)  limit 0,10".format(highlight, db_name, tb_name)
    sql = prepare_sql(sql, [query_str])
    print(sql)
    rst = db_client.query(sql)
    print(rst)


if __name__ == "__main__":
    search()
