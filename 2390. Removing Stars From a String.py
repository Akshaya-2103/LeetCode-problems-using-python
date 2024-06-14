
def removeStars(s: str) -> str:
    stack = []
    for i in s:
        if i == "*":
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return "".join(stack)
s = input()
print(removeStars(s))

