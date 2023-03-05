import os
import time
from web3 import Web3
from dotenv import load_dotenv

from contract import CONTRACT_ABI, CONTRACT_ADDRESS
from transaction import buy_stock

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URL')))
w3.eth.default_account = os.getenv('INVESTOR_ADDRESS')

contract = w3.eth.contract(
    address=CONTRACT_ADDRESS,
    abi=CONTRACT_ABI
)

def check_stock_balance():
    balance = contract.functions.balanceOf(w3.eth.default_account).call()
    print(f"You currently have {balance} startup stock(s)")

def buy_stock_from_startup(startup_address, stock_amount):
    tx_hash = buy_stock(w3, startup_address, stock_amount)
    print(f"Transaction sent with hash: {tx_hash.hex()}")

    txn_receipt = None
    count = 0
    while txn_receipt is None and (count < 30):
        try:
            txn_receipt = w3.eth.getTransactionReceipt(tx_hash)
        except:
            print('Waiting for transaction to be approved... ({})'.format(count), end='\r')
            count += 1
            time.sleep(5)

    if txn_receipt is None:
        print('Transaction failed.')
    else:
        print('Transaction succeeded.')
        check_stock_balance()
