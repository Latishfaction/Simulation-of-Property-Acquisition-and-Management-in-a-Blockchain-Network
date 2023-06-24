# Simulation of Property  Acquisition and Management in a Blockchain Network

Taking Property related data from various sources by using Aadhar data as a primary authenticator and storing the property transaction in pre-acquisition state that is "Agreement" and "Sale Deed", Also process after-math of buying the property like changing the owner name in property tax, and other such documents.

## Features

- User sign-in
- Buy Property
    - Send buy request
    - Create Agreement
    - Publish Agreement
- Sell Property
- Use Aadhar Card as primary authenticator
- Integrated with 
    - Banks to get hassle-free loans on property
    - Tax Authority to get tax(tax-default/non-default) information on property.

Note : Data sources of banks,tax,aadhar data created by using "dummy data".No real-time data is being used in this simulation.



## Dependencies
- Ganache 2.7.0
- Python 3.10.10
    - Django 4.1.7
    - Web3.py 5.31.3
## Run the project

Clone the file and run the django project

```bash
  python manage.py runserver
```
### Default user credentials
| Aadhar Number  | Password |
| ------------- | ------------- |
| Latish (admin only)  | 123  |
| 838427959970  | 123  |
| 662223509284  | 123  |

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

## Figma Design Board
### [UI Design with figma](https://www.figma.com/file/lZrRiL7NdJ048PzcwIagQx/website-uiux?type=design&node-id=0-1&mode=design)

## Authors

- [@latishfaction](https://www.github.com/latishfaction)
- [Ankit Harjal]()
- [Akansha Shende]()
- [Neelam Thakur]()
