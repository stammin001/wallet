# Import dependencies
import os
import subprocess
import json

from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account

from bit import PrivateKeyTestnet
from bit.network import NetworkAPI

from dotenv import load_dotenv
from constants import *

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("FINTECH-WALLET")

# Create a function that derives keys for different coins in wallet
def derive_wallets(mnemonic, coin, keys_number):
    
    command = 'php derive -g --mnemonic="' + str(mnemonic) + '"' + ' --cols=path,address,privkey,pubkey --numderive=' + str(keys_number) + ' --coin=' + str(coin) + ' --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    
    return json.loads(output)

# Create a function that converts privkey strings to account objects.
def priv_key_to_account(private_key, coin):
    
    if coin == ETH:
        return Account.privateKeyToAccount(private_key)
    
    if coin == BTC:
        return PrivateKeyTestnet(private_key)

# Create a function that creates an unsigned transaction appropriate metadata.
def create_tx(sender, recipient, amount, coin):
    
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas({"from": sender.address, "to": recipient, "value": amount})
        
        return {
            "to": recipient,
            "from": sender.address,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(sender.address)
        }
        
    if coin == BTC:
        return PrivateKeyTestnet.prepare_transaction(sender.address, [(recipient, amount, BTC)])  

# Create a function that creates, signs and sends the transaction.
def send_tx(sender, recipient, amount, coin):
    
    if coin == ETH:
        transaction = create_tx(sender, recipient, amount, coin)
        sign_transaction = sender.sign_transaction(transaction)
        result = w3.eth.sendRawTransaction(sign_transaction.rawTransaction)
        return result.hex()
    
    if coin == BTC:
        transaction = create_tx(sender, recipient, amount, coin)
        sign_transaction = account.sign_transaction(transaction)
        result = NetworkAPI.broadcast_tx_testnet(sign_transaction)       
        return result.hex()

coins = {BTC: derive_wallets(mnemonic, BTC, 10), ETH: derive_wallets(mnemonic, ETH, 10)}
for coin in coins:
    print(f'coin = {coin}')
    
    for adds_keys in coins[coin]:
        print(f'address = {adds_keys["address"]}, private_key = {adds_keys["privkey"]}, public_key = {adds_keys["pubkey"]} \n')
