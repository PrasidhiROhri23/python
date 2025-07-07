# To count the number of words in the string, count number of letter 's' in the string and to swap case

user = input("Enter a string in any case: ");
user = user +' ';
words = user.split();
print(f'Number of words in the given string is {len(words)}');

letter = user.count('s');
print(f'Number of letters in the provided string is {letter}')

print(f'Case swap of user is {user.swapcase()}');