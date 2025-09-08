from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406414776',
        'name': 'Kenzie Nibras Tradezqi',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)

# Create your views here.
