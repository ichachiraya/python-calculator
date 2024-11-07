class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        if b == 0 :
            return "error"
        
        a_abs = abs(a)
        b_abs = abs(b)
        while a_abs >= b_abs :
            a_abs = self.subtract(a_abs, b_abs)
            result +=1
        if (a<0) and (b<0)  :
            result = result 
        elif (a<0) or (b<0)  :
            result = -result 
        return result

    def modulo(self, a, b):
        if b == 0 :
            return "error"
        
        a_abs = abs(a)
        b_abs = abs(b)
        while a_abs >= b_abs :
            a_abs = self.subtract(a_abs, b_abs)
        if (b <0) :
            a_abs = -a_abs
        return a_abs

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(-2, 3))
    print("Example: division: ", calc.divide(4, -2))
    print("Example: modulo: ", calc.modulo(10, 3))