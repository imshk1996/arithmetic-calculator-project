from rest_framework.decorators import api_view
from rest_framework.response import Response
import re

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

@api_view(['POST'])
def calculate(request):
    if request.method == 'POST':
        expression = request.data.get('expression')
        if expression:
            # Validate expression
            if re.match(r'^[0-9+\- ]+$', expression):
                result = evaluate_expression(expression)
                return Response({'result': result})
            else:
                return Response({'error': 'Invalid expression. Only positive integers and +,- operators are allowed.'}, status=400)
        else:
            return Response({'error': 'Expression not provided'}, status=400)
    else:
        return Response({'error': 'Method not allowed'}, status=405)
