def hackerrankInString(s):
    original = 'hackerrank'
    sub = ''
    index = 0

    for i in s:
        if index < len(original) and original[index] == i:
            sub += i
            index += 1
    
    if len(original) == len(sub):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input().strip()

        result = hackerrankInString(s)

        print(result)
