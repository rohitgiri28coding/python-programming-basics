def compress(chars: list[str]) -> int:
    unique = []
    [unique.append(i) for i in chars if i not in unique]
    s = ''
    for i in unique:
        c = chars.count(i)
        if c == 1:
            s = s + i
        else:
            s = s + i + str(c)
    chars = list(s)
    print(chars)
    return len(chars)


print(compress(["a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c"]))
