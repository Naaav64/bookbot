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


def get_report(text):
    key = get_character_num(text)
    name_list = []
    for k in key:
        name = k
        num = key[k]
        if name.isalpha() == True:
            name_list.append({"char": k, "num": key[k]})
        else:
            pass

    name_list.sort(reverse=True, key=lambda item: item["num"])
    for name in name_list:
        print(f"{name["char"]}: {name["num"]}")
    return ""
   