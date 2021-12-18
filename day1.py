inputs = input("INPUT")
mylist = inputs.split()
counter = 0
mylist1 = list(map(int, mylist))
A = 0
B = 0
for i in range(len(mylist1)):
  try:
    A = mylist1[i] + mylist1[i+1] + mylist1[i+2]
  except:
    pass
  try:
    B = mylist1[i+1] + mylist1[i+2] + mylist1[i+3]
  except:
    pass

  if B > A:
    counter +=1

print(counter,"!")