#Pay Calculator

print 'Wage calculator'
sunday_hours = float(raw_input('Enter your hours worked on Sunday:'))
monday_hours = float(raw_input('Enter your hours worked on Monday:'))
tuesday_hours = float(raw_input('Enter your hours worked on Tuesday:'))
wednesday_hours = float(raw_input('Enter your hours worked on Wednesday:'))
thursday_hours = float(raw_input('Enter your hours worked on Thursday:'))
friday_hours = float(raw_input('Enter your hours worked on Friday:'))
saturday_hours = float(raw_input('Enter your hours worked on Saturday:'))
weekly_hours = [sunday_hours, monday_hours, tuesday_hours, wednesday_hours, thursday_hours, friday_hours, saturday_hours]
base_rate = float(raw_input('What is your payrate?'))
print weekly_hours
daily_method_wage = 0.0
weekly_method_wage = 0.0
#in the future I could add double time rules // holidays
#applying overtime to each day
for daily_hours in weekly_hours:
	if daily_hours > 8:
		overtime_hours = daily_hours - 8
		overtime_wage = overtime_hours * (1.5 * base_rate)
		daily_method_wage = daily_method_wage + overtime_wage + (base_rate * 8)
	elif daily_hours <= 8:
		daily_method_wage = daily_method_wage + (daily_hours * base_rate)
	else:
		print 'There is a problem with the code'
#applying overtime to the week
if sum(weekly_hours) > 44:
		weekly_overtime_hours = sum(weekly_hours) - 44
		weekly_overtime_wage = weekly_overtime_hours * (1.5 * base_rate)
		weekly_method_wage = (44 * base_rate) + weekly_overtime_wage

if weekly_method_wage > daily_method_wage:
	print weekly_method_wage
else:
	print daily_method_wage


closeInput = raw_input("Press ENTER to exit")
