from collections import Counter
text =input("Enter Your Texts here : ")
words=text.lower().split()
word=Counter(words)
print(word)