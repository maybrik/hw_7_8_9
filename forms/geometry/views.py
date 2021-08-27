from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404

from .forms import TriangleCathetus, PersonForm

from .models import Person


def index(request):
    if request.method == "POST":
        a = request.POST.get("a")
        b = request.POST.get("b")
        a_int = float(a)
        b_int = float(b)
        c = (a_int * a_int + b_int * b_int) ** 0.5
        response = redirect('hypotenuse')
        response['Location'] += f'?hypotenuse={c}'
        return response

    else:
        trianglecathetus = TriangleCathetus()
        return render(request, "index.html", {"form": trianglecathetus})


def hypotenuse(request):
    if 'hypotenuse' in request.GET:
        result = 'Значение гипотенузы по заданным катетам: %r' % request.GET['hypotenuse']
    else:
        result = 'Входные данные не были указаны, невозможно вычислить'
    return HttpResponse(result)


def person(request):
    if request.method == 'POST':
        personform = PersonForm(request.POST)
        person_new = Person()
        person_new.save()
        return HttpResponse('Пользователь успешно создан.')

    else:
        personform = PersonForm()
        return render(request, 'person.html', {'form': personform})


def person_update(request, person_id):
    object_person_id = get_object_or_404(Person, pk=person_id)
    personform = PersonForm(instance=object_person_id)
    if request.method == 'POST':
        personform = PersonForm(request.POST, instance=object_person_id)
        personform.save()
        return HttpResponse('Данные обновлены успешно.')
    data = {'form': personform}
    return render(request, 'person.html', context=data)
