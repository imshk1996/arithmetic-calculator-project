from rest_framework.decorators import api_view
from rest_framework.response import Response
import re


def evaluate_expression(expression):
    if expression.startswith('--'):
        return "Invalid expression: Double negative at the beginning"

    tokens = re.findall(r'(\d+|\+|\-)', expression)

    if not tokens:
        return "Invalid expression"

    if len(tokens) == 1 and not tokens[0].isdigit():
        return "Invalid expression"

    if tokens[-1] in ['+', '-']:
        return "Invalid expression: Missing operand after '{}'".format(tokens[-1])

    result = int(tokens[0])

    i = 1
    while i < len(tokens):
        operator = tokens[i]
        if operator not in ['+', '-']:
            return "Invalid expression: Unexpected operator '{}'".format(operator)

        i += 1

        if i >= len(tokens):
            return "Invalid expression: Missing operand after '{}'".format(operator)

        operand = tokens[i]
        if not operand.isdigit():
            return "Invalid expression: Unexpected operand '{}'".format(operand)

        operand = int(operand)

        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand

        i += 1

    return result



@api_view(['POST'])
def calculate(request):
    if request.method == 'POST':
        expression = request.data.get('expression')
        if expression:
            if re.match(r'^[0-9+\- ]+$', expression):
                result = evaluate_expression(expression)
                if isinstance(result, str):
                    return Response({'error': result}, status=400)
                return Response({'result': result})
            else:
                return Response({'error': 'Invalid expression. Only positive integers and +,- operators are allowed.'}, status=400)
        else:
            return Response({'error': 'Expression not provided'}, status=400)
    else:
        return Response({'error': 'Method not allowed'}, status=405)