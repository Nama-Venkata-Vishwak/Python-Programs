from threading import Thread, current_thread

print("start", current_thread().getName())


def mul(n=10):
    for j in range(2, n):
        x = True
        for i in range(2, int(n**(1/2))):
            if j % i == 0 :
                x = False
        if x:
            print(j)


def fact(n):
    if n == 1:
        return 1
    else:
        y = int(fact(n-1))
        return n*y


a = int(input("Enter a Number: "))
child = Thread(target=mul(a))
child.start()
w = fact(a)
print(w)
print("End:", current_thread().getName)
