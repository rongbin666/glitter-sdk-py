from glitter_sdk.core import Numeric, Coins
from glitter_sdk.key.mnemonic import MnemonicKey

chain_id = "glitter_12000-2"
# url = "https://api.xian.glitter.link"
url = "http://sg3.testnet.glitter.link:41317"
gas_prices = Coins.from_str("1agli")
gas_adjustment = Numeric.parse(2.5)
mnemonic_key = "lesson police usual earth embrace someone opera season urban produce jealous canyon shrug usage subject cigar " \
               "imitate hollow route inhale vocal special sun fuel"

db_name = "database_test"
book_tb_name = "book_v2"
user_tb_name = "user_v2"

