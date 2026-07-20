# 1.Write a Python script that takes a string input from the user and 
# prints a dictionary showing how many times each character appears in the string.

string=input("Enter name = ")

count={}
for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

# 2.Create a program that reads a short review (multi-line string) about your 
# favorite food delivery app (like Zomato or Swiggy) and counts the frequency of 
# each word, displaying the results as a dictionary.<br><br><em><strong>Hint:</strong> 
# Convert all words to lowercase and remove punctuation for accurate counting.</em>

review=input("Enter Review = ")

review=review.lower()

words=review.split()

count={}
for i in words:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

# 3.Given the following string: 'Virat scored 100, Rohit scored 80, and Gill scored 50 in 
# the IPL match', write a function word_freq_dict(text) that returns a dictionary with the frequency of each word.

def word_freq_dict(text):

    text = text.lower()
    text = text.replace(",", "")

    words = text.split()
    ans={}

    for i in words:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1
    return ans

text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"
print(word_freq_dict(text))

# 4.Modify your word frequency program to ignore common stopwords like 'the', 'and', 'in', 
# 'of', 'a', 'to', 'is' when counting word frequencies.<br><br><em><strong>Constraint:</strong> 
# Use a list of stopwords and filter them out before counting.</em>

def word_freq(text):

    text = text.lower()
    text = text.replace(",", "")

    words = text.split()
    stopwords = ["the", "and", "in", "of", "a", "to", "is"]
    ans= {}
    for i in words:
        if i not in stopwords:
            if i in ans:
                ans[i]+= 1
            else:
                ans[i]=1
    return ans

text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"
print(word_freq(text))

# 5.Refactor your character count script to use a function named char_count_dict(text) that returns 
# the frequency dictionary, and then print the dictionary sorted by character (A-Z or a-z).

def char_count_dict(text):

    ans={}
    for i in text:
        if i in ans:
            ans[i]+=1
        else:
            ans[i] = 1
    return ans

text = input("Enter String: ")
result = char_count_dict(text)

for ch in sorted(result):
    print(ch, "=", result[ch])