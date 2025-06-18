# Question 1 : Write a function that counts the number of times a specific word appears in a given string.
#              Example: count how many times "Emma" appears in "Emma is a good developer. Emma is a writer".

# The following solution is based on compartmentalizing the words of the string into an array and then counting
def count_wrd_freq(string, word):
    for ch in ['.', '?', ',', '!', ';', ':']:
        string = string.replace(ch, '')
    words = string.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count


# Question 2 : Write a program that takes a list of numbers and prints only those divisible by 5.
def nums_divisible_by_5(nums):
    return [i for i in nums if i % 5 == 0]
