verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages

message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."


#Problem 1:What is the length of the string variable verse?
length = len(verse)

#Problem 2:What is the index of the first occurrence of the word 'and' in verse?
first_idx = verse.find('and')

#Problem 3:What is the index of the last occurrence of the word 'you' in verse?
last_idx = verse.rfind('you')

#Problem 4:What is the count of occurrences of the word 'you' in the verse?
count = verse.count('you')

print(message.format(length, first_idx, last_idx, count))
