def get_num_words(text):
    counter = len(text.split())
    return counter

def get_num_characters(text):
    characters = {
        }
    for i in text.lower():
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
