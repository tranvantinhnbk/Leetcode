s=")"
hash = {'(':')','[':']','{':'}'}
stack = []

for c in s:
    if c in hash:
        stack.append(c)
    else:
        if stack != []:
            if c != hash[stack.pop()]:
                print(False)
                break
        else:
            print(False)




