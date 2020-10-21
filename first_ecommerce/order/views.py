from django.shortcuts import render, reverse

# Create your views here.
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])  
            # clear the cart
            cart.clear()
            return render(request,
                          'order/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'order/order/create.html',
                  {'cart': cart, 'form': form})

def created(self):
    return reverse('order/order/created.html')