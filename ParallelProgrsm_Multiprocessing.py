import multiprocessing
def fact(n):
 if n == 1:
 return 1
 else:
 y = int(fact(n-1))
 return n*y
def hel(n):
 print(fact(n))
if __name__ == '__main__':
 for i in range(1, 20, 5):
 p = multiprocessing.Process(target=hel, args=(i,))
 p.start()
