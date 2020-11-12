mylist = ["abcd","bcd","cd"]
chars=0
for letter in mylist:
    chars += len(letter)
print("total characters: {}, average length: {}".format(chars,chars/len(mylist)))
#part 2
# enumerate
full_list = ["1st","2nd","3rd","4th"]
for index, rank in enumerate(full_list): #enumerate return a tuple
    print("{}-{}".format(index+1,rank))

#exp
def skip_elements(elements):
    mylist=[]
    for ind,ele in enumerate(elements):
        if ind%2==0:
            mylist.append(ele)

    return mylist

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

#real scenario
def full_email(people):
    ex_list=[]
    for email,name in people:
        ex_list.append("{} <{}>".format(name,email))
    return ex_list

print(full_email(
[("d.nahel@gmail.com","djilali nahel"),
("m.karim@gmail.com", "mriza9 karim")
]))
