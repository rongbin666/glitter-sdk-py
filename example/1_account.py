from mnemonic.mnemonic import Mnemonic
from glitter_sdk.client.lcd import LCDClient
from glitter_sdk.core import Numeric, Coins
from glitter_sdk.key.mnemonic import MnemonicKey
from config import *

def generate():
    m = Mnemonic("english")
    m_str = m.generate(256)
    print(m_str)
    for i in range(10):
        mk = MnemonicKey(m_str, 0, i)
        print("{}:{}".format(i, mk.acc_address))


def transfer():
    client = LCDClient(
        chain_id=chain_id,
        url=url,
        gas_prices=gas_prices,
        gas_adjustment=gas_adjustment)

    from_addr = MnemonicKey(mnemonic_key, 0, 0)
    to_addr = MnemonicKey(mnemonic_key, 0, 1).acc_address

    # transfer
    r = client.db(from_addr).transfer(to_addr, "10agli")
    print(r)
    client.bank.balance(from_addr.acc_address)
    # query balance
    print("the balance of {} is {}".format(from_addr.acc_address, client.bank.balance(from_addr.acc_address)))
    print("the balance of {} is {}".format(to_addr, client.bank.balance(to_addr)))


if __name__ == "__main__":
    # generate()
    transfer()
