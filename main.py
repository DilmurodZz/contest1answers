import random
from task1 import decorator_1
from task2 import typeBasedTransformer

@decorator_1
def func():
    print("I am ready to Start")
    finish = 0
    n = random.randint(10, 751)
    for i in range(n):
        finish += (i ** 2)

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    mval = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > mval:
            mval = i

if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()

    transformed = typeBasedTransformer(A=5, B="Me", C=True, D=[1, 2, 3], E={'a': 1, 'b': 2})
    print(transformed)
