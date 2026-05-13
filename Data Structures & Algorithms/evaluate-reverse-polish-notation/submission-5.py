class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        op_stack = []
        result = 0
        for i in tokens:
            print(f"now at {i}...")
            if i not in operators:
                print(f"{i} is a digit")
                op_stack.append(i)
                print(f"stack at {i}: {op_stack}")
            elif i == '+':
                A = int(op_stack.pop())
                print('popping stack: ', A)
                B = int(op_stack.pop())
                print('popping stack: ', B)
                result = B + A
                print('result after adding: ', result)
                op_stack.append(result)
                print('appended result: ', op_stack)
            elif i == '-':
                A = int(op_stack.pop())
                print('popping stack: ', A)
                B = int(op_stack.pop())
                print('popping stack: ', B)
                result = B - A
                print('result after sub: ', result)
                op_stack.append(result)
                print('appended result: ', op_stack)
            elif i == '*':
                A = int(op_stack.pop())
                print('popping stack: ', A)
                B = int(op_stack.pop())
                print('popping stack: ', B)
                result = B * A
                print('result after mult: ', result)
                op_stack.append(result)
                print('appended result: ', op_stack)
            elif i == '/':
                A = int(op_stack.pop())
                print('popping stack: ', A)
                B = int(op_stack.pop())
                print('popping stack: ', B)
                result = int(B / A)
                print('result after div: ', result)
                op_stack.append(result)
            

        return int(op_stack[0])