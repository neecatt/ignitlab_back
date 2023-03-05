import web3 as w3

class StartupStocks:
    def __init__(self, contract_address, abi):
        self.contract = w3.eth.contract(address=contract_address, abi=abi)

    def buy_stocks(self, amount):
        txn_hash = self.contract.functions.buyStocks(amount).transact({'from': w3.eth.defaultAccount, 'value': amount * self.price})
        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
        return txn_receipt

    def get_balance(self, account):
        return self.contract.functions.balances(account).call()

    def get_remaining_stocks(self):
        return self.contract.functions.remainingStocks().call()

    def withdraw(self):
        txn_hash = self.contract.functions.withdraw().transact({'from': w3.eth.defaultAccount})
        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
        return txn_receipt
