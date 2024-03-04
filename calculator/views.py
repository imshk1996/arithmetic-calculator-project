from rest_framework.decorators import api_view
from rest_framework.response import Response
import re

<<<<<<< HEAD

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


=======
>>>>>>> 5443155b540008057f0ad6486d4cd73822653295

@api_view(['POST'])
def calculate(request):
    if request.method == 'POST':
        expression = request.data.get('expression')
        if expression:
<<<<<<< HEAD
            if re.match(r'^[0-9+\- ]+$', expression):
                result = evaluate_expression(expression)
                if isinstance(result, str):
                    return Response({'error': result}, status=400)
                return Response({'result': result})
=======
            if all(char.isdigit() or char in '+-' for char in expression):
                try:
                    result = int(expression[0])
                    for i in range(1, len(expression), 2):
                        operator = expression[i]
                        operand = int(expression[i+1])
                        if operator == '+':
                            result += operand
                        elif operator == '-':
                            result -= operand
                    return Response({'result': result})
                except Exception as e:
                    return Response({'error': str(e)}, status=400)
>>>>>>> 5443155b540008057f0ad6486d4cd73822653295
            else:
                return Response({'error': 'Invalid expression. Only positive integers and +,- operators are allowed.'}, status=400)
        else:
            return Response({'error': 'Expression not provided'}, status=400)
    else:
        return Response({'error': 'Method not allowed'}, status=405)