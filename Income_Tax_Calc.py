data_entry = False
working_days = 260
tax_brackets = [1, 0.8, 0.6, 0.55]


while data_entry == False:
	salary_type = input('Monthly(m)/Yearly(y)/Daily(d) salary: ')
	print()
	if salary_type == 'm':
		salary_entry = int(input('Enter monthly salary: '))
		data_entry = True
		salary = int(salary_entry * 12)
	elif salary_type == 'y':
		salary_entry = int(input('Enter yearly salary: '))
		data_entry = True
		salary = int(salary_entry)
	elif salary_type == 'd':
		salary_entry = int(input('Enter daily salary: '))
		data_entry = True
		salary = int(salary_entry * working_days)
	else:
		data_entry = False
		print('Incorrect entry, m/y/d')

print()
income = 0
tax = 0
i = 0
tax_amount = [(1 - tax_brackets[0]),
(1 - tax_brackets[1]),
(1 - tax_brackets[2]),
(1 - tax_brackets[3])]

for i in range(salary):
	if i <= 11850:
		income = income + tax_brackets[0]
		tax = tax + tax_amount[0]
		
	if i > 11850 and i <= 46350:
		income = income + tax_brackets[1]
		tax = tax + tax_amount[1]
	
	if i > 46350 and i <= 150000:
		income = income + tax_brackets[2]
		tax = tax + tax_amount[2]
	
	if i > 150000:
		income = income + tax_brackets[3]
		tax = tax + tax_amount[3]

per_year = int(income)
per_month = int(income / 12)
per_day = int(income / 260)
per_hr = per_day / 8        

print('Total Tax paid per year: ' + str(tax))
print()
print('Total earnings per year: ' + str(per_year))
print('Total earnings per month: ' + str(per_month))
print('Total earnings per day: ' + str(per_day))
print('Total earnings per hour: ' + str(per_hr))
input()

