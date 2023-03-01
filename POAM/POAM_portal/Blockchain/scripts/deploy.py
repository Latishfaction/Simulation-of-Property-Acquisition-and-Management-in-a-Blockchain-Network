from brownie import Agreement,SaleDeed

def get_account():
    if(network.show_active()=="ganache-local"):
        return accounts[1]
    else:
        accounts[0]

def deploy_Agreement():
    account = get_account()
    agreement_contract = Agreement.deploy({
        "from":account
    # print(ss)
    print(agreement_contract.)
    # getting the initial value

    # storing the value
    # transaction = ss.store(15,{
    #     "from":account
    })
    # #  waiting for block conformation
    # transaction.wait(1)
    # # getting the updated value
    # updated_val = ss.retrieve()
    # print(updated_val)


def main():

    deploy_Simple_storage()