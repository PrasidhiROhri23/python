user = input("Enter a sentence: ");
user = user+ ' ';
words = user.split();
count = len(words);

print(f'The number of words in the given sentence are {count}');