#栈
def check(string):
    stack = []
    result_line = [' '] * len(string)


    for index, char in enumerate(string):
        if char == '(':
            stack.append((char,index))
        elif char == ')':
            # 直接和栈顶进行配对
            if stack and stack[-1][0]=='(':
                stack.pop()
            else:
                result_line[index] = '?'
    for _, pos in stack:
        result_line[pos] = 'x'
    
    return ''.join(result_line)

input_string = input("stings :")
result = check(input_string)
print(f"{input_string}\n{result}")