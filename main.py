import commands
import config
# import copy
# from loan import Loan
CONFIG = config.BANK_CONFIG


def driver():
    while True:
        command = input(
            "\nEnter your command (type 'help' for available commands): ").lower().strip()

        if command == "advance_month" or command == "1":
            cmd = commands.AdvanceMonthCommand()
        elif command == "deposit_to_savings" or command == "2":
            amount = float(input("Enter amount to deposit: "))
            cmd = commands.DepositToSavingsCommand(amount)
        elif command == "withdraw_from_savings" or command == "3":
            amount = float(input("Enter amount to withdraw: "))
            cmd = commands.WithdrawFromSavingsCommand(amount)
        elif command == "create_new_loan" or command == "4":
            amount = float(input("Enter loan amount: "))
            # interest_rate = float(input("Enter interest rate: "))
            interest_rate = config.BANK_CONFIG.get('interest_rate')
            cmd = commands.CreateNewLoanCommand(amount, interest_rate)
        elif command == "pay_loan" or command == "5":
            loan_id = int(input("Enter loan ID: "))
            amount = float(input("Enter amount to pay: "))
            cmd = commands.PayLoanCommand(loan_id, amount)
        elif command == "show_savings_balance" or command == "6":
            cmd = commands.ShowSavingsBalanceCommand()
        elif command == "show_loan" or command == "7":
            loan_id = int(input("Enter loan ID: "))
            cmd = commands.ShowLoanCommand(loan_id)
        elif command == "show_all_loans" or command == "8":
            cmd = commands.ShowAllLoansCommand()
        elif command == "generate_report" or command == "9":
            cmd = commands.GenerateReportCommand()
        elif command == "help" or command == "10":
            cmd = commands.HelpCommand()
        elif command == "exit" or command == "0":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid command. Type 'help' for available commands.")
            continue

        cmd.execute()


def main():
    print("\nWelcome to the WeCheatEm Bank System!")
    commands.HelpCommand().execute()
    driver()


if __name__ == '__main__':
    main()
