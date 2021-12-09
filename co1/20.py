num=[1,2,7,5,40,8]
print("original list:",num)
num=[x for x in num if x%2!=0]
print("list after removing even numbers:",num)
