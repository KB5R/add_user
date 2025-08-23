#!/usr/bin/python3

FILE_INPUT = 'user.txt'
FILE_OUTPUT = 'full_users.txt'

def transliterate(name):

    dictionary = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'c',
        'ч': 'cz',
        'ш': 'sh',
        'щ': 'sch',
        'ъ': '',
        'ы': 'y',
        'ь': '',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'ZH',
        'З': 'Z',
        'И': 'I',
        'Й': 'Y',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'C',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Sch',
        'Ъ': '',
        'Ы': 'y',
        'Ь': '',
        'Э': 'E',
        'Ю': 'Yu',
        'Я': 'Ya',
        ',': '',
        '?': '',
        ' ': ' ',
        '~': '',
        '!': '',
        '@': '',
        '#': '',
        '$': '',
        '%': '',
        '^': '',
        '&': '',
        '*': '',
        '(': '',
        ')': '',
        '-': '',
        '=': '',
        '+': '',
        ':': '',
        ';': '',
        '<': '',
        '>': '',
        '\'': '',
        '"': '',
        '\\': '',
        '/': '',
        '№': '',
        '[': '',
        ']': '',
        '{': '',
        '}': '',
        'ґ': '',
        'ї': '',
        'є': '',
        'Ґ': 'g',
        'Ї': 'i',
        'Є': 'e',
        '—': ''
    }

    for key in dictionary:
        name = name.replace(key, dictionary[key])
    return name


def main():
    __read_file()

def __read_file():
    with open (FILE_INPUT, "r", encoding="utf-8") as users, \
    open (FILE_OUTPUT, "a",  encoding="utf-8") as resultat:
        for line in users:
            split = line.split()

            format_lastname = transliterate(split[1])
            format_firstname = transliterate(split[0])

            login_lastname = transliterate(split[1])
            login_firstname = transliterate(split[0])

            mail_name = split[3]

            title_name = split[4] if len(split) >= 5 else ""

            result = (format_lastname + ":" + format_firstname + ":" + login_lastname.lower() + "." + login_firstname.lower() + ":" + title_name  + ":" + mail_name )

            resultat.write(result + "\n")



if __name__ == "__main__":
    main()
