from threading import Thread, Lock
import threading

lock = Lock()


class BankAccount(Thread):
    state_2: object
    state_1: object

    def __init__(self, check, balance, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.check = check
        self.balance = balance

    def withdraw(self, state_1):
        with lock:
            self.state_1 = state_1
            self.balance -= self.state_1
            print(f'Withdrew {self.state_1}, new balance is {self.balance}')

    def deposit(self, state_2):
        with lock:
            self.state_2 = state_2
            self.balance += self.state_2
            print(f'Deposited {self.state_2}, new balance is {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)
        # account = BankAccount()


account = BankAccount('30101810907020000615', 1000)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
