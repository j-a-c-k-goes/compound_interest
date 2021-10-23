'''
    most investments use a compound interest formula,
    which is more accurate than computing simple interest.
'''
def starting_amount():
	starting_amount = float(input('enter investment starting amount: '))
	return starting_amount
def investment_time():
	investment_time = float(input('enter time to invest (in years): '))
	return investment_time
def interest_rate():
	interest_rate = float(input('enter the interest rate (example: 3.75): '))
	interest_rate = interest_rate / 100
	return interest_rate
def monthly_contribution():
	monthly_contribution = float(input('enter monthly contribution to investment: '))
	return monthly_contribution
def print_comp_table():
	comp_table = '''
	periods for compunding interest
	365\tdaily
	180\tevery two days
	52\tweekly
	12\tmonthly
	6\tevery two months
	4\tquarterly
	2\tsemi annually
	1\tyearly	
	'''
	print(comp_table)
def comp_periods():
	comp_periods = [365,180,52,12,6,4,2,1]
	return comp_periods
def calc_compound_interest(starting_amount, investment_time, interest_rate, monthly_contribution, period):
	interest_rate = interest_rate / 100
	compounded_interest = starting_amount * (1 + (interest_rate/period)) ** (period*investment_time)
	# with monthly contribution PMT × (((1 + r/n)^(nt) - 1) / (r/n))
	compounded_interest = compounded_interest + monthly_contribution * (((1 + interest_rate/period)**(period*investment_time) - 1) / (interest_rate/period))
	compounded_interest = round(compounded_interest, 2)
	return compounded_interest
def print_compound_interest(starting_amount, investment_time, interest_rate, monthly_contribution, comp_periods):
	for period in comp_periods:
		if period == 365:
			p_engl = 'daily'
		elif period == 180:
			p_engl = 'twice a day'
		elif period == 52:
			p_engl = 'weekly'
		elif period == 12:
			p_engl = 'monthly'
		elif period== 6:
			p_engl = 'bimonthly'
		elif period == 4:
			p_engl = 'quarterly'
		elif period == 2:
			p_engl = 'semi annually'
		elif period == 1:
			p_engl = 'yearly'
		print()
		print(f'principal amount\t${starting_amount}')
		print(f'investment time\t\t{investment_time} years')
		print(f'monthly contribution\t${monthly_contribution}')
		print(f'interest rate\t\t{interest_rate * 100}%')
		print(f'compound rate\t\t{p_engl}')
		print(f'compounded interest\t${calc_compound_interest(starting_amount, investment_time, interest_rate, monthly_contribution, period)}')
		print(f'total contribution\t${monthly_contribution * 12 * investment_time}')
		print()
if __name__ == '__main__':
	starting_amount = starting_amount()
	investment_time = investment_time()
	interest_rate = interest_rate()
	monthly_contribution = monthly_contribution()
	comp_periods = comp_periods()
	print_comp_table()
	print_compound_interest(starting_amount, investment_time, interest_rate, monthly_contribution, comp_periods)