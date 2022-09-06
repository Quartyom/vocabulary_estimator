import random

while True:
    print("type 0 for simple mode and 1 for a hard one")
    inp = input(">>> ")
    if inp == "0":
        f = open("vocabulary.txt", "r")
        how_much_to_show = 75
        break
    if inp == "1":
        f = open("test.txt", "r")
        how_much_to_show = 100
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
