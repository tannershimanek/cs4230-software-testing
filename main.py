import config, copy
CONFIG = config.BANK_CONFIG


def main():

    print("Hello World!")
    print(copy.copy(CONFIG.get('interest_rate')))


if __name__ == '__main__':
    main()
