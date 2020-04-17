my_list=[]
count=1
print('Creating the list')
while len(my_list)<7: #creating the list
    print('Enter the integer number',count,end='')
    a=input(':')
    try:
        val=int(a)
        my_list.append(val)
        count+=1
    except ValueError:
        try:
            val=float(a)
            print('You entered a float. ')
        except ValueError:
            print('You did not enter a number. ')
count_1=0
while count_1==0:
    print('Enter the number from the list you want to find its difference from the mid number',end='')
    x=input(':') 
    try:
        val=int(x)
        count_1+=1
    except ValueError :
        try:
            val=float(x)
            print('You entered a float. ')
        except ValueError :
            print('You did not enter a number. ')
def finddiff(a,array):#This function receives a number and a list.Then calculates the difference between mid number and received number.
    count=0 
    for i in range(7):
        if array[i]==a:
            diff=abs(a-array[3])
            count+=1
    if count==0:
        print('This number does not exist in the list ')
    else:
        print(diff,'is the difference of mid number and received number.')
finddiff(val,my_list)
        
            
        
    
  





       
