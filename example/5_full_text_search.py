import time
from glitter_sdk.client.lcd import LCDClient
from glitter_sdk.core import Numeric, Coins
from glitter_sdk.key.mnemonic import MnemonicKey
from glitter_sdk.util.parse_sql import prepare_sql
from glitter_sdk.util.parse_query_str import *
from glitter_sdk.util.highlight import *
from config import *


def search():
    lcd_client = LCDClient(
        chain_id=chain_id,
        url=url,
        gas_prices=gas_prices,
        gas_adjustment=gas_adjustment)

    #  new client
    db_client = lcd_client.db(MnemonicKey(mnemonic_key, 0, 0))

    # query all
    print("=====query all:")
    rst = db_client.query("select * from database_test.book limit 10")

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
    sql = "select  {} _score, * from {}.{} where  query_string(?)  limit 0,10".format(highlight, db_name, book_tb_name)
    rst = db_client.query(sql, [query_str])
    print(rst)

    print("=====match phrase query:")
    title = "Potter Harry"  # no result return
    title = "Harry Potter"
    # about more phrase query https://docs.glitterprotocol.io/#/dev/search_query?id=phrases
    queries = []
    queries.append(MatchPhraseQuery("title", title, 1))
    query_str = query_string_prepare(queries)
    highlight = highlight_prepare(["title"])
    sql = "select  {} _score, * from {}.{} where  query_string(%s)  limit 0,10".format(highlight, db_name, book_tb_name)
    sql = prepare_sql(sql, [query_str])
    print(sql)
    rst = db_client.query(sql)
    print(rst)


if __name__ == "__main__":
    search()
