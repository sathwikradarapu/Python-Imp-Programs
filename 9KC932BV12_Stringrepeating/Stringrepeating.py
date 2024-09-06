def unique_char(word):
    word=word.lower()
    set_1=set(word)
    set_1.discard(" ")
    for char in sorted(set_1):
        res="{}:{}"
        print(res.format(char,word.count(char)))
word=input()
unique_char(word)