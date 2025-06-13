# app/views.py
import requests
from django.http import JsonResponse

def get_outbreak_prediction(request):
    region = request.GET.get('region')
    year = request.GET.get('year')

    print(f"Received input: region={region}, year={year}")  # ✅ 加这行调试

    if not region or not year:
        return JsonResponse({"error": "Missing region or year"}, status=400)

    try:
        year = int(year)
    except ValueError:
        return JsonResponse({"error": "Year must be integer"}, status=400)

    try:
        response = requests.post("http://127.0.0.1:8001/predict", json={
            "region": region,
            "year": year
        })
        print(f"FastAPI response status: {response.status_code}")  # ✅ 再加
        print(f"FastAPI response body: {response.text}")            # ✅ 再加
        return JsonResponse(response.json())
    except Exception as e:
        import traceback
        print("🔥 Exception occurred during FastAPI request:")
        traceback.print_exc()  # ✅ 打印完整堆栈错误信息
        return JsonResponse({"error": str(e)}, status=500)