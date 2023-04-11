def greeting():
    print("Hello User")

greeting() 

def pack(first_name, last_name, age):
    print([last_name, first_name, age])

pack("John", "Doe", 30)

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}") 

eat_lunch([])
eat_lunch(["BEC"])
eat_lunch(["Orange","Yogurt","BEC","Ice Cream"])