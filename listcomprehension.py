#unoamil=[i for i in range(1,1001)]
#print (unoamil)

## Use for the questions below:
#1.Find all of the numbers from 1–1000 that are divisible by 8
nums = [i for i in range(1,1001)]
divisible8=[num for num in nums if num%8==0]
#print(divisible8)
#2.Find all of the numbers from 1–1000 that have a 6 in them
number6=[num for num in nums if "6" in str(num)]
#print(number6)
#3.Count the number of spaces in a string (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
spaces=len([i for i in string if i==" "])
print (spaces)
#4.Remove all of the vowels in a string (use string above)
remove="".join([i for i in string if i not in "aeiou"])
print (remove)
#5.Find all of the words in a string that are less than 5 letters (use string above)
words=string.split(" ")
print (words)
find=[i for i in words if len(i)<5]
print (find)
#6.Use a dictionary comprehension to count the length of each word in a sentence (use string above)
mydict={word: len(word) for word in words }
print (mydict)
#7.Use a nested list comprehension to find all of the numbers from 1–1000 
# that are divisible by any single digit besides 1 (2–9)
divisors= [num for num in nums if True in [True for divisor in range(2,10) if num % divisor == 0]]
#print (divisors)
#For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by
q8_answer = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}
print(q8_answer)
nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."