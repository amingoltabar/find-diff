my_list=[]
for i in range(7):
    a=float(input('Create your list.Enter the integer. '))
    while a!=int(a):
        a=float(input('You did not enter an integer.Enter the integer '))
    a=int(a)
    my_list.append(a)
x=int(input('Enter the number you want to find its difference from the mid number'))
def finddiff(a,array):#This function receives a number and a list.Then calculates the difference between mid number and received number.
    count=0 
    for i in range(7):
        if my_list[i]==a:
            diff=abs(a-my_list[3])
            count+=1
    diff=int(diff)
    if count==0:
        print('This number does not exist in the list ')
    else:
        print(diff,'is the difference of mid number and received number.')
finddiff(x,my_list)
        
            
        
    
  





       
