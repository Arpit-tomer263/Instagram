from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
import json
from django.utils import timezone
from django.shortcuts import render
@csrf_exempt  # Use CSRF exempt for simplicity, but in production, you should handle CSRF tokens properly.
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
            latitude = data['latitude']
            longitude = data['longitude']
            
            # Create the user profile and save it to the database
            user_profile = UserProfile(
                username=username,
                password=password,
                latitude=latitude,
                longitude=longitude,
                timestamp=timezone.now(),
            )
            user_profile.save()
            
            return JsonResponse({'message': 'User created successfully!'}, status=201)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
    return render(request, 'index.html')

