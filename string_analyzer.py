from string_package import count_characters, count_words, average_word_length, reverse_string, capitalize_words, remove_punctuation

a = input("Enter a sentence: ")

print("Reverse version: ", reverse_string(a))
print("Capital version: ", capitalize_words(a))
a = remove_punctuation(a)
print("Total characters: ", count_characters(a))
print("Total words: ", count_words(a))
print("Average word length: ", average_word_length(a))
