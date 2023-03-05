import os
from django.shortcuts import render
from .web3_utils import w3
from .contract import CONTRACT_ABI, CONTRACT_ADDRESS


contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def buy_shares(request):
    startup_name = "MyStartup"
    num_shares = 100

    txn_dict = {
        'value': w3.toWei(1, 'ether'),
        'gas': 2000000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': w3.eth.getTransactionCount(w3.eth.default_account),
        'chainId': w3.eth.chainId,
    }

    txn = contract.functions.buyShares(startup_name, num_shares).buildTransaction(txn_dict)
    signed_txn = w3.eth.account.signTransaction(txn, private_key=os.getenv('INVESTOR_PRIVATE_KEY'))
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    context = {
        'txn_hash': txn_hash.hex(),
    }

    return render(request, 'buy_shares.html', context)