from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reminder
import json

@csrf_exempt
def create_reminder(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = data.get('date')
        time = data.get('time')
        message = data.get('message')
      

      
        reminder = Reminder.objects.create(date=date, time=time, message=message)
        reminder.save()

        return JsonResponse({'status': 'Reminder created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
