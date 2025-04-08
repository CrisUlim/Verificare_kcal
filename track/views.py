from django.shortcuts import render, redirect
from .models import Food
from django.http import JsonResponse

def home(request):
    calorie_goal = 2000
    if 'consumed_food' not in request.session:
        request.session['consumed_food'] = []

    if request.method == 'POST':
        food_consumed = request.POST.get('food_consumed')
        if food_consumed and food_consumed not in request.session['consumed_food']:
            request.session['consumed_food'].append(food_consumed)
            request.session.modified = True

    foods = Food.objects.all()
    consumed_food_names = request.session['consumed_food']
    consumed_food = Food.objects.filter(name__in=consumed_food_names)

    return render(request, 'home.html', {
        'foods': foods,
        'consumed_food': consumed_food,
        'calorie_goal': calorie_goal,
    })


def remove_food(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        food_name = data.get('food_name')

        if 'consumed_food' in request.session and food_name in request.session['consumed_food']:
            request.session['consumed_food'].remove(food_name)
            request.session.modified = True
            return JsonResponse({'success': True, 'message': f'{food_name} removed.'})
        return JsonResponse({'success': False, 'message': 'Food not found.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})



def contact(request):
    return render(request, 'contact.html')

def calculator(request):
    
    if request.method == 'POST':
        gender = request.POST.get('gender')
        age = int(request.POST.get('age', 0))
        height = float(request.POST.get('tall', 0))
        weight = float(request.POST.get('weigh', 0))
        activity_level = float(request.POST.get('active', 1.2))
        
        if gender == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
        daily_kcal = bmr * activity_level
        weekly_kcal = daily_kcal * 7
        
        protein_min_kcal = daily_kcal * 0.10
        protein_max_kcal = daily_kcal * 0.35
        protein_min_grams = protein_min_kcal / 4
        protein_max_grams = protein_max_kcal / 4
        
        fat_min_kcal = daily_kcal * 0.20
        fat_max_kcal = daily_kcal * 0.35
        fat_min_grams = fat_min_kcal / 9
        fat_max_grams = fat_max_kcal / 9
        
        return render(request, 'result.html', {
            'daily_kcal': daily_kcal,
            'weekly_kcal': weekly_kcal,
            'protein_min_grams': protein_min_grams,
            'protein_max_grams': protein_max_grams,
            'fat_min_grams': fat_min_grams,
            'fat_max_grams': fat_max_grams,
        })
    return render(request, 'calculator.html')