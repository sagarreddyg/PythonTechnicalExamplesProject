from django.shortcuts import render


# Create your views here.
def content(str):
    fh = open(str, "r")
    con = fh.read()
    return con


def index(request):
    home = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/Add Of Matrices.py")}
    return render(request, "PythonTechnicalExamples/index.html", context=home)


def python(request):
    return render(request, "PythonTechnicalExamples/aboutpython.html")


def additionofmatix(request):
    mat = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/Add Of Matrices.py")}
    return render(request, "PythonTechnicalExamples/addition of matrix.html", context=mat)


def helloworld(request):
    hello = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/helloworld/helloworld.py")}
    return render(request, "PythonTechnicalExamples/helloworld/helloworld.html", context=hello)


def helloworld1(request):
    hello = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/helloworld/helloworld1.py")}
    return render(request, "PythonTechnicalExamples/helloworld/helloworld.html", context=hello)


def helloworld2(request):
    hello = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/helloworld/helloworld2.py")}
    return render(request, "PythonTechnicalExamples/helloworld/hello1.html", context=hello)


def helloworld3(request):
    hello = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/helloworld/helloworld3.py")}
    return render(request, "PythonTechnicalExamples/helloworld/hello2.html", context=hello)


def sumofnum(request):
    su = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/sumofNum/sumoftwonumbers.py")}
    return render(request, "PythonTechnicalExamples/Sumofnum/sumofnum.html", context=su)


def sumofnum1(request):
    su = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/sumofNum/sumofgivennumbers.py")}
    return render(request, "PythonTechnicalExamples/Sumofnum/sumofnum1.html", context=su)


def sumofnum2(request):
    su = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/sumofNum/sumoftwousergivenNumbers.py")}
    return render(request, "PythonTechnicalExamples/Sumofnum/sumofnum2.html", context=su)


def sumofnum3(request):
    su = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/sumofNum/sum.py")}
    return render(request, "PythonTechnicalExamples/Sumofnum/sumofnum3.html", context=su)


def evenrange(request):
    even = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/even.py")}
    return render(request, "PythonTechnicalExamples/even.html", context=even)


def prime(request):
    prime = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/prime.py")}
    return render(request, "PythonTechnicalExamples/prime.html", context=prime)


def Odd(request):
    odd = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/Odd.py")}
    return render(request, "PythonTechnicalExamples/odd.html", context=odd)

