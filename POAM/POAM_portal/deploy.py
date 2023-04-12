from solcx import compile_standard, install_solc
import json

with open("POAM\POAM_portal\property.sol", "r") as file:
    property_file = file.read()

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

with open("POAM\POAM_portal\compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["property.sol"]["Agreement"]["evm"]["bytecode"][
    "object"
]

# get abi
abi = json.loads(compiled_sol["contracts"]["property.sol"]["Agreement"]["metadata"])[
    "output"
]["abi"]
