from django.shortcuts import render, get_object_or_404, redirect
from .models import Breed, Dog, Pet
from .forms import PetForm

# View для отображения списка пород
def breed_list(request):
    """
    Отображает список всех пород животных.

    :param request: объект HTTP-запроса
    :return: рендер страницы с списком пород
    """
    breeds = Breed.objects.all()
    return render(request, 'dogs/breed_list.html', {'breeds': breeds})


# View для отображения списка собак
def dog_list(request):
    """
    Отображает список всех собак.

    :param request: объект HTTP-запроса
    :return: рендер страницы с списком собак
    """
    dogs = Dog.objects.all()
    return render(request, 'dogs/dog_list.html', {'dogs': dogs})


# View для отображения списка питомцев
def list_pets(request):
    """
    Отображает список всех питомцев.

    :param request: объект HTTP-запроса
    :return: рендер страницы с списком питомцев
    """
    pets = Pet.objects.all()
    context = {'pets': pets}
    return render(request, 'dogs/pet_list.html', context)


# View для создания нового питомца
def create_pet(request):
    """
    Создает нового питомца и добавляет его в базу данных.

    :param request: объект HTTP-запроса
    :return: рендер страницы с формой создания или редирект на список питомцев
    """
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pets')  # Перенаправление на список питомцев
    else:
        form = PetForm()  # Пустая форма для создания
    context = {'form': form}
    return render(request, 'dogs/pet_form.html', context)


# View для обновления информации о питомце
def update_pet(request, pk):
    """
    Обновляет данные существующего питомца.

    :param request: объект HTTP-запроса
    :param pk: первичный ключ питомца
    :return: рендер страницы с формой обновления или редирект на список питомцев
    """
    pet = get_object_or_404(Pet, pk=pk)  # Получение объекта или 404
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('list_pets')  # Перенаправление на список питомцев
    else:
        form = PetForm(instance=pet)  # Форма с данными существующего питомца
    context = {'form': form}
    return render(request, 'dogs/pet_form.html', context)


# View для удаления питомца
def delete_pet(request, pk):
    """
    Удаляет питомца из базы данных.

    :param request: объект HTTP-запроса
    :param pk: первичный ключ питомца
    :return: рендер страницы подтверждения удаления или редирект на список питомцев
    """
    pet = get_object_or_404(Pet, pk=pk)  # Получение объекта или 404
    if request.method == 'POST':  # Проверка, что запрос POST (подтверждение удаления)
        pet.delete()
        return redirect('list_pets')  # Перенаправление на список питомцев
    context = {'pet': pet}
    return render(request, 'dogs/pet_confirm_delete.html', context)
