import config, copy
from loan import Loan
CONFIG = config.BANK_CONFIG

def main():

    print("Hello World!")
    print(copy.copy(CONFIG.get('interest_rate')))

    loan = Loan(101, 1000)
    print(loan)


if __name__ == '__main__':
    main()
