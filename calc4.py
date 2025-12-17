import re

#raw numbers, handles parenthesis
def numbers(tokens):
    face = tokens.pop(0)
    if face == '(':
        result = Add_Subtract(tokens)
        tokens.pop(0)
        return result
    
    return float(face) if '.' in face else int(face)

#negative numbers
def Unary(tokens):
    if tokens and tokens[0] == '-':
        tokens.pop(0)
        return -Unary(tokens) 
    if tokens and tokens[0] == '+':
        tokens.pop(0)
        return Unary(tokens)
    return numbers(tokens)

#Going through PEMDAS starting at exponents
def Exponent(tokens):
    result = Unary(tokens)
    while tokens and tokens[0] == '^':
        tokens.pop(0)
        right = Exponent(tokens)
        result = result ** right
    return result

def Multiply_Divide(tokens):
    result = Exponent(tokens)
    while tokens and tokens[0] in ('*' , '/'):
        operator = tokens.pop(0)
        right = Exponent(tokens)
        result = (result * right) if operator == '*' else (result / right)
    return result

def Add_Subtract(tokens):
    result = Multiply_Divide(tokens)
    while tokens and tokens[0] in ('+','-'):
        operator = tokens.pop(0)
        right = Multiply_Divide(tokens)
        result = (result + right) if operator == '+' else (result - right)
    return result

def Calculate():
    equation_line = input()
    tokens = re.findall(r'\d+\.?\d*|[\+\-\*\/\^\(\)]', equation_line)
    if tokens:
        result = Add_Subtract(tokens)
        print(result)
        
if __name__ == '__main__':
    Calculate()



