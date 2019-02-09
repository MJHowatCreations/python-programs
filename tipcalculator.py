bill = raw_input('Enter your bill amount:')
tip = raw_input('Enter your tip amount:')
bill = float(bill)
tip = float(tip)
tip = tip / 100.0
bill = bill * 1.05
tip = bill * tip
print 'Your bill with tax is:', bill
print 'Your tip is:', tip
total = bill + tip
print 'Your total is:', total

closeInput = raw_input("Press ENTER to exit")
print "Closing..."
