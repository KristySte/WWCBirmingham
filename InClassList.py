def first_last_element(listOfNum):
	output=[]
	if(len(listOfNum)==0):
		print"list is empty. can't do anything"
	else:
		output.append(listOfNum[0])
		output.append(listOfNum[len(listOfNum)-1])

	for num in output:
		print num



def sleep_in(weekday, vacation):
  if vacation =='True':
  	print"True"
  	return True
  elif weekday =='False':
  	print"True"
  	return True
  else:
  	print"False"
  	return False


def check(a, b):
	if((a and b) or (not a and not b)):
		print"we are in trouble: true"
		return True
	else:
		print"we are not in trouble: False"
		return False
# list2=[1]
list1=[1,2,3,4,5,10]
first_last_element(list1)
# check(True, True)
# print"*****"
# check(False,False)
# print"*****"
# check(False,True)

# sleep_in('False','False')
# print"******"
# sleep_in('True','True')
# print"************"
# sleep_in('False','True')
# print"*******"
# sleep_in('True','False')
