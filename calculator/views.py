from rest_framework.decorators import api_view
from rest_framework.response import Response
import re


@api_view(['POST'])
def calculate(request):
    if request.method == 'POST':
        expression = request.data.get('expression')
        if expression:
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
            else:
                return Response({'error': 'Invalid expression. Only positive integers and +,- operators are allowed.'}, status=400)
        else:
            return Response({'error': 'Expression not provided'}, status=400)
    else:
        return Response({'error': 'Method not allowed'}, status=405)
