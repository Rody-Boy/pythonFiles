class questions:
		def __init__(self):
			self.monday="\nIT 202 10 AM TO 12 PM\nIT 203 1:00 TO 3:00 PM\nIT 205 5:30 TO 7 PM"
			self.tuesday="\nIT201 7:30 TO 9:30 AM\nBIBLE 103 10:30 AM TO 12:00 PM\nPE 103 1:00TO 2:00 PM\nSTS 4:00 to 5:30 PM\n5:30 TO 7 PM"
			self.wednesday="IT 202 9 AM TO 12 PM\nIT 205 5:30 TO 7 PM"
			self.thursday="IT 201 7:30 to 10:30 AM\nBIBLE 103 10:30 AM TO 12:00 PM\nPE 103 1:00 TO 2:00 PM\nSTS 4:00 TO 5:30 PM\nIT204 5:30 TO 7:00 PM"
			self.friday="IT 203 1:00 TO 4:00 PM\nDALUMATFIL 5:30 TO 8:30 PM"
			self.saturday=None
			self.sunday=None
			
		def day(self,day):
			day.day=input('What is the day today? \n')
		
		
#main

qs=questions()
qs.day("")
while qs.day=='stop'or 'Stop':
	if qs.day()=='monday'or 'Monday':
		print("\nYour schedule for today are:")
		print(qs.monday)
	elif qs.day()=='tuesday'or 'Tuesday':
		print("\nYour schedule for today are:")
		print(qs.tuesday)
	elif qs.day()=='wednesday'or 'Wednesday':
		print("\nYour schedule for today are:")
		print(qs.wednesday)	
	elif qs.day()=='thursday'or 'Thursday':
		print("\nYour schedule for today are:")
		print(qs.thursday)
	elif qs.day()=='friday'or 'Friday':
		print("\nYour schedule for today are:")
		print(qs.friday)
	elif qs.day()=='saturday'or 'Saturday':
		print("\nYour schedule for today are:")
		print(qs.saturday)
	elif qs.day()=='sunday'or 'Sunday':
		print("\nYour schedule for today are:")
		print(qs.sunday)
	else:
		print('error')



	
	
	






