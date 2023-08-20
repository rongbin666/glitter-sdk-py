import time
from mnemonic.mnemonic import Mnemonic
from glitter_sdk.client.lcd import LCDClient
from glitter_sdk.core import Numeric, Coins
from glitter_sdk.key.mnemonic import MnemonicKey
from config import *

def ddl():
    lcd_client = LCDClient(
        chain_id=chain_id,
        url=url,
        gas_prices=gas_prices,
        gas_adjustment=gas_adjustment)
    #  new client
    db_client = lcd_client.db(MnemonicKey(mnemonic_key, 0, 0))

    # create database
    print("====create database:")
    db_name = "database_test"
    r = db_client.create_database(db_name)
    print(r)
    time.sleep(10)  # wait for the transaction to chain

    # create full_text engine table
    print("=====create full_text engine table:")
    book_tb_name = "book"
    book_schema = """
     CREATE TABLE IF NOT EXISTS {}.{} (
        _id VARCHAR(255) PRIMARY KEY COMMENT 'md5',
        title VARCHAR(2000) COMMENT 'title',
        series VARCHAR(512) COMMENT 'series',
        author VARCHAR(512) COMMENT 'author',
        publisher VARCHAR(512) COMMENT 'publisher',
        language VARCHAR(128) COMMENT 'language',
        tags VARCHAR(512) COMMENT 'tags',
        issn VARCHAR(32) COMMENT 'issn',
        ipfs_cid VARCHAR(512) COMMENT 'ipfs cid',
        extension VARCHAR(512) COMMENT 'extension',
        year VARCHAR(14) COMMENT 'year',
        filesize INT(11),
        _tx_id VARCHAR(255) COMMENT 'transaction id auto generate',
        FULLTEXT INDEX(title) WITH PARSER standard,
        FULLTEXT INDEX(series) WITH PARSER keyword,
        FULLTEXT INDEX(author) WITH PARSER standard,
        FULLTEXT INDEX(publisher) WITH PARSER standard,
        FULLTEXT INDEX(language) WITH PARSER standard,
        FULLTEXT INDEX(tags) WITH PARSER standard,
        FULLTEXT INDEX(ipfs_cid) WITH PARSER keyword,
        FULLTEXT INDEX(extension) WITH PARSER keyword,
        FULLTEXT INDEX(year) WITH PARSER keyword
    ) ENGINE = full_text COMMENT 'book records';
    """.format(db_name, book_tb_name)
    rst = db_client.create_table(book_schema)
    print(rst)

    # create standard engine table
    print("=====create standard engine table:")
    user_tb_name = "user"
    user_schema = """
    CREATE TABLE  IF NOT EXISTS {}.{} (
     _id VARCHAR(500) PRIMARY KEY COMMENT 'document id',
     author VARCHAR(255) NOT NULL Default '' COMMENT 'ens address or lens address',
     handle VARCHAR(128) NOT NULL Default '' COMMENT 'ens or lens handler', 
     display_name VARCHAR(128) NOT NULL Default '' COMMENT 'nickname',
     avatar_url VARCHAR(255) NOT NULL Default '' COMMENT 'the url of avatar',
     entry_num int(11) NOT NULL Default 0 COMMENT 'the article numbers' ,
     status int(11) NOT NULL Default 0 ,         
     source VARCHAR(64) NOT NULL Default '' COMMENT 'enum: mirror, lens, eip1577',
     domain VARCHAR(128) NOT NULL Default '' COMMENT 'mirror second domain',
     _tx_id VARCHAR(255) COMMENT 'transaction id auto generate',
     KEY `author_idx` (`author`),
     KEY `handle_idx` (`handle`),
     KEY `display_name_idx` (`display_name`),
     KEY `domain_idx` (`domain`)
     ) ENGINE=standard COMMENT 'all user info:mirror,lens,eip1577 and so on';
    """.format(db_name, user_tb_name)
    rst = db_client.create_table(user_schema)
    print(rst)
    time.sleep(10)  # wait for the transaction to chain

    # list tables
    print("=====list table:")
    rst = db_client.list_tables(database=db_name)
    print(rst)

    # show schema
    print("=====show create table:")
    rst = db_client.show_create_table(db_name, book_tb_name)
    print(rst)
    rst = db_client.show_create_table(db_name, user_tb_name)
    print(rst)

    # add column
    # db_client.add_column(db_name, user_tb_name, "test varchar(255)") # valid only for standard engine

    # drop table
    # db_client.drop_table(db_name, user_tb_name)


if __name__ == "__main__":
    ddl()
