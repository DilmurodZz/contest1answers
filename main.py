from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer

def main():
    # Task 1
    print("Task 1 Output:")
    kwargsAcceptFun(A="Me", B=20, country="Urgench")

    # Task 2 
    print("\nTask 2 Output:")
    result = typeBasedTransformer(
        number=4,
        text="Yes, worked",
        is_active=True,
        items=[1, 2, 3],
        coordinates=(10, 20),
        data={"a": 1, "b": 2},
        unsupported_obj=set([1, 2, 3])
    )
    print(result)

if __name__ == "__main__":
    main()
