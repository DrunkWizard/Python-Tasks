import re

class PhoneNumberException(Exception):
    pass

def prepare_phone_number(phone: str)-> str:
    if isinstance(phone, int):
        raise PhoneNumberException(phone)
    phone_pattern = r"(\+7|7|8)(\s|\-)?(\(?\d{3}\)?)(\s|\-)?((\d{3})(\s|\-)?(\d{2})(\s|\-)?(\d{2})|(\d{2})(\s|\-)?(\d{3})(\s|\-)?(\d{2})|(\d{2})(\s|\-)?(\d{2})(\s|\-)?(\d{3}))"
    match = re.fullmatch(phone_pattern, phone)
    if match is None:
        raise PhoneNumberException("SOS")
    match = match.group()
    match = re.sub(r"[\(\)\-\s\+]", "", match)
    if(len(match) == 10):
        match = '+7' + match
    elif(len(match) == 11):
        match = '+7' + match[1:]
    else:
        raise PhoneNumberException("SAS")
    return '{} ({}) {}-{}-{}'.format (match[0:2], match[2:5], match[5:8], match[8:10], match[10:12])
