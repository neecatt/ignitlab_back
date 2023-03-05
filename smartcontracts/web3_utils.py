import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URL')))
w3.eth.default_account = os.getenv('INVESTOR_ADDRESS')