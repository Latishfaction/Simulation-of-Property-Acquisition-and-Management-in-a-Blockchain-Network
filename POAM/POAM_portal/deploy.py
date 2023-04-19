from solcx import compile_standard, install_solc
import json
from web3 import Web3

with open(".\property.sol", "r") as file:
    property_file = file.read()
    # print(property_file)

install_solc("0.6.0")

# compiling solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"property.sol": {"content": property_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

with open("./compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["property.sol"]["Agreement"]["evm"]["bytecode"][
    "object"
]

# get abi
abi = json.loads(compiled_sol["contracts"]["property.sol"]["Agreement"]["metadata"])[
    "output"
]["abi"]

# connecting to ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chainId = 1337
my_address = "0x7F9CB6A3B92431D87Bc576Cb279684FDAF9a48D1"
private_key = "0x894a334895ed42a061bbeffbaca3116ae08e559bf47e45c37105622de4c10a08"


def deploy_agreement():
    # creating contract object
    Agreement = w3.eth.contract(abi=abi, bytecode=bytecode)
    """ 
    Creating Transactions

    1) Build Transaction
    2) Signed Transaction
    3) Deploy Transaction
    """
    # Get number of transaction
    nonce = w3.eth.get_transaction_count(my_address)

    transaction = Agreement.constructor().build_transaction(
        {
            "chainId": chainId,
            "gasPrice": w3.eth.gas_price,
            "from": my_address,
            "nonce": nonce,
        }
    )
    # sign transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

    # deploy transaction to ganache
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # working with smart contract
    #  call -> making call and getting return value (no state change)
    # transact -> fill value in the smart contract
    agreement_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

    # print(agreement_contract.functions.getDate().call())
    # print(agreement_contract.functions.setDate())

    # setting date
    setDate = agreement_contract.functions.setDate(date).build_transaction(
        {
            "chainId": chainId,
            "from": my_address,
            "nonce": nonce + 1,
        }
    )
    signed_setDate = w3.eth.account.sign_transaction(setDate, private_key=private_key)

    # deploy transaction to ganache
    tx_hash = w3.eth.send_raw_transaction(signed_setDate.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # setting seller and purchaser
    setPurchaser = agreement_contract.functions.setPurchaser(purchaser).build_transaction(
        {
            "chainId": chainId,
            "from": my_address,
            "nonce": nonce + 1,
        }
    )
    signed_setPurchaser = w3.eth.account.sign_transaction(setPurchaser, private_key=private_key)

    # deploy transaction to ganache
    tx_hash = w3.eth.send_raw_transaction(signed_setPurchaser.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
   
    # set seller
    setSeller = agreement_contract.functions.setSeller(seller).build_transaction(
        {
            "chainId": chainId,
            "from": my_address,
            "nonce": nonce + 1,
        }
    )
    signed_setSeller = w3.eth.account.sign_transaction(setSeller, private_key=private_key)

    # deploy transaction to ganache
    tx_hash = w3.eth.send_raw_transaction(signed_setSeller.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

