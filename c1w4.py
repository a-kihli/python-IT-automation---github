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

#list Comprehensions
mylist=[]
for x in range(1,11):
    mylist.append(x*10)
print(mylist)
mylist= [x*10 for x in range(1,11)]
print(mylist)
# the same thing for the 1st exemple
length= [len(letter) for letter in mylist]
# we can also use condition
div3= [x for x in range(0,101) if x%3==0]
print(div3)
## QUESTION: our odd function
def odd_numbers(n):
	return [x for x in range(0,n+1) if x%2!=0]

print(odd_numbers(5))  # Should print [1, 3, 5]
