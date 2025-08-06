from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import datetime
# Create your views here.
def index(request):
    if request.method =="POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    expenses = Expense.objects.all()
    #caculating the total amount of expenses
    total_expenses = expenses.aggregate(Sum('amount'))
    
    #logic to calculate 365 days expenses:
    last_year = datetime.date.today() - datetime.timedelta(days=365) #last year
    datay = Expense.objects.filter(date__gt=last_year)
    yearly_sum = datay.aggregate(Sum('amount'))

    #logic to calculate 30 days expenses:
    last_month = datetime.date.today() - datetime.timedelta(days=30) #last month
    datam = Expense.objects.filter(date__gt=last_month)
    monthly_sum = datam.aggregate(Sum('amount'))

    #logic to calculate 7 days expenses:
    last_week = datetime.date.today() - datetime.timedelta(days=7) #last week
    dataw = Expense.objects.filter(date__gt=last_week)
    weekly_sum = dataw.aggregate(Sum('amount'))
    
    #filter and order by date for 30 days 
    #it will create a list of dictionaries <QuerySet [{'date': datetime.date(2025, 8, 5), 'sum': 14000}]>
    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
    #print(daily_sums)

    #filter and sum by categories
    #it will create a list of dictionaries <QuerySet [{'category': 'Business', 'sum': 8000}, {'category': 'Personal', 'sum': 6000}]>
    categ_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
    
    expense_form = ExpenseForm()
    return render(request,'myapp/index.html',{
        'expense_form':expense_form, 
        'expenses':expenses, 
        'total_expenses':total_expenses,
        'yearly_sum' : yearly_sum,
        'monthly_sum' : monthly_sum,
        'weekly_sum' : weekly_sum,
        'daily_sums' : daily_sums,
        'categ_sums' : categ_sums,
        })





def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    if request.method =="POST":
        #weare editing the instances
        form = ExpenseForm(request.POST, instance = expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, "myapp/edit.html", {'expense_form':expense_form,})


def delete(request, id):

    if request.method =="POST" and "delete" in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')
