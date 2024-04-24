import threading
import random
import time

class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print(f"{self.name} is depositing ${amount}")
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"{self.name} is withdrawing ${amount}")
                self.balance -= amount
            else:
                print(f"{self.name} tried to withdraw ${amount} but insufficient funds")

def deposit_thread(account):
    for i in range(5):
        amount = random.randint(100, 500)
        account.deposit(amount)
        time.sleep(1)

def withdraw_thread(account, operations):
    for i in range(operations):
        amount = random.randint(50, 300)
        account.withdraw(amount)
        time.sleep(1)

if __name__ == "__main__":
    account = BankAccount("Glenn", 1000)

    deposit_worker = threading.Thread(target=deposit_thread, args=(account,))
    withdraw_worker = threading.Thread(target=withdraw_thread, args=(account,))

    deposit_worker.start()
    withdraw_worker.start()

    deposit_worker.join()
    withdraw_worker.join()

    print(f"Final account balance for {account.name}: ${account.balance}")
