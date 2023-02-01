#1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#2
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#3
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#4
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
#5
set1 = {"abc", 34, True, 40, "male"}
print(set1)
#6
myset = {"apple", "banana", "cherry"}
print(type(myset))
#7
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#8
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#9 true
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#10
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#11
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#12
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#13
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#14Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#15Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#16 set()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#17
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists
#18
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#19The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#20The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#21
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#22
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
#23
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#24
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
