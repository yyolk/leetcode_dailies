# https://leetcode.com/problems/simple-bank-system/


class Bank:
    """2043. Simple Bank System

    You have been tasked with writing a program for a popular bank that will
    automate all its incoming transactions (transfer, deposit, and withdraw).
    The bank has n accounts numbered from 1 to n. The initial balance of each
    account is stored in a 0-indexed integer array balance, with the (i + 1)th
    account having an initial balance of balance[i].

    Execute all the valid transactions. A transaction is valid if:

    The given account number(s) are between 1 and n, and
    The amount of money withdrawn or transferred from is less than or equal to
    the balance of the account.
    Implement the Bank class:

    Bank(long[] balance) Initializes the object with the 0-indexed integer array
    balance.
    boolean transfer(int account1, int account2, long money) Transfers money
    dollars from the account numbered account1 to the account numbered account2.
    Return true if the transaction was successful, false otherwise.
    boolean deposit(int account, long money) Deposit money dollars into the
    account numbered account. Return true if the transaction was successful,
    false otherwise.
    boolean withdraw(int account, long money) Withdraw money dollars from the
    account numbered account. Return true if the transaction was successful,
    false otherwise.
    """

    def __init__(self, balance: list[int]):
        # Store the balances; accounts are 1-indexed, list is 0-indexed
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Determine the number of accounts
        n = len(self.balance)
        # Check if both accounts are valid (1 to n)
        if not (1 <= account1 <= n and 1 <= account2 <= n):
            return False
        # Check if account1 has sufficient balance for transfer
        if self.balance[account1 - 1] >= money:
            # Deduct from account1
            self.balance[account1 - 1] -= money
            # Add to account2
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        # Determine the number of accounts
        n = len(self.balance)
        # Check if account is valid (1 to n)
        if not (1 <= account <= n):
            return False
        # Add money to the account
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Determine the number of accounts
        n = len(self.balance)
        # Check if account is valid (1 to n)
        if not (1 <= account <= n):
            return False
        # Check if account has sufficient balance for withdrawal
        if self.balance[account - 1] >= money:
            # Deduct money from the account
            self.balance[account - 1] -= money
            return True
        return False
