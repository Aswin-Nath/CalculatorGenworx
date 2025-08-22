from add import add
from sub import sub
from div import div

while True:
    ch = input("Enter the choice: 1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit")
    if ch == 1:
        inp = list(map(int, input().split()))
        print(add(inp))
    elif ch == 2:
        inp = list(map(int, input().split()))
        print(sub(inp))
    elif ch == 3:
        pass
    elif ch == 4:
        pass
    elif ch == 5:
        pass
    else:
        print("Invalid choice")