# Simulation of Property  Acquisition and Management in a Blockchain Network

Taking Property related daata from various sources by using Aadhar data as a primary authenticator and storing the proeprty transaction in pre-acquisition state that is "Agreement" and "Sale Deed", Also process after math of buying the property like changing the owner name in property tax, and other such documents.


## Features

- Prevent Double Selling
- Maintain interoperability
- Stored data in the form of smart contract
- Less transaction of the property


## Modules
### Aadhar DB (managed by uidai)
This database consist of the following data about a person which help in authentication.
- First Name
- Middle Name
- Last Name
- Date of Birth
- Gender
- Aadhar no. (12 digit)
- Address
- Photo

### SARATHI DB 
This is STAMP and Registration Assistance through online help information. This module is rersponsible for getting the data from the smart contract and registering the property with the help of the data stored in smart contract.

- calculate/receive the tax on buying and selling of the property
- get the seller and buyer data through aadhar DB
- show the agreement and sale deed term of transfer
- Resolve any proerty related issue/grievences while making the transaction through the smart contract.
- Can block/unblock the property to prevent frauds.

### Bank DB
This is the bank simulation, which lends money to the user by mortgaging the property and does the following task.
- Lends money to the user.
- And can able to see the property details with the consent of the user.
- User can make transaction while buying the property
- bank and store the transaction with ID,sender bank,amount.

### Police DB
This module handles if there is any police complaint related to the property. And send the complaint to the **SARATHI DB** so that it can temporary block the current owner of the proeprty to make any property transaction.

### Property Details
This is the modules  which has the total details of the property along with its tax related information.
- stores the property details
- banks,sarathi can get access to these details after user consent.

### Main portal
main module is the front-end to the user, where they can see the following details : 
- Aadhar card to get the registered property.
- Take loan on the property 
- Send the property details to the purchaser
- After getting the approval the buyer can make the agreement with purchaser
- If the agreement fails then the buyer and purchaser both can decide to drop the agreement.
- Make payment to buy the property.
- After successfull complition of the "Agreement" and buyer and purchaser can create the "Sale Deed" in the form of smart contract.
- After Agreement and sale Deed they can register their property to the **SARATHI DB** by providing the details of smart contract transactions, hence it will make paperless transction of property possible.
