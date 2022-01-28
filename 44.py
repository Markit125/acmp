s = input()
ans = 0
i = 0
while i < len(s):
    if s[i] == '<':
        if i < len(s) - 4:
            if s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] == '--<<':
                ans += 1
    elif s[i] == '>':
        if i < len(s) - 4:
            if s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] == '>-->':
                ans += 1
    i += 1
print(ans)
    