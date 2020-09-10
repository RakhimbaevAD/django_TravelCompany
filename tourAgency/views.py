from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib import messages

from .models import Hotel, Services, Hotel_photos, Reviews, Food_in_hotel, Orders, Food_type
from .forms import ReviewForm, CreateUserForm, OrderForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class RegisterView(View):
    '''Регистрация'''
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('main')
        form = CreateUserForm(request.GET)
        return render(request, 'tourAgency/register.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('main')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Пользователь с логином ' + user + ' создан' )
        return redirect('login')

class LoginView(View):
    '''Страница входа'''
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('main')
        return render(request, 'tourAgency/login.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('main')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Неверный Пароль или Имя пользователя')
        return render(request, 'tourAgency/login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')

class HotelsView(View):
    '''Список отелей'''
    def get(self, request):
        hotels = Hotel.objects.all()
        return render(request, 'tourAgency/hotel_list.html', {'hotel_list':hotels})

class HotelDetailView(View):
    '''Подробная информация об отеле'''
    def get(self, request, slug):
        hotel = Hotel.objects.get(url=slug)
        hotel.services = Services.objects.get(hotel_id=hotel.id)
        hotel.photos = Hotel_photos.objects.filter(hotel_id=hotel.id)
        hotel.reviews = Reviews.objects.filter(hotel_id=hotel.id)
        return render(request, 'tourAgency/hotel_detail.html', {'hotel': hotel})


class AddReview(View):
    '''Отзыв'''
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        hotel = Hotel.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.hotel = hotel
            form.save()
        return redirect(hotel.get_absolut_url())

class OrderView(View):
    '''Бронирование отеля'''
    def get(self, request, slug):
        if not request.user.is_authenticated:
            return redirect('login')
        hotel = Hotel.objects.get(url=slug)
        foodInHotel = Food_in_hotel.objects.filter(hotel_id=hotel.id)
        user = request.user
        return render(request, 'tourAgency/order.html', {'hotel': hotel, 'foodInHotel': foodInHotel, 'user': user})

    def post(self, request, slug):
        if not request.user.is_authenticated:
            return redirect('login')
        form = OrderForm(request.POST)
        hotel = Hotel.objects.get(url=slug)
        food_type = form.data['food_type']
        days = form.data['days_number']
        persons = form.data['persons_number']

        food_price = Food_in_hotel.objects.get(hotel_id=hotel.id, food_type_id=food_type)
        user = request.user
        #food_price = foodInHotel.objects.get(food_type_id=food_type)
        total_price = (hotel.price + food_price.price) * (int(days) * int(persons))

        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.hotel = hotel
            form.price = total_price
            form.save()

        return redirect('my_orders')


class MyOrdersView(View):
    '''Мои бронирования'''
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        orders = Orders.objects.filter(user_id=request.user).select_related()
        for order in orders:
            order.hotel = Hotel.objects.get(id=order.hotel.id)
            order.ftype = Food_type.objects.get(id=order.food_type.pk)
        return render(request, 'tourAgency/my_order.html', {'orders': orders})