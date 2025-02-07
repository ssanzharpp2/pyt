def rev():
    lst = []
    s = str(input())
    start = 0
    last = 0
    for x in s:
        if x != ' ':
            last += 1
        else:
            lst.append(s[start:last])
            start = last + 1
            last += 1
            continue
    lst.append(s[start:last])
    print(lst[::-1])
rev()