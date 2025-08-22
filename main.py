from add import add
from sub import sub
from div import div
from mul import mul

while True:
    ch = input("Enter the choice: 1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit")
    if ch == 1:
        inp = list(map(int, input().split()))
        print(add(inp))
    elif ch == 2:
        inp = list(map(int, input().split()))
        print(sub(inp))
    elif ch == 3:
        inp1 = int(input())
        inp2 = int(input())
        print(mul(inp1, inp2))
    elif ch == 4:
        inp1 = int(input())
        inp2 = int(input())
        print(div(inp1, inp2))
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")