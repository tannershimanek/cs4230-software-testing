# cs4230-software-testing

<br>

## Customer

- A customer is issued a user id by the system.
- A customer has one savings accuont at all times.
- A customer can initiate a new loan. (max 3)
- A customer can Deposit into savings any number of times each month.
- A customer can Withdraw from savings any number of times each month. The customer cannot withdraw more than the amount in savings.
- A customer can make a payment on a loan any number of times each month. The payment cannot be greater than the owed amount.
- A customer can generate a bank report any number of times each month.
- A customer can advance a month.
- When a month is advanced, a the system will generate a report.

*The above items can be done through commands, excluding user id generation.*


<br>

## System

### Commands
todo
1. Advance Month
2. Deposit to Savings
3. Withdraw from Savings
4. Create New Loan
5. Pay Loan
6. Show Savings Balance
7. Show Loan
8. Show All Loans
9. Generate Report
10. Help (shows a list of commands)
0. exit (exits program)



### Rounding
- 1 penny is equal to 0.01.
- The amount deposited to savings will be rounded down to the nearest penny.
- The amount withdrawn from savings will be rounded down to the nearst penny.
- The interest applied to a savings account will be rounded down to the nearest penny.
- The amount in savings will be rounded up to the nearest penny.
- The amount on a loan will be rounded up to the nearest penny.
- The amount paid to a loan will be rounded down to the nearest penny.
- The loan late fee will be rounded down to the nearest penny.
- The interest applied to a loan will be rounded up to the nearest penny.



### System Report
The system report includes: 
1. Savings account balance
2. Each loan with their amount owed and interest rate.
3. Transactions.
    - Transactions include savings deposits, savings withdrawls, loan interest added, savings interest added, and late fees.
    - Each transaction will state the month that it happened in.

```
--- Bank System Report ---

Savings Account:
Balance: $400.12

Loans:
Loan 1: $11964.34 at 0.12% interest rate
Loan 2: $11063.26 at 0.12% interest rate

Transactions:
Month 1: Deposited $500.0 to savings. New balance: $500.0
Month 1: Withdrew $100.0 from savings. New balance: $400.0
Month 2: Applied $50 late fee to loan 2. New balance: $11050.0
Month 2: Applied $14.34 interest to loan 1. New balance: $11964.34
Month 2: Applied $13.26 interest to loan 2. New balance: $11063.26
Month 2: Applied $0.12 interest to savings. New balance: $400.12
```

<br>

## Loans

- A loan id will be issued by the system.
- A customer can initiate a new loan. (max 3)
- A customer cannot loan less than $500.
- A cutsomer cannot loan more than $50_000.
- A customer can make a payment on a loan greater than or equal to the minumum amount.
- A customer can make any number of payments to a loan each month.
- A loan payment cannot be greater than the owed amount.
- If a customer fails to make a loan payment greater than or equal to the minimum payment before the month advances, they will receive a $50 late fee per loan. Even if the loan was created in the same month.
- The minimum loan payment is `due interest` + `1% of principal` + `$50 late fee (if assessed)` or $10. Whichever is greatest. (due interest is 12% of the current balance)
- A loan is automatically closed at the moment the balance is paid.
- The loan interest rate is a fixed 12% of the remaing balance issued monthly.
- Late fees and interest are added at the beginning of each month.
- Payment to a loan will be taken from savings.
- The loan payment cannot be greater than the amount in savings.


<br>

## Savings

- The savings balance cannot be negative.
- The user cannot withdraw or deposit an amount under 0.01.
- The customer can deposit any number of times each month.
- The customer can withdraw any number of times each month.
- The customer cannot withdraw more than the amount in savings.
- Savings interest is applied at the beginning of each month at 3%.