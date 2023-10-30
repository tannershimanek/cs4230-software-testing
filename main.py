from Banking.BankSystem import BankSystem
import Banking.Commands as Commands
import config
CONFIG = config.BANK_CONFIG


def driver():
    """
    Driver for command loop, allows for interaction with bank commands.
    Prompts user for commands until the "exit" command is entered.
    """


    while True:
        command = input(
            "\nEnter the number associated with your command (type 'help' for available commands): ").lower().strip()

        if command == "advance_month" or command == "1":
            cmd = Commands.AdvanceMonthCommand()
        elif command == "deposit_to_savings" or command == "2":
            amount = BankSystem.validate_decimal_input("Enter amount to deposit (Up to $1,000,000): ")
            cmd = Commands.DepositToSavingsCommand(amount)
        elif command == "withdraw_from_savings" or command == "3":
            amount = BankSystem.validate_decimal_input("Enter amount to withdraw: ")
            cmd = Commands.WithdrawFromSavingsCommand(amount)
        elif command == "create_new_loan" or command == "4":
            amount = BankSystem.validate_decimal_input("Enter loan amount: ")
            interest_rate = config.BANK_CONFIG.get('interest_rate')
            cmd = Commands.CreateNewLoanCommand(amount, interest_rate)
        elif command == "pay_loan" or command == "5":
            loan_id = BankSystem.validate_int_input("Enter loan ID: ")
            if not BankSystem.loan_exists(loan_id):
                print("Invalid loan ID. Please enter a valid loan ID.")
                continue
            amount = BankSystem.validate_decimal_input("Enter amount to pay: ")
            cmd = Commands.PayLoanCommand(loan_id, amount)
        elif command == "show_savings_balance" or command == "6":
            cmd = Commands.ShowSavingsBalanceCommand()
        elif command == "show_loan" or command == "7":
            loan_id = int(input("Enter loan ID: "))
            if not BankSystem.loan_exists(loan_id):
                print("Invalid loan ID. Please enter a valid loan ID.")
                continue
            cmd = Commands.ShowLoanCommand(loan_id)
        elif command == "show_all_loans" or command == "8":
            cmd = Commands.ShowAllLoansCommand()
        elif command == "generate_report" or command == "9":
            cmd = Commands.GenerateReportCommand()
        elif command == "help" or command == "10":
            cmd = Commands.HelpCommand()
        elif command == "exit" or command == "0":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid command. Type 'help' for available Commands.")
            continue

        cmd.execute()


def main():
    """
    Entry point for bank system.
    Greet user, display commands, and start driver loop.

    """
    print("\nWelcome to the WeCheatEm Bank System!")
    Commands.HelpCommand().execute()
    driver()


if __name__ == '__main__':
    main()
