import random

my_list = [1,2,3,4,5,6]
# for i in my_list:
#     print(i)




iterator = iter(my_list)

for i in iterator:
    print(i)



for i in iterator:
    print(i)


# print(next(iterator))


# class RandomIterator:
#     def __init__(self , limit):
#         self.limit = limit
#         self.__reload = limit
#     def __iter__(self):
#       self.limit = self.__reload
#       return self

#     def __next__(self):
#       if self.limit == 0 :
#          raise StopIteration
#       self.limit -=1
#       return random.randint(0,100)
      

# my_iter = RandomIterator(1)
# for i in my_iter:
#     print (i)



























# import time
# import sys




# class ThreadRedirect:
#     def __init__(self):
#         self.stdout = sys.stdout



#     def __enter__(self):
#         sys.stdout = open(f"file.txt","w", encoding = "utf-8")

#     def __exit__(self,exc_type,exc_val ,exc_tb):
#         sys.stdout = self.stdout


# with ThreadRedirect():
#     print("hello , world")


























# import time






# class CodeTimer:
#     def __init__(self):
#         self.start = None

#     def __enter__(self):
#         self.start = time.time()

#     def __exit__(self,exc_type,exc_val ,exc_tb) :    
#         t = time.time() - self.start
#         print(f"код работал{t}")

# timer = CodeTimer()

# with timer:
#     l = [x for x in range(100_000_000)]