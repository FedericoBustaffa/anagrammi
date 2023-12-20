import sys

if len(sys.argv) != 3:
    print("USAGE: py anagrammi.py <frase1> <frase2>")
else:
    s1 = str(sys.argv[1])
    s2 = str(sys.argv[2])

    x = s1.replace(" ", "")
    y = s2.replace(" ", "")

    x = "".join(sorted(x.lower()))
    y = "".join(sorted(y.lower()))

    # print(x)
    # print(y)

    if len(x) != len(y):
        print("Non sono anagrammi: numero di lettere diverso")
    elif x != y:
        print("Non sono anagrammi: stringhe differenti")
    else:
        print(f'"{s1}" e "{s2}" sono anagrammi')
