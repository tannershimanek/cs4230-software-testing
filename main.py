import config, copy
CONFIG = config.BANK_CONFIG

#Test commit by Natalina

def main():

    print("Hello World!")
    print(copy.copy(CONFIG.get('interest_rate')))


if __name__ == '__main__':
    main()
