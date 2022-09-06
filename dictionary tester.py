import random

while True:
    print("type 0 for simple mode and 1 for a hard one")
    print("or you may input your own list of words by dragging your file here")
    inp = input(">>> ")
    if inp == "0":
        f = open("vocabulary.txt", "r")
        how_much_to_show = 75
        break
    elif inp == "1":
        f = open("test.txt", "r")
        how_much_to_show = 100
        break
    else:
        try:
            f = open(inp, "r")
            how_much_to_show = 100
        except:
            print("Can't open a file:", inp)
            continue
        try:
            how_much_to_show = int(input("How many words to show? "))
        except:
            print("Something went wrong")
        break
            

work_list = f.readlines()

print("If you know this word, type ok")

counter = 0

for x in range(how_much_to_show):
    print(random.choice(work_list)[:-1])
    if input(">>> ") == "ok":
        counter += 1

result = counter * len(work_list) / how_much_to_show

print("Your vocabulary is estimated to be", round(result))
input()

f.close()
