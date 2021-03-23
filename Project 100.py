class ATM(object):
    def _init_(user, atm, pin):
        user.atm = atm
        user.pin = pin

    def CashWithdrawal(user):
        print("Cash Successfully Withdrawed")

    def BalanceEnquiry(user):
        print("The amount of money in your bank account is : ")

    def CashDeposit(user):
        print("Cash Successfully Deposited")
        
