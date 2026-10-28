class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Le montant du dépôt doit être positif.")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Le montant du retrait doit être positif.")
        elif amount > self.balance:
            print("\nVotre solde est insuffisant pour effectuer cette opération.")
        else:
            self.balance -= amount

    def display_details(self):
        print("\n*** Compte bancaire ***")
        print(f"Nom : {self.account_holder}\nSolde : {self.balance}")


if __name__ == "__main__":
    compte = BankAccount("Paul")
    compte.deposit(2500)
    compte.withdraw(750)
    compte.withdraw(650)
    compte.withdraw(950)
    compte.withdraw(450)
    compte.display_details()