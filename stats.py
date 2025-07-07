def get_num_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def get_character_num(text):
    char = text.lower()
    char_count = {}
    for c in char:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
       
    return char_count