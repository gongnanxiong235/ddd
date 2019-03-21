import re


def phone(phone):
    phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7|5]|18\d)\d{8}$')
    res = re.search(phone_pat, phone)
    return res