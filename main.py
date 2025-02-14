from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import filterGreaterThan

def main():
    # Task 1
    print("Task 1 Output:")
    kwargsAcceptFun(A="Me", B=20, country="Urgench")

    # Task 2 
    print("\nTask 2 Output:")
    result2 = typeBasedTransformer(
        number=4,
        text="Yes, worked",
        is_active=True,
        items=[1, 2, 3],
        coordinates=(10, 20),
        data={"a": 1, "b": 2},
        unsupported_obj=set([1, 2, 3])
    )
    print(result2)

    # Task 3 
    print("\nTask 3 Output:")
    result3 = filterGreaterThan(10, A=5, B=15, C=25, text="Yes, worked", D=3.5)
    print(result3)

if __name__ == "__main__":
    main()
