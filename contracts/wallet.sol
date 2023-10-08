// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Wallet {
    address public owner;

    event Deposit(address indexed from, uint256 amount);
    event Withdraw(address indexed to, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    receive() external payable {
        emit Deposit(msg.sender, msg.value);
    }

    function sendEther(address payable _recipient, uint256 _amount) public onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(address(this).balance >= _amount, "Insufficient balance");
        _recipient.transfer(_amount);
        emit Withdraw(_recipient, _amount);
    }

    function withdrawBalance() public onlyOwner {
        uint256 balanceToWithdraw = address(this).balance;
        require(balanceToWithdraw > 0, "No balance to withdraw");
        owner.transfer(balanceToWithdraw);
        emit Withdraw(owner, balanceToWithdraw);
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
