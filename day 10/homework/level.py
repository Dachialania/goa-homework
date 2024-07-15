
# 1. გამოიტანეთ რიცხვები 0-დან 20-ის ჩათვლით.
print("Numbers from 0 to 20:")
for i in range(21):
    print(i)

# 2. მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ ლუწია თუ არა.
user_input = int(input("Enter a number: "))
if user_input % 2 == 0:
    print(f"{user_input} is even")
else:
    print(f"{user_input} is odd")


# 3. დაპრინტეთ 20-მდე ლუწი რიცხვები.
print("Even numbers up to 20:")
for i in range(21):
    if i % 2 == 0:
        print(i)


# 4. 50-იდან 100-ის ჩათვლით არსებული ყველა რიცხვი დააჯამეთ for ციკლის გამოყენებით.
sum = 0
for i in range(50, 101):
    sum += i
print(f"Sum of numbers from 50 to 100 is: {sum}")


# 6. დაბეჭდეთ 5-ის ჯერადი რიცხვები 1-დან 50-ის ჩათვლით.
print("Multiples of 5 from 1 to 50:")
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

# 6. დაბეჭდეთ 5-ის ჯერადი რიცხვები 1-დან 50-ის ჩათვლით.
print("Multiples of 5 from 1 to 50:")
for i in range(1, 51):
    if i % 5 == 0:
        print(i)


# მომხმარებელს შემოატანინეთ ორი რიცხვი
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# შეამოწმეთ რომელია უდიდესი
if num1 < num2:
    smaller = num1
    larger = num2
else:
    smaller = num2
    larger = num1

# for ციკლის გამოყენებით უმცირესიდან უდიდესამდე დაპრინტეთ ყველა რიცხვი
print(f"Numbers from {smaller} to {larger}:")
for i in range(smaller, larger + 1):
    print(i)


print("Numbers from 0 to 20:")
for i in range(21):
    print(i)


# ნამრავლი ინიციალიზაცია
product = 1

# for ციკლის გამოყენებით 5-იდან 10-ის ჩათვლით რიცხვების ნამრავლის გამოთვლა
for i in range(5, 11):
    product *= i

# ნამრავლის დაბეჭდვა
print(f"The product of numbers from 5 to 10 is: {product}")


# შემოატანინეთ მომხმარებელს სიტყვა
word = input("Enter a word: ")

# საპირისპირო მიმართულებით დაბეჭდვა for ციკლის გამოყენებით
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word

print(f"The word '{word}' reversed is '{reversed_word}'")



