print (" hello world")

x = 2
print (x) # prints x as int type 
print (float(x)) # prints x as float 

b= "first task"
print(len(b)) # prints length of b variable (10)

print("task" in b) # checks if word "task" is in given string b 
print("python" not in b) # checks if word "python" isn't in given string b

# string modifications 

print(b.upper()) #prints b variable's value in upper cases 
print(b.lower()) #prints b variable's value in lower cases
print(b.replace("first" , "second")) # changes word "first" to "second"
print(b.split("_")) # splits string with _

# concatenation 

a= "run"
print (a + " " + b) #prints a and b string values 

# f-strings 

m=f"first task for {x}"
print(m) #prints string and int type value 

# lists 

mylist = [1,2,3,4,5,6]

mylist[3]=0 # changes value 4 to 0

mylist.append(7) #adds 7 as another list value 
mylist.insert(0, 0) #inserts 0 as first list value
mylist.remove(5)
print(mylist[-3]) #prints third value from end
print(mylist[1:3]) # prints in range (2 and 3)
print(len(mylist)) # prints length of given list


#if...elif... else 

n=2 
z=9 
if n > z:
   print(" n is more than z")
elif n==z:
   print("n is equal to z")
else :
   print("n is less than z ") # else is very last statement otherwise if you have other condintions before else you write elif

#while 

while n < z:
   print(n) 
   n+=1 
   if n == 6:
      break # when n is 6 while loop stops 
    
      
#for loop

secondList = ["erti ", "ori", "sami", "otxi", "xuti"]

for i in secondList :
   if i == "ori" :
      continue # when i gets value of "ori" it jumps to next value
      print(i) 

for i in range(12) :
     print(i)
