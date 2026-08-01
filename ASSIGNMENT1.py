#ASSIGNMENT 1

#LEVEL 1

#Q1:- Write a program to input marks in five subjects and calculate the total, percentage, and grade.

'''marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)'''

#Q2:-Write a program to determine whether a given year is a leap year.

'''year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")'''
    
#Q3:-Write a program to find the largest and second largest among three numbers.

'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

numbers = [a, b, c]
numbers.sort()

print("Largest:", numbers[-1])
print("Second Largest:", numbers[-2])'''

#Q4:-Write a program to calculate an electricity bill based on slab rates.

'''units = int(input("Enter units consumed: "))

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Electricity Bill = ₹", bill)'''

#Q5:-Write a program to check whether a number is an Armstrong number

'''num = int(input("Enter a number: "))

power = len(str(num))
temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit ** power
    temp //= 10

if sum_digits == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")'''
    
#Q6:- Input a string and print the first 3 characters, last 3 characters, every alternate character, and the reversed string.

'''text = input("Enter a string: ")

print("First 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Alternate characters:", text[::2])
print("Reversed string:", text[::-1])'''

#Q7:- Count the number of vowels, consonants, digits, and special characters in a string.

'''text = input("Enter a string: ")

vowels = consonants = digits = special = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)'''

#Q8:- Check whether a string is a palindrome using slicing.

'''text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")'''
    
#Q9:-Find the frequency of each character in a string

'''text = input("Enter a string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for key, value in freq.items():
    print(key, ":", value)'''
    
#Q10:-Remove all spaces from a string and count the number of words.

'''text = input("Enter a sentence: ")

no_spaces = text.replace(" ", "")
word_count = len(text.split())

print("String without spaces:", no_spaces)
print("Number of words:", word_count)'''

#Q11:- Print all prime numbers between 1 and N

'''n = int(input("Enter N: "))

print("Prime numbers:")

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")'''
        
#Q12:-Generate the Fibonacci sequence up to N terms using loops.

'''n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b'''
    
#Q13:-Find all factors of a given number.

'''num = int(input("Enter a number: "))

print("Factors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")'''
        
#Q14:- Check whether a number is a Perfect Number

'''num = int(input("Enter a number: "))

sum_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")'''
    
#Q15:-Print Floyd's Triangle up to N rows

'''n = int(input("Enter number of rows: "))

num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()'''
    
#Q16:- Find the largest, smallest, and average value in a list

'''numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)

print("Largest:", largest)
print("Smallest:", smallest)
print("Average:", average)'''

#Q17:-Remove duplicate elements from a list while maintaining the original order.

'''numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List after removing duplicates:")
print(result)'''

#Q18:-Find the second largest and second smallest element in a list.

'''numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second Smallest:", unique_numbers[1])
print("Second Largest:", unique_numbers[-2])'''

#Q19:-Separate even and odd numbers from a list into two different lists

'''numbers = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even Numbers:", even)
print("Odd Numbers:", odd)'''

#Q20:-Rotate a list by K positions to the left

'''numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter K: "))

k = k % len(numbers)

rotated = numbers[k:] + numbers[:k]

print("Rotated List:")
print(rotated)'''

#LEVEL 2
#Q1:-Create a list of squares of numbers from 1 to 50 using list comprehension

'''squares = [x**2 for x in range(1, 51)]

print(squares)'''

#Q2:- Generate a list containing only prime numbers between 1 and 100 using list comprehension.

'''primes = [
    num
    for num in range(2, 101)
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
]

print(primes)'''

#Q3:-Convert a list of strings into uppercase using list comprehension

'''words = ["python", "java", "c++", "javascript"]

uppercase_words = [word.upper() for word in words]

print(uppercase_words)'''

#Q4:-Create a list containing the lengths of each word in a sentence.

'''sentence = input("Enter a sentence: ")

lengths = [len(word) for word in sentence.split()]

print(lengths)'''

#Q5:- Remove empty strings and strings containing only spaces from a list using list comprehension

'''items = ["Python", "", "   ", "Java", "C++", " ", "JavaScript"]

cleaned = [item for item in items if item.strip()]

print(cleaned)'''

#Q6:-Write a function to check whether a number is prime.

'''def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")'''
    
#Q7:-Write a function to calculate the GCD of two numbers.

'''def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD =", gcd(num1, num2))'''

#Q8:-Write a function that returns the second largest element of a list.

'''def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]


numbers = list(map(int, input("Enter numbers: ").split()))

print("Second Largest:", second_largest(numbers))'''

#Q9:-Write a function that accepts a sentence and returns the longest word.

'''def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)


text = input("Enter a sentence: ")

print("Longest Word:", longest_word(text))'''

#Q10:- Write a function that merges two lists and removes duplicate elements.

'''def merge_lists(list1, list2):
    merged = []

    for item in list1 + list2:
        if item not in merged:
            merged.append(item)

    return merged


list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

print("Merged List:", merge_lists(list1, list2))'''

#Q11:-Find the common elements between two lists without using sets.

'''list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common Elements:", common)'''

#Q12:-Find the missing number from a list containing numbers from 1 to N.

'''numbers = list(map(int, input("Enter numbers: ").split()))

n = len(numbers) + 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing = expected_sum - actual_sum

print("Missing Number:", missing)'''

#Q13:-Find the frequency of every element in a list.

'''numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

for key, value in frequency.items():
    print(key, ":", value)'''
    
#Q14:-Sort a list in ascending order without using the sort() method

'''numbers = list(map(int, input("Enter numbers: ").split()))

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted List:", numbers)'''

#Q15:-Print a diamond star pattern.

'''n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))'''
    
#Q16:- Write a program to safely divide two numbers using exception handling

'''try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")'''
    
#Q17:-Accept integer input until a valid integer is entered using try-except

'''while True:
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
        break

    except ValueError:
        print("Invalid input. Please enter an integer.")'''
        
#Q18:-Handle IndexError while accessing list elements

'''numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Please enter a valid integer index.")'''
    
#Q19:-Handle FileNotFoundError while opening a file

'''try:
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: File not found.")'''
    
#Q20:-Build a menu-driven calculator that handles invalid inputs and division by zero using try-except

'''while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Exiting...")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", num1 + num2)

        elif choice == 2:
            print("Result =", num1 - num2)

        elif choice == 3:
            print("Result =", num1 * num2)

        elif choice == 4:
            print("Result =", num1 / num2)

        else:
            print("Invalid choice.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter valid numeric values.")'''
        
#LEVEL 3
#Q1:- Find the factorial of a number using recursion

'''def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


num = int(input("Enter a number: "))

print("Factorial =", factorial(num))'''

#Q2:-Generate the Fibonacci sequence using recursion.

'''def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter number of terms: "))

for i in range(terms):
    print(fibonacci(i), end=" ")'''
    
#Q3:-Find the sum of digits of a number using recursion.

'''def sum_digits(n):
    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)


num = int(input("Enter a number: "))

print("Sum of Digits =", sum_digits(num))'''

#Q4:-Reverse a string using recursion.

'''def reverse_string(text):
    if len(text) == 0:
        return text

    return reverse_string(text[1:]) + text[0]


text = input("Enter a string: ")

print("Reversed String:", reverse_string(text))'''

#Q5:-Solve the Tower of Hanoi problem using recursion.

'''def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print(f"Move disk {n} from {source} to {destination}")

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

tower_of_hanoi(n, 'A', 'B', 'C')'''

#Q6:-Write a recursive function to determine whether a string is a palindrome

'''def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")'''
    
#Q7:-Use list comprehension and a helper function to create a list containing only prime numbers

'''def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


primes = [num for num in range(1, 101) if is_prime(num)]

print(primes)'''

#Q8:-Read numbers until 'stop' is entered, handle invalid inputs using try-except, then calculate minimum, maximum, average, and median.

'''numbers = []

while True:
    value = input("Enter a number (or 'stop'): ")

    if value.lower() == "stop":
        break

    try:
        numbers.append(float(value))

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if len(numbers) == 0:
    print("No numbers entered.")

else:
    numbers.sort()

    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    n = len(numbers)

    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]

    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", average)
    print("Median:", median)'''
    
#Q9:-Write a recursive function to flatten a nested list.

'''def flatten(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


nested_list = [1, [2, [3, 4], 5], [6, 7], 8]

flat_list = flatten(nested_list)

print(flat_list)'''

#Q10:-Create a Student Record Management System using functions, lists, loops, list comprehensions, exception handling, and file handling.

'''students = []


def add_student():
    try:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students.append({
            "roll": roll,
            "name": name,
            "marks": marks
        })

        print("Student Added Successfully!")

    except ValueError:
        print("Invalid Input!")


def view_students():
    if not students:
        print("No Records Found.")
        return

    print("\nStudent Records")
    print("-" * 30)

    for student in students:
        print(
            student["roll"],
            student["name"],
            student["marks"]
        )


def search_student():
    try:
        roll = int(input("Enter Roll No to Search: "))

        found = False

        for student in students:
            if student["roll"] == roll:
                print(student)
                found = True
                break

        if not found:
            print("Student Not Found.")

    except ValueError:
        print("Invalid Roll Number!")


def save_to_file():
    try:
        with open("students.txt", "w") as file:
            for student in students:
                file.write(
                    f"{student['roll']},{student['name']},{student['marks']}\n"
                )

        print("Data Saved Successfully!")

    except Exception as e:
        print("Error:", e)


def load_from_file():
    try:
        with open("students.txt", "r") as file:
            students.clear()

            for line in file:
                roll, name, marks = line.strip().split(",")

                students.append({
                    "roll": int(roll),
                    "name": name,
                    "marks": float(marks)
                })

        print("Data Loaded Successfully!")

    except FileNotFoundError:
        print("File Not Found.")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Save to File")
    print("5. Load from File")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        save_to_file()

    elif choice == "5":
        load_from_file()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")'''
        

