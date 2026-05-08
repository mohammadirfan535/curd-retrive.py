list=[1,2,3,4,5,6,7,8,9,10]
print(list[4])
print(list[-1:-10:-1])

le=[1,2,3,4,5,6,7,8,9]
print(le)
le.append(10)
print("after adding 10")
print(le)


le=[1,2,3,4,5]
print(le)
le.extend(range(6,20))
print("after extend for 6,20")
print(le)

le=[1,2,3,5,6,7,8,9]
print(le)
le.insert(4,3)
print("after insert the element")
print(le)