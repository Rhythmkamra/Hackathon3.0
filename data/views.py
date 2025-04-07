# # views.py
# from django.shortcuts import render, redirect
# from django.contrib import messages  # Import messages module
# from .forms import StudentForm

# def home_view(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Data submitted successfully.')  # Add success message
#             return redirect('home')  # Redirect to the home page after saving
#     else:
#         form = StudentForm()
#     return render(request, 'data/home.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentFormCultural, StudentFormSports, StudentFormTechnical

def student_cultural_view(request):
    if request.method == 'POST':
        form = StudentFormCultural(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully.')
            return redirect('cultural')
    else:
        form = StudentFormCultural()
    return render(request, 'data/home.html', {'form': form})

def student_sports_view(request):
    if request.method == 'POST':
        form = StudentFormSports(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully.')
            return redirect('sports')
    else:
        form = StudentFormSports()
    return render(request, 'data/sports.html', {'form': form})

def student_technical_view(request):
    if request.method == 'POST':
        form = StudentFormTechnical(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully.')
            return redirect('technical')
    else:
        form = StudentFormTechnical()
    return render(request, 'data/technical.html', {'form': form})
