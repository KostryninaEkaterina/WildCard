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


def find_by_phone_number(phone_number):
    return trie[phone_number]


def find_by_name(name):
    phone = []
    for key, value in trie.items():
        if value == name:
            phone += [key]
    return phone


def find_by_wildcard_phone_and_name(wildcard_phone, wildcard_name):
    list_phone_name = []
    for key, value in trie.items():
        m1 = re.search(wildcard_phone, key)
        m2 = re.search(wildcard_name, value)
        if m1 and m2:
            list_phone_name += [key]
            list_phone_name += [value]
    return list_phone_name


file1.close()