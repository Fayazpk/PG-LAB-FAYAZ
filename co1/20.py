num=[3,4,7,8,24,88]
print("original list:",num)
num=[x for x in num if x%2!=0]
print("list after removing even numbers:",num)
