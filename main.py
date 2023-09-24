import Commands
import config
CONFIG = config.BANK_CONFIG


user_commands = {
    "advance_month": ["advance_month", "Advance Month", "advance month"],
    "deposit_to_savings": ["deposit_to_savings", "Deposit to Savings", "deposit to savings"],
    "withdraw_from_savings": ["withdraw_from_savings", "Withdraw from Savings", "withdraw from savings"],
    "create_new_loan": ["create_new_loan", "Create New Loan", "create new loan"],
    "pay_loan": ["pay_loan", "Pay Loan", "pay loan"],
    "show_savings_balance": ["show_savings_balance", "Show Savings Balance", "show savings balance"],
    "show_loan": ["show_loan", "Show Loan", "show loan"],
    "show_all_loans": ["show_all_loans", "Show All Loans", "show all loans"],
    "generate_report": ["generate_report", "Generate Report", "generate report"],
    "help": ["help", "Help"],
}

# add a number to each array in user_commands
for key, value in user_commands.items():
    value.append(str(list(user_commands.keys()).index(key) + 1))

# todo: use the dict above to create commands

def driver():
    while True:
        command = input(
            "\nEnter your command (type 'help' for available commands): ").lower().strip()

        if command == "advance_month" or command == "1":
            cmd = Commands.AdvanceMonthCommand()
        elif command == "deposit_to_savings" or command == "2":
            amount = float(input("Enter amount to deposit: "))
            cmd = Commands.DepositToSavingsCommand(amount)
        elif command == "withdraw_from_savings" or command == "3":
            amount = float(input("Enter amount to withdraw: "))
            cmd = Commands.WithdrawFromSavingsCommand(amount)
        elif command == "create_new_loan" or command == "4":
            amount = float(input("Enter loan amount: "))
            # interest_rate = float(input("Enter interest rate: "))
            interest_rate = config.BANK_CONFIG.get('interest_rate')
            cmd = Commands.CreateNewLoanCommand(amount, interest_rate)
        elif command == "pay_loan" or command == "5":
            loan_id = int(input("Enter loan ID: "))
            amount = float(input("Enter amount to pay: "))
            cmd = Commands.PayLoanCommand(loan_id, amount)
        elif command == "show_savings_balance" or command == "6":
            cmd = Commands.ShowSavingsBalanceCommand()
        elif command == "show_loan" or command == "7":
            loan_id = int(input("Enter loan ID: "))
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
    print("\nWelcome to the WeCheatEm Bank System!")
    Commands.HelpCommand().execute()
    driver()


if __name__ == '__main__':
    main()
