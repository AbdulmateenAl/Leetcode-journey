class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []

        for val in tokens:
            if self.isOperator(val):
                num2 = result.pop()
                num1 = result.pop()
                result.append(self.operation(num1, num2, val))
            else:
                result.append(int(val))

        return result[0]
        
    def isOperator(self, operator: str) -> bool:
        match operator:
            case "+":
                return True
            case "-":
                return True
            case "*":
                return True
            case "/":
                return True

    def operation(self, a: int, b: int, operator:str) -> int:
        match operator:
            case "+":
                return int(a + b)
            case "-":
                return int(a - b)
            case "*":
                return int(a * b)
            case "/":
                return int(a / b)