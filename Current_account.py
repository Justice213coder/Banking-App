from account import Account

class CurrentAccount(Account):
    def __init__(self, account_no, balance=0):
        super().__init__(account_no, balance, withdrawal_limit=2000)