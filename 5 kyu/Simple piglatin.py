# Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

def pig_it(text):
    lst = text.split(' ')
    result = ''
    for i in lst:
        if i in '!.%&?':
            result += i
        else:
            word = i[1:] + i[0] + 'ay '
            result += word
    return result.strip()