string = "appel"
char = "a"
func = lambda string, char: string.startswith(char)
resulte = func(string, char)
print(f"Dose the string '{string}' strat whith '{char}'? {resulte}")