def solution(s):
    result = ''
    for i in s:
        if i.isupper():
            result += ' '
        result += i
    return result

print(solution('someCameCaseShit'))