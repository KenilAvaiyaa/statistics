from django.shortcuts import render, redirect
from .forms import NumbersInputForm
import statistics
import math

# split numbers and corvert in to float type
def parseNumber(num_str):
    num_list=[]
    split = num_str.split(',')
    for i in split:
        data = i.strip()
        if data != "":
            num = float(data)
            num_list.append(num)
    return num_list


def primeNumberCheck(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def armstrongCheck(n):
    n = abs(n)
    numbers = str(n)
    total_digit = len(numbers)
    sum = 0
    for i in numbers:
        digit = int(i)
        sum += digit ** total_digit
    if sum == n:
        return True
    else:
        return False

def home(request):
    unique_count = len(request.session.get("unique_numbers", []))
    if request.method == "POST":
        form = NumbersInputForm(request.POST, request.FILES)
        if form.is_valid():
            numbers_list = []
            numbers_input = form.cleaned_data.get("numbers")
            if numbers_input:
                numbers_list.extend(parseNumber(numbers_input))
            uploaded_file = form.cleaned_data.get("file")
            if uploaded_file:
                data = uploaded_file.read().decode()
                numbers_list.extend(parseNumber(data))
            if not numbers_list:
                return render(
                    request,
                    "web/home.html",
                    {"form": form, "unique_count": unique_count, "error": "No valid numbers."},
                )
            request.session["numbers"] = numbers_list
            request.session["unique_numbers"] = list(set(numbers_list))
            return redirect("result")
    else:
        form = NumbersInputForm()

    return render(
        request,
        "web/home.html",
        {"form": form, "unique_count": unique_count},
    )

def result(request):
    num = request.session.get("numbers")
    if not num:
        return redirect("home")

    addition = sum(num)
    mean = statistics.mean(num)
    median = statistics.median(num)
    try:
        modeResult = statistics.mode(num)
    except statistics.StatisticsError:
        modeResult = ", ".join(map(str, statistics.multimode(num)))
    range = max(num) - min(num)


    integer = []
    for i in num:
        if float(i).is_integer():
            integer.append(int(i))
    
    primeNumber = []
    for i in integer:
        if primeNumberCheck(i):
            primeNumber.append(i)
    
    armstrongNumber = []
    for i in integer:
        if armstrongCheck(i):
            armstrongNumber.append(i)

    context = {
        "sum": addition,
        "mean": mean,
        "median": median,
        "mode": modeResult,
        "range": range,
        "primes": primeNumber,
        "armstrongs": armstrongNumber,
        "unique_no": len(request.session.get("unique_numbers", [])),
    }
    return render(request, "web/result.html",context)
