from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            country = data.get('country')
            year = int(data.get('year'))

            print(f"[Django] Received request: country={country}, year={year}")

            # Forward request to FastAPI
            response = requests.post(
                "http://127.0.0.1:8001/predict",
                json={"country": country, "year": year}
            )

            print(f"[Django] FastAPI responded: {response.status_code} {response.text}")

            return JsonResponse(response.json())

        except Exception as e:
            import traceback
            print("Error while contacting FastAPI:")
            traceback.print_exc()
            return JsonResponse({"error": str(e)}, status=500)
