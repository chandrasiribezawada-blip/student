from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def colleges(request):
    collegelist = ['SVECW', 'VIT', 'BVRICE']
    return render(request, 'college.html', {'colleges': collegelist})


studentdata=[
    {'rno':1201,'name':'milky','age':21,'branch':'CSE',},
    {'rno':1202,'name':'siri','age':17,'branch':'ECE',},
    {'rno':1203,'name':'yash','age':21,'branch':'MECH',},
    
    
]
def Student(request):
    return render(request, 'students.html', {'students': studentdata})

# Create your views here.
