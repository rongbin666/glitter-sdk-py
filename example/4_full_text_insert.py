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
    ebook_tb_name = "ebook"

    # insert
    print("=====insert one row:")
    row = {
        '_id': '7f2b6638ab9ec6bfeb5924bf8e7f17e',
        '_tx_id': '',  # The _tx_id is filled in automatically
        'author': 'J. K. Rowling',
        'extension': 'pdf',
        'filesize': 743406,
        'ipfs_cid': 'bafykbzaceah6cdfb3syzrntpuuxycsfp55rtmby4oxzli2wodajgtea3ghafg',
        'issn': '',
        'language': 'English',
        'publisher': '',
        'series': '',
        'tags': "'",
        'title': "Harry Potter and the Sorcerers Stone",
        'year': '1999'
    }
    rst = db_client.insert(db_name, ebook_tb_name, row)
    print(rst)
    return

    # batch insert
    print("=====insert multi rows:")
    rows = [{
        '_id': '1532675066c4913e5d0f44b82014ca9e',
        '_tx_id': '',
        'author': 'J. K. Rowling',
        'extension': 'pdf',
        'filesize': 3475199,
        'ipfs_cid': 'bafykbzaceasltcubwipjpirdmxklcwdznq4mkdx4zrey5xradmoaif34a5bn2',
        'issn': '',
        'language': 'English',
        'publisher': '',
        'series': 'Harry Potter 2',
        'tags': '',
        'title': 'Harry Potter and the Chamber of Secrets (Book 2)',
        'year': '2000'
    },
        {
            '_id': '50740153c2bf4a5db99f8b807b4a4b60',
            '_tx_id': '',
            'author': "J.K. Rowling, Mary GrandPré",
            'extension': 'pdf',
            'filesize': 4478241,
            'ipfs_cid': 'bafykbzaceaaxtdouipt5managw2creovvg6pscsjkyqfqtocpaqg3zsmbndtm',
            'issn': '',
            'language': 'English',
            'publisher': 'Scholastic',
            'series': 'Harry Potter 3',
            'tags': '',
            'title': 'Harry Potter and the Prisoner of Azkaban',
            'year': '1999'
        }]
    rst = db_client.batch_insert(db_name, ebook_tb_name, rows)
    print(rst)


if __name__ == "__main__":
    insert()
