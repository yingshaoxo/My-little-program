with open('simple_word.txt', 'rt') as f:
    text = f.read()
my_list = eval(text)

while True:
    word = input('Add your word here(q to quit): ')
    if word == 'q':
        break
    my_list.append(word)

with open('my_words.txt', 'wt') as f:
    f.write(str(my_list))
