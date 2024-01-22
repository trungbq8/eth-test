from eth_account import Account
from web3 import Web3
import mnemonic
from datetime import datetime

rpc_server = 'https://api.securerpc.com/v1'
w3 = Web3(Web3.HTTPProvider(rpc_server))
Account.enable_unaudited_hdwallet_features()
def generate_ethereum_address_from_seed_phrase(seed_phrase):
    account = Account.from_mnemonic(seed_phrase)
    address = account.address
    return address
def generate_seed_phrase():
    seed_phrase = mnemonic.Mnemonic(language='english').generate(strength=128)
    return seed_phrase
found = False
while found == False:
    seed_phrase = generate_seed_phrase()
    ethereum_address = generate_ethereum_address_from_seed_phrase(seed_phrase)
    balance_wei = w3.eth.get_balance(ethereum_address)
    current_time = datetime.now()
    current_second = current_time.second
    if current_second == 30:
      balance_test = w3.eth.get_balance("0xBE0eB53F46cd790Cd13851d5EFf43D12404d33E8")
      if balance_test > 0:
        print(f"{datetime.now()} - Check balance work properly")

    if balance_wei > 0:
        with open('seed.txt', 'w') as file:
            file.write(seed_phrase)
        print(f"Seed: {seed_phrase}")
        print(f"Balance of {ethereum_address}: {balance_wei} ETH")
        found = True
    print(f"{balance_wei} ETH")
