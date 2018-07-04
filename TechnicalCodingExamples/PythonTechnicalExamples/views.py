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
    even = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/evennumbers/even4.py")}
    return render(request, "PythonTechnicalExamples/even/even.html", context=even)


def even(request):
    even = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/evennumbers/even2.py")}
    return render(request, "PythonTechnicalExamples/even/even.html", context=even)


def even2(request):
    even = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/evennumbers/even3.py")}
    return render(request, "PythonTechnicalExamples/even/even.html", context=even)


def even3(request):
    even = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/evennumbers/even.py")}
    return render(request, "PythonTechnicalExamples/even/even.html", context=even)


def even4(request):
    even = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/evennumbers/even5.py")}
    return render(request, "PythonTechnicalExamples/even/even.html", context=even)


def Odd(request):
    odd = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/oddnumbers/Odd2.py")}
    return render(request, "PythonTechnicalExamples/Odd/odd.html", context=odd)


def Odd1(request):
    odd = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/oddnumbers/Odd1.py")}
    return render(request, "PythonTechnicalExamples/Odd/odd.html", context=odd)


def Odd2(request):
    odd = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/oddnumbers/Odd3.py")}
    return render(request, "PythonTechnicalExamples/Odd/odd.html", context=odd)


def Odd3(request):
    odd = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/oddnumbers/Odd.py")}
    return render(request, "PythonTechnicalExamples/Odd/odd.html", context=odd)

def Odd4(request):
    odd = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/oddnumbers/Odd4.py")}
    return render(request, "PythonTechnicalExamples/Odd/odd.html", context=odd)


def prime(request):
    prime = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/primenumbers/prime1.py")}
    return render(request, "PythonTechnicalExamples/prime/prime.html", context=prime)


def prime1(request):
    prime = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/primenumbers/prime4.py")}
    return render(request, "PythonTechnicalExamples/prime/prime.html", context=prime)


def prime2(request):
    prime = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/primenumbers/prime.py")}
    return render(request, "PythonTechnicalExamples/prime/prime.html", context=prime)


def prime3(request):
    prime = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/primenumbers/prime2.py")}
    return render(request, "PythonTechnicalExamples/prime/prime.html", context=prime)


def feb(request):
    prime = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/feb/feb1.py")}
    return render(request, "PythonTechnicalExamples/feb/feb.html", context=prime)


def feb1(request):
    prime = {'insert_me': content("PythonTechnicalExamples/PythonPrograms/feb/feb.py")}
    return render(request, "PythonTechnicalExamples/feb/feb.html", context=prime)
