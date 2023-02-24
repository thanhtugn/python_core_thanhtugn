class Wallet:
    def __init__(self, init_amount=0):
        self.balance = init_amount
        
    def spend_cash(self, amount):
        if self.balance < amount:
            raise Exception("Not enough money to spend")
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
        
            
