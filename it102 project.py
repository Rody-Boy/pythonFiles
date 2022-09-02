def greet():
	print('Otherwise, enjoy your day, and live your life in purpose\n')

def error_message():
	print ('You should answer (yes) or (no), Sir/Mam\n')
	

name=input('What is your name?\n')
age=int(input('What is your age\n'))

print('Welcome, and make sure your smiling while using this code ' + name)

print('Please do answer the questions with yes or no only... Thank you!')

is_ok=input('Are you feeling okay ' +  name +'?')

if is_ok=='yes':
	print('Congratulations you are one of the people that is blessed')
	greet()
elif is_ok== 'no':
	print('Nothing is impossible, the word itself says “I’m possible”! -- Audrey Hepburn')
	greet()
else:
	error_message()
	greet()
	
is_sleep=input('Are you sleeping more or less than you normally do ' + name + '?' )

if is_sleep=='yes':
	print('This are the common causes of that symptom: Mental health disorders. Anxiety disorders, such as post-traumatic stress disorder, may disrupt your sleep. Awakening too early can be a sign of depression, Medications, Medical conditions, Sleep-related disorders, Caffeine, nicotine and alcohol')
	greet()
	
elif is_sleep=='no':
	print('Congratulations, you are one of the blessed people who do not have any trouble sleeping')
	greet()
	
else:
	error_message()
	greet()
	
is_lonely=input('Are you having thoughts of your own death '+ name +'?')

if is_lonely=='yes':
	print(' Please talk to your friends, families, and loved ones about it and do not hide it from them, and please seek medical attention. Also, remember that life is precious, and should not be go to waste ' + name)
	
elif is_lonely=='no':
	print('Congratulations, may you continue to live your life as happily as you are spending it now, just keep smiling and move forward to the future ' + name)
	
else:
	error_message()
	greet()
	
	
print('Please consider why you started before, you decide to quit, a friendly reminder from truly yours..')