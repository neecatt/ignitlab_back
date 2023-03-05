import sys
from time import sleep
from web3 import Web3, HTTPProvider
from startup_stocks import StartupStocks

# The url for node connecting to Ropsten testnet (the chain), you may apply it at https://infura.io/
w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/ID_FROM_INFURA"))

# Contract address provided by TA
contract_address = "CONTRACT_ADDRESS"

# Private key of wallet on testnet
wallet_private_key = "YOUR_PRIVATE_KEY"

# Address of wallet on testnet
wallet_address = "YOUR_WALLET_ADDRESS"

# Value to send, make sure you have enough value in account (must > 3gwei)
value_to_send = 0.1
amount_in_wei = w3.toWei(value_to_send,'ether')

# Parse contract
startup_stocks = StartupStocks(w3, contract_address)

# Prepare transaction
txn_dict = {
        'value': amount_in_wei,
        'gas': 2000000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': w3.eth.getTransactionCount(wallet_address),
        'chainId': 3,
}

# Prepare contract function
company_name = "YOUR_COMPANY_NAME"
num_shares = 100
txn_hash = startup_stocks.buy_shares(company_name, num_shares).buildTransaction(txn_dict)

# Sign & send txn
signed_txn = w3.eth.account.signTransaction(txn_hash, wallet_private_key)
txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

# Wait for result
txn_receipt = None
count = 0
while txn_receipt is None and (count < 30):
    try:
        txn_receipt = w3.eth.getTransactionReceipt(txn_hash)
        print(txn_receipt)
    except:
        print('Waiting for transaction to be approved ... ({})'.format(count), end='\r')
        count += 1
        sleep(5)
if txn_receipt is None:
    print('Failed.')
else:
    print('Done.')
