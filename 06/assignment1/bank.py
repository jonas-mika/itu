#################
# Mandatory Assignment 1 - IDSP
#################

# Assignment: 	Hypothetical Bank functionalities within Python 
# Author: 		Jonas-Mika Senghaas
# Date: 		09. September 2020
# TA:			Simon Martin Breum

import math

def calculate_balance(transactions):
	sum_transactions = 0 

	for transaction in transactions:
		sum_transactions += transaction

	return sum_transactions

def calculate_compound(account_balance, rate, years):
	for i in range(years):
		account_balance = account_balance * (1+ rate)

	return account_balance

def filter_withdrawals(transactions):
	withdrawals = []

	for transaction in transactions:
		if transaction < 0:
			withdrawals.append(transaction)

	return withdrawals

def risk_analysis(transactions):
	if len(transactions) == 0:
		print ("No transactions have been made!")
	min_transaction = 0

	for transaction in transactions:
		if transaction < min_transaction:
			min_transaction = transaction

	return min_transaction

def join_records(names, transactions):
	joined_transactions = []

	for i in range (len(names)):
		joined_transactions.append((names[i], transactions[i]))
		
	return joined_transactions

def unique_deposit_names(joined_transactions):
	deposited_accounts = []
	unique_names = []

	for person in joined_transactions:
		if person[1] > 0:
			deposited_accounts.append(person)

	for person in deposited_accounts:
		if person[0].lower() not in unique_names:
			unique_names.append(person[0])

	return unique_names

def main():
	#calculate balance example
	transactions = [100 , 5000 , -30, -1200]
	balance = calculate_balance(transactions)
	print(balance) #Expected output: 3870

	#calculate compound example
	compound_balance = calculate_compound(500 , 0.05 , 25)
	print(compound_balance) #Expected outuput: 1693.17[...]

	#filter withdrawals example
	withdrawals = filter_withdrawals(transactions)
	print(withdrawals) #Expected outuput: [-30, -1200]

	#risk analysis example 
	transactions = [-5000, 200, 120, -99999] 
	risk = risk_analysis(transactions)
	print(risk)#Expected outuput: -99999

	#join records example
	names = ['Muhammed', 'emma', 'Emma', 'julie']
	joined_transactions = join_records(names, transactions)
	print(joined_transactions)#Expected outuput: [( ’Muhammed’ , −5000), ( ’emma’ , 200), ( ’Emma’ , 120), ( ’ julie ’ , −99999)]

	#unique deposit names example
	unique_names = unique_deposit_names(joined_transactions)
	print(unique_names) #Expected outuput: ['emma']


if __name__ == "__main__":
	# execute only if run as a script
	main()
	#Expected output:
	#3870
	#1693.17[...]
	#-99999
	#[( ’Muhammed’ , −5000), ( ’emma’ , 200), ( ’Emma’ , 120), ( ’ julie ’ , −99999)]
	#['emma']

