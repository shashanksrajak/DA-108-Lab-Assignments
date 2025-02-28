# built-in package unicodedata
import unicodedata


def determine_unicode_name(char):
    try:
        # the default output is like this -> LATIN SMALL LETTER S
        # so we take only the first string part LATIN
        return unicodedata.name(char).split()[0]
    except ValueError:
        return "Unknown"


if __name__ == "__main__":
    with open("file.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # initialise a dict for recording scripts and count
    scripts_count = {}

    for char in text:
        if char.isalpha():
            script = determine_unicode_name(char)
            if script in scripts_count:
                scripts_count[script] += 1
            else:
                scripts_count[script] = 1

    print(scripts_count)
