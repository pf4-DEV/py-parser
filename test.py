from parseur import parser

sortie = parser("""

print("runing")
for i in range(4000):
    max = int(i ** 0.5 + 1) #2!
    if i%2 != 0:
        for x in range(2, max):
            if i%x == 0:
                break
            if x == max:
                print(i)

""")

for e in sortie:
    print(e)