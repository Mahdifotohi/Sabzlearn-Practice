def rec_fanc(string):
    if len(string) == 0:
        return ""
    return string[-1] + rec_fanc(string[:-1])


print(rec_fanc("hello"))
