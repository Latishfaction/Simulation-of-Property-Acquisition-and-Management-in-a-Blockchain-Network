from brownie import Agreement,SaleDeed,network,accounts
import datetime
import Getdetails as gd

# plot = Plot.objects.get(owner = p1)
def get_account():
    if(network.show_active()=="ganache-local"):
        return accounts[1]
    else:
        return accounts[0]

def deploy_Agreement():
    account = accounts[1]
    agreement_contract = Agreement.deploy({"from":account})
    # setAgreement(agreement_contract,account)
    # getAgreement(agreement_contract,account)
    t1 = agreement_contract.setDate("23-03-2023",{"from":account})
    agreement_contract.setPurchaser(838427959970,{"from":account})
    agreement_contract.setSeller(662223509284,{"from":account})
    agreement_contract.setP_details({"from":account})
    agreement_contract.setPayments({"from":account})
    agreement_contract.set_total_Amt(1400000,{"from":account})
    agreement_contract.setamt_till_paid(300000,{"from":account})
    agreement_contract.set_remaining_bal({"from":account})
    agreement_contract.setLast_exe_date("24-09-2023",{"from":account})
    agreement_contract.setWitness({"from":account})
    t1.wait(1)

    date= agreement_contract.getDate()
    purchaser = agreement_contract.getPurchaser()
    seller = agreement_contract.getSeller()
    p = agreement_contract.getP_details()
    total_amt = agreement_contract.get_total_Amt()
    till_paid = agreement_contract.getamt_till_paid()
    remaining_bal = agreement_contract.get_remaining_bal()
    last_exe_date = agreement_contract.getLast_exe_date()
    s_witness = agreement_contract.getWitness_seller()
    p_witness = agreement_contract.getWitness_purchaser()
    
    print("***Getting Details****")
    print("Date : ",date)
    print("Purchase :",purchaser)
    print("Seller : ",seller)
    print("Plot number : ",p[0])
    print("Plot Area : ",p[1])
    print("Plot Area Length : ",p[2])
    print("Plot Area Width : ",p[3])
    print("Society Name : ",p[4])
    print("Society Rera Number",p[5])
    print("Plot Direction : ")
    print("North : ",p[6])
    print("South : ",p[7])
    print("East : ",p[8])
    print("West : ",p[9])
    print("***Contract Call Execution Successful****")
    # getting the initial value

    # storing the value
    # transaction = ss.store(15,{
    #     "from":account
    # #  waiting for block conformation
    # transaction.wait(1)
    # # getting the updated value
    # updated_val = ss.retrieve()
    # print(updated_val)


def main():
    print("****deploying contract****")
    deploy_Agreement()