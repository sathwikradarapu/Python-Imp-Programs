def count_of_duplicate_words(text):
    count_map = {}
    words = text.split(" ")
    for word in words:
        count_map[word]=words.count(word)
    print(count_map)
    for word,count in count_map.items():
        print(str(word)+" : "+str(count))

# Test the function
text = input()
count_of_duplicate_words(text)