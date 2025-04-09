def rec_fanc(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return rec_fanc(s[1:-1])
    

print(rec_fanc("mom"))
