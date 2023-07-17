from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from apps.product_module.models import Product
from apps.shopping_cart_module.models import Order, OrderDetail


# Create your views here.

@method_decorator(login_required,name='dispatch')
class User_Cart(ListView):
    template_name = "shopping_cart_module/user_cart.html"
    model = Order

    def get_queryset(self):
        query = super(User_Cart, self).get_queryset()

        return query

    def get_context_data(self, **kwargs):
        print(self.request.user.id)
        context = super(User_Cart, self).get_context_data(**kwargs)
        current_order = Order.objects.prefetch_related('order_products').filter(is_paid=False,
                                                                                user_id=self.request.user.id).first()
        context['order'] = current_order
        total = 0
        for order in current_order.order_products.all():
            total += order.product.price * order.count
        context['total'] = total
        return context

@login_required()
def delete_order(request: HttpRequest):
    order_detail_id = request.GET.get('order_detail_id')
    print(order_detail_id)
    if order_detail_id is None:
        JsonResponse({
            "status": "order detail not found"
        })
    else:
        current_order, created = Order.objects.prefetch_related('order_products').get_or_create(is_paid=False,
                                                                                                user_id=request.user.id)
        order_detail = current_order.order_products.filter(id=order_detail_id).first()
        if order_detail is None:
            return JsonResponse({
                "response": "order_not_found"
            })
        else:
            order_detail.delete()

    current_order, created = Order.objects.prefetch_related('order_products').get_or_create(is_paid=False,
                                                                                            user_id=request.user.id)

    context = {
        'order': current_order
    }
    data = render_to_string('shopping_cart_module/user_cart_content.html', context)
    return JsonResponse(
        {"status": 'success',
         "response": data

         }
    )

@login_required()

def add_to_order(request: HttpRequest):
    product_id = request.GET.get('product_id')
    print(product_id)
    count = request.GET.get('count')
    if request.user.is_authenticated:
        product: Product = Product.objects.filter(id=product_id, is_delete=False, is_active=True).first()
        if product is not None:

            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail: OrderDetail = current_order.order_products.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += int(count)
                current_order_detail.save()
            else:
                new_order_detail: OrderDetail = OrderDetail(order_id=current_order.id, product_id=product_id,
                                                            count=count)
                new_order_detail.save()
            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse({
                "status": "product not found"
            })
    else:
        return JsonResponse({
            "response": "please login"
        })

@login_required()

def change_order_cart(request: HttpRequest):
    order_detail_id = request.GET.get('order_detail_id')
    state = request.GET.get('state')

    if order_detail_id is None:
        return JsonResponse(
            {
                'status': 'not_found'
            })
    current_order, created = Order.objects.prefetch_related('order_products').get_or_create(is_paid=False,
                                                                                            user_id=request.user.id)
    order_detail = current_order.order_products.filter(id=order_detail_id).first()
    if order_detail is None:
        return JsonResponse(
            {
                'status': 'not_found'
            })
    if state == "increase":
        order_detail.count += 1
        order_detail.save()
    elif state == "decrease" :
        if order_detail.count == 1 :
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else :
        return JsonResponse(
            {
                'status': 'not_valid'
            })
    current_order, created = Order.objects.prefetch_related('order_products').get_or_create(is_paid=False,
                                                                                            user_id=request.user.id)

    context = {
        'order': current_order
    }
    data = render_to_string('shopping_cart_module/user_cart_content.html', context)
    return JsonResponse(
        {"status": 'success',
         "response": data

         }
    )

