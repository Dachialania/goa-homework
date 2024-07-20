
for i in range(21):
  print(i)

3
num = int(input("please enter your desired number: "))

if num % 2 == 0:
   print("number is even")
else:
    print("number is odd")


for i in range(2,22,2):
   print(x)

5

sum = 0
for i in range(50,101):
  sum = sum + x

print(sum)




for i in range(0,55,5):
  print(x)

user1 = int(input("Enter the first number: "))
user2 = int(input("Enter the second number: "))


if user1 > user2:
    for i in range(user2 , user1):
        print(i)
elif user1 < user2:
   for i in range(user1, user2):
        print(i)
else:
    print("Both numbers are equal, no numbers to display in between.")


num = 1
for i in range(5,11):
    print(i)
    num *= i
print(num)



word = input("Enter a word: ") 
reversed_word = "" 

for i in range(len(word) - 1, -1, -1):
   reversed_word = reversed_word +  word[i] 

print(reversed_word)
