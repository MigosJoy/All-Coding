## Intro to CS and Python - MIT - Unit 1 - Probem Set 1 - Problem 1
s = str(input("Enter a string: "))
vowels = 0
for letter in s:
    if letter == 'i' or letter == 'u' or letter == 'e' or letter == 'o' or letter == 'a':
        vowels += 1
print("Number of vowels: " + str(vowels))

## Intro to CS and Python - MIT - Unit 1 - Probem Set 1 - Problem 2
s = "azcbobobegghakl"
bob_count = 0 
for i in range(len(s)):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        bob_count += 1
print("Number of times bob occurs is: " + str(bob_count))

## Intro to CS and Python - MIT - Unit 1 - Probem Set 1 - Problem 3
s = "azcbobobegghakl"
letter_holder = ""
longest_string = ""
for i in range(len(s)):
   if i == 0 or s[i] >= s[i-1]:
       letter_holder += s[i]
       if len(letter_holder) > len(longest_string):
            longest_string = letter_holder
   else:
        letter_holder = s[i]  
print(longest_string)

##End of file
