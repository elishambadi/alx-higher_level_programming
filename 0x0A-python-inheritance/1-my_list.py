#!/usr/bin/python3
class MyList(list):
    pass

def print_sorted(self):
    bubblesort(MyList)
    print(MyList)

def bubblesort(list):

# Swap the elements to arrange in order
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
