from django.shortcuts import render


# Create your views here.
def content(str):
    fh = open(str, "r")
    con = fh.read()
    return con


def index(request):
    home = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/Add Of Matrices.py")}
    return render(request, "PythonTechnicalExamples/index.html", context=home)


def additionofmatix(request):
    mat = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/Add Of Matrices.py")}
    return render(request, "PythonTechnicalExamples/index.html", context=mat)


def helloworld(request):
    hello = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/helloworld.py")}
    return render(request, "PythonTechnicalExamples/helloworld.html", context=hello)


def sumofnum(request):
    su = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/sum.py")}
    return render(request, "PythonTechnicalExamples/sumofnum.html", context=su)


def evenrange(request):
    even = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/even.py")}
    return render(request, "PythonTechnicalExamples/even.html", context=even)

