import string
import datrie
import re
file1 = open("C://Users//ekost//OneDrive//Desktop//sample.txt")
s = [line.strip() for line in file1]
trie = datrie.Trie(string.printable)
for line in s:
    line1 = line.split(', ')
    name = line1[0]
    phone = line1[1]
    trie[phone] = name

trie1 = datrie.Trie(string.printable)

for key, value in trie.items():
    trie1.setdefault(value, set()).add(key)


def find_by_phone_number(phone_number):
    return trie[phone_number]


def find_by_name(name):
    return list(trie1[name])


def find_by_wildcard_phone(wildcard_phone):
    w_p = ''.join(symbol for symbol in str(wildcard_phone) if symbol != '*')
    return trie.items(w_p)


def find_by_wildcard_name(wildcard_name):
    w_n = ''.join(symbol for symbol in str(wildcard_name) if symbol != '*')
    return trie1.items(w_n)


def find_by_wildcard_phone_and_name(wildcard_phone, wildcard_name):
    list_phone_name = []
    for key, value in trie.items():
        m1 = re.search(wildcard_phone, key)
        m2 = re.search(wildcard_name, value)
        if m1 and m2:
            list_phone_name += [key]
            list_phone_name += [value]
    return list_phone_name

wildcard = input('Enter the search data: ')


def find_data_by_input(wildcard):
    if wildcard.find(',') == -1:
        match1 = re.search(r'\d', wildcard)
        if match1:
            if wildcard.find(('*')) == -1:
                return find_by_phone_number(wildcard)
            else:
                return find_by_wildcard_phone(wildcard)
        else:
            if wildcard.find(('*')) == -1:
                return find_by_name(wildcard)
            else:
                return find_by_wildcard_name(wildcard)
    else:
        w = wildcard.split(', ')
        w_name = w[0]
        w_phone = w[1]
        w_ph = ''.join('\d' if symbol == '*' else symbol for symbol in w_phone)
        w_nm = ''.join('\w' if symbol == '*' else symbol for symbol in w_name)
        return find_by_wildcard_phone_and_name(w_ph, w_nm)


print(find_data_by_input(wildcard))

file1.close()