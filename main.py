from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider
from mnemonic import Mnemonic
import hashlib
import bip32utils

api_key=""
mnemonic_phrase = "" #mnemonic_phrase of wallet A that has rights of wallet B

client = Tron(HTTPProvider(api_key=api_key))
mnemo = Mnemonic("english")
seed = mnemo.to_seed(mnemonic_phrase)

master_key = bip32utils.BIP32Key.fromEntropy(seed)

child_key = master_key.ChildKey(44 + bip32utils.BIP32_HARDEN) \
                        .ChildKey(195 + bip32utils.BIP32_HARDEN) \
                        .ChildKey(0 + bip32utils.BIP32_HARDEN) \
                        .ChildKey(0) \
                        .ChildKey(0)

priv_key = PrivateKey(child_key.PrivateKey())

address = input("Your address of wallet with MultiSign:  ") #Wallet's address B that has multisign (and doesn't have rights for example)
receiver_addr = input("Address of wallet to get tron:  ")
def send_trx(amount, toadress):
    txn = (
        client.trx.transfer(address, toadress, int(int(amount-2) * 1e6))
        .build()
        .sign(priv_key)
    )
    result = txn.broadcast()
    print("Transaction ID:", txn.txid)
  send_trx(1,receiver_addr) #Example
