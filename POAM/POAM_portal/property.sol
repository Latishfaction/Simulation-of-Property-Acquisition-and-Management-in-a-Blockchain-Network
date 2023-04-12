// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.6.0 <=0.8.0;

// plot data structure
struct Plot {
    uint number;
    string area;
    string length;
    string width;
    string society_name;
    string society_rera_no;
    string plot_address;
    string north;
    string south;
    string east;
    string west;
}

// transaction data structure
struct payment {
    uint id;
    uint amount;
    string date;
}

contract Agreement {
    string public date;
    uint256 public purchaser;
    uint256 public seller;
    Plot public plot_details;
    uint256 public total_amount;
    uint256 public amount_till_paid;
    uint256 public remaining_balance_amount;
    // last execution date
    string public last_exe_date;
    // list of transaction done
    payment[] public payment_data;
    uint256 public witness_purchaser;
    uint256 public witness_seller;

    // date = "25-02-2023";
    function setDate(string memory _date) public {
        date = _date;
    }

    function setPurchaser(uint256 _purchaser) public {
        purchaser = _purchaser;
    }

    function setSeller(uint256 _seller) public {
        seller = _seller;
    }

    function setP_details() public {
        plot_details.number = 1;
        plot_details.area = "1000.00";
        plot_details.length = "500.00";
        plot_details.width = "500.00";
        plot_details.society_name = "Shreesai Housing Society";
        plot_details.society_rera_no = "002/B-56";
        plot_details
            .plot_address = "Plot no 43,Near Maha-Laxmi Market, Peace Road, Laxman Nagar, Nagpur-33";
        plot_details.north = "Other Plot";
        plot_details.south = "Road 11X20ft";
        plot_details.east = "Road 11X20ft";
        plot_details.west = "Other Plot";
    }

    function setPayments() public {
        // payment memory t1 = payment(1,400000,"27-02-2023");
        payment memory t1 = payment(1, 400000, "27-02-2023");
        payment memory t2 = payment(2, 500000, "28-02-2023");
        payment memory t3 = payment(3, 500000, "1-03-2023");

        payment_data.push(t1);
        payment_data.push(t2);
        payment_data.push(t3);
    }

    function set_total_Amt(uint256 _total_amount) public {
        total_amount = _total_amount;
    }

    function setamt_till_paid(uint256 _amount_till_paid) public {
        amount_till_paid = _amount_till_paid;
    }

    function set_remaining_bal() public {
        remaining_balance_amount = total_amount - amount_till_paid;
    }

    function setLast_exe_date(string memory _last_exe_date) public {
        last_exe_date = _last_exe_date;
    }

    function setWitness() public {
        witness_purchaser = 204970513456;
        witness_seller = 556623238790;
    }

    function setAgreement() public {
        // purchaser = 123412341234;
        // seller = 987698769876;
        // plot details
        // plot_details.number = 34432;
        // plot_details.area = "2000";
        // plot_details.length = "1000";
        // plot_details.width = "1000";
        // plot_details.society_name = "Shreesai Housing Society";
        // plot_details.society_rera_no = "123/CC/342B2";
        // plot_details.plot_address = "Plot no 43,Near Maha-Laxmi Market, Peace Road, Laxman Nagar, Nagpur-33";
        // plot_details.north = "Other plot";
        // plot_details.south = "Road 11X20ft";
        // plot_details.east = "Road 10X15 ft";
        // plot_details.west = "Other plot";
        //transactions
        // total_amount = 1500000;
        // amount_till_paid = 100000;
        // remaining_balance_amount = total_amount - amount_till_paid;
        // last_exe_date = "30-11-2023";
        // witness_purchaser = 334455667788;
        // witness_seller = 776644331155;
    }

    // getter
    function getDate() public view returns (string memory) {
        return date;
    }

    function getPurchaser() public view returns (uint256) {
        return purchaser;
    }

    function getSeller() public view returns (uint256 _seller) {
        return seller;
    }

    function getP_details() public view returns (Plot memory) {
        return plot_details;
    }

    function GetPayment() public view returns (payment[] memory) {
        return payment_data;
    }

    function get_total_Amt() public view returns (uint256) {
        return total_amount;
    }

    function getamt_till_paid() public view returns (uint256) {
        return amount_till_paid;
    }

    function get_remaining_bal() public view returns (uint256) {
        return remaining_balance_amount;
    }

    function getLast_exe_date() public view returns (string memory) {
        return last_exe_date;
    }

    function getWitness_seller() public view returns (uint256) {
        return witness_seller;
    }

    function getWitness_purchaser() public view returns (uint256) {
        return witness_purchaser;
    }
}

contract SaleDeed {
    // agreement structure
    struct Agreement_data {
        address agreement_address;
        string date;
    }

    string public date;
    uint256 public purchaser;
    uint256 public seller;
    Plot public plot_details;
    uint256 public total_amount;
    Agreement_data public Agreement_details;
    // list of transaction done
    payment[] public payment_data;
    uint256 public witness_purchaser;
    uint256 public witness_seller;

    function setDate() public {
        date = "10-02-2001";
    }

    function setPurchaser() public {
        purchaser = 662223509284;
    }

    function setSeller() public {
        seller = 662223509284;
    }

    function setP_details() public {
        plot_details.number = 1;
        plot_details.area = "1000.00";
        plot_details.length = "500.00";
        plot_details.width = "500.00";
        plot_details.society_name = "Shreesai Housing Society";
        plot_details.society_rera_no = "002/B-56";
        plot_details
            .plot_address = "Plot no 43,Near Maha-Laxmi Market, Peace Road, Laxman Nagar, Nagpur-33";
        plot_details.north = "Other Plot";
        plot_details.south = "Road 11X20ft";
        plot_details.east = "Road 11X20ft";
        plot_details.west = "Other Plot";
    }

    function set_total_Amt() public {
        total_amount = 1400000;
    }

    function set_agreement() public {
        Agreement_details
            .agreement_address = 0x975C2f9CC74Df635770339eF2a168529b993CC17;
        Agreement_details.date = "02-03-2023";
    }

    function setPayments() public {
        // payment memory t1 = payment(1,400000,"27-02-2023");
        payment memory t1 = payment(1, 400000, "27-02-2023");
        payment memory t2 = payment(2, 500000, "28-02-2023");
        payment memory t3 = payment(3, 500000, "1-03-2023");

        payment_data.push(t1);
        payment_data.push(t2);
        payment_data.push(t3);
    }

    function setWitness() public {
        witness_purchaser = 204970513456;
        witness_seller = 556623238790;
    }

    // getter
    function getDate() public view returns (string memory) {
        return date;
    }

    function getPurchaser() public view returns (uint256) {
        return purchaser;
    }

    function getSeller() public view returns (uint256 _seller) {
        return seller;
    }

    function getP_details() public view returns (Plot memory) {
        return plot_details;
    }

    function get_total_Amt() public view returns (uint256) {
        return total_amount;
    }

    function get_agreement() public view returns (Agreement_data memory) {
        return Agreement_details;
    }
}
