
# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import Product, FeedbackModel, ProductImport
from .models import Category_products
from .models import CustomerUser, Cart, Order, ProductSold
from django.views import View
from .form import Register
from .form import Contact
from django.http import JsonResponse, HttpResponse , Http404
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib import messages
from datetime import datetime, date
from .filters import SearchFilter
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from fpdf import FPDF
import os

from django.conf import settings

# Create your views here.
url_path = ""

def get_number_product_cart(id_user, count):

    cart_product = Cart.objects.filter(Cart_user_id=id_user)
    for product in cart_product:
        count += product.Cart_quantity

    return count


def view_product(request):
    global url_path
    url_path = "/product/"
    query_dict ={}
    user_name = ""
    user_id =""
    count = 0
    try:
        query_dict = {
            "Pr_name": request.GET["Pr_name"].capitalize(),
            "encoding": 'utf-8'
        }
    except Exception as e:
        pass
    if "login" in request.session:
        user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
        user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
        count = get_number_product_cart(user_id, count)

    list_product = Product.objects.all()
    list_product_active =list_product.filter(Pr_active=True)
    product_filter = SearchFilter(query_dict, queryset=list_product_active)

    list_active = {'form': product_filter.form,'product': product_filter.qs, "active": ['active', '', '', '', ''],
                   "user_name": user_name, "user_id":user_id, "count":count}
    return render (request, 'homepage/shop.html',  list_active )


def view_category(request):
    global url_path
    url_path = "/raucu"
    user_name = ""
    user_id = ""
    count = 0
    query_dict ={}
    try:
        query_dict = {
            "Pr_name": request.GET["Pr_name"].capitalize(),
            "encoding": 'utf-8'
        }
    except Exception as e:
        pass

    if "login" in request.session:
        user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
        user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
        count = get_number_product_cart(user_id, count)

    product_raucu = Product.objects.filter(Pr_category= Category_products.objects.get(Cpr_name="Rau củ"))
    product_filter = SearchFilter(query_dict, queryset=product_raucu)

    context = {"form": product_filter.form, "product": product_filter.qs,  "active": ['', 'active', '', '', ''],
               "user_name":user_name, "user_id": user_id, "count": count}
    return render (request, 'homepage/shop.html', context)


def view_category1(request):
    global url_path
    url_path = "/traicay"
    user_name = ""
    user_id = ""
    count = 0
    query_dict = {}
    try:
        query_dict = {
            "Pr_name": request.GET["Pr_name"].capitalize(),
            "encoding": 'utf-8'
        }
    except Exception as e:
        pass
    if "login" in request.session:
        user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
        user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
        count = get_number_product_cart(user_id, count)

    product_traicay = Product.objects.filter(Pr_category= Category_products.objects.get(Cpr_name="Trái cây"))
    product_filter = SearchFilter(query_dict, queryset=product_traicay)

    context = {"form": product_filter.form, "product": product_filter.qs,  "active": ['', '', 'active', '', ''],"user_name":user_name, "user_id":user_id, "count": count}
    return render (request, 'homepage/shop.html', context)


def view_category2(request):
    global url_path
    url_path = "/nuocep"
    user_name = ""
    user_id = ""
    count = 0
    query_dict = {}
    try:
        query_dict = {
            "Pr_name": request.GET["Pr_name"].capitalize(),
            "encoding": 'utf-8'
        }
    except Exception as e:
        pass
    if "login" in request.session:
        user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
        user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
        count = get_number_product_cart(user_id, count)
    product_nuocep = Product.objects.filter(Pr_category= Category_products.objects.get(Cpr_name="Nước ép"))
    product_filter = SearchFilter(query_dict, queryset=product_nuocep)
    context = {"form": product_filter.form, "product": product_filter.qs,  "active": ['', '', '', 'active', ''], "user_name":user_name, "user_id":user_id, "count": count}
    return render (request, 'homepage/shop.html', context)


def view_category3(request):
    global url_path
    url_path = "/cacloaihat"
    user_name = ""
    user_id = ""
    count = 0
    query_dict = {}
    try:
        query_dict = {
            "Pr_name": request.GET["Pr_name"].capitalize(),
            "encoding": 'utf-8'
        }
    except Exception as e:
        pass
    if "login" in request.session:
        user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
        user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
        count = get_number_product_cart(user_id, count)
    product_cacloaihat = Product.objects.filter(Pr_category= Category_products.objects.get(Cpr_name="Các loại hạt"))
    product_filter = SearchFilter(query_dict, queryset=product_cacloaihat)

    context = {"form": product_filter.form, "product": product_filter.qs,  "active": ['', '', '', '', 'active'], "user_name":user_name, "user_id":user_id, "count":count}
    return render (request, 'homepage/shop.html', context)


def detailproduct(request, id):
    detailproduct = Product.objects.get(Pr_id=id)
    user_name = ""
    user_id = ""
    count = 0
    if "login" in request.session:
        user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
        user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
        count = get_number_product_cart(user_id, count)
    context = {'detail': detailproduct, "user_name":user_name, "user_id":user_id, "count":count}
    return render (request, 'homepage/product-single.html', context)

def view_index(request):
    global url_path
    url_path = "/"
    user_name = ""
    user_id = ""
    count = 0
    view_index = Product.objects.filter(Pr_sale=True)
    if "login" in request.session:
        user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
        user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
        count = get_number_product_cart(user_id, count)
    context = {'view_index': view_index, "user_name": user_name, "user_id":user_id, "count":count}
    return render (request, 'homepage/index.html', context)


#Login Register

class LoginUser(View):
    def get(self,request):
        return render(request, 'homepage/login_user.html')

    def post(self, request):
        # post cho đăng nhập
        try:
            user_name = request.POST.get('Username')
            password = request.POST.get('Password')
            my_user = CustomerUser.objects.get(U_gmail=user_name, U_password=password)
            request.session['login'] = my_user.U_id
            return redirect(url_path)
            # return render(request, 'homepage/index.html', context)
        except ObjectDoesNotExist:
            messages.error(request, "Email hoặc mật khẩu không đúng")
            return redirect("/login")



class RegisterUser(View):

    def get(self, request):
        form_customer = Register()
        context = {'customer': form_customer}
        return render(request, 'homepage/register_user.html', context)

    def post(self, request):
        q = Register(request.POST)
        # post đăng kí
        if q.is_valid():
            email = q.cleaned_data["U_gmail"]
            if CustomerUser.objects.filter(U_gmail=email).exists():
                messages.error(request, "Email đã tồn tại")
                return redirect("/register")
            else:
                q.save()
                return redirect("/login")
        else:
            return redirect("/login")

def log_out(request):
    if "login" in request.session:
        del request.session["login"]

    return redirect(url_path)


class Views_contact(View):
     def get(self, request):
         user_name = ""
         user_id = ""
         count = 0
         if "login" in request.session:
             form = Contact(initial={'Fb_user_id': request.session["login"]})
             user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
             user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
             count = get_number_product_cart(user_id, count)
             context = {'user_name':user_name,'user_id':user_id,'contact': form,'count':count,}
             return render(request, 'homepage/contact.html',context)
         else:
             return redirect("/login")

     def post(self,request):
         c = Contact(request.POST)
         user_name = ""
         user_id = ""
         count = 0
         if c.is_valid():
             c.save()
             form = Contact(initial={'Fb_user_id': request.session["login"]})
             user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
             user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
             count = get_number_product_cart(user_id, count)
             context = {'user_name': user_name, 'user_id': user_id, 'contact': form, 'count': count,}
             messages.success(request, "Gửi thành công...")
             return render(request, 'homepage/contact.html', context)
         else:
             messages.error(request, "Gửi thất bại...")



class Views_blog(View):
     def get(self, request):
         user_name = ""
         user_id = ""
         if "login" in request.session:
             user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
             user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
         context ={"user_name":user_name, "user_id":user_id}
         return render(request, 'homepage/blog.html',context)



class Views_about(View):    
    def get(self, request):
        user_name=""
        user_id=""
        count = 0
        if "login" in request.session:
            user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
            user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
            count = get_number_product_cart(user_id, count)
        context={"user_name":user_name, "user_id":user_id, "count":count}
        return render(request, 'homepage/about.html', context)



class Views_information(View):
    def get(self, request):
        user_name = ""
        user_id = ""
        count = 0
        id_user = request.session["login"]
        user_infomation = CustomerUser.objects.get(U_id=id_user)
        if "login" in request.session:
            user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
            user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
            count = get_number_product_cart(user_id, count)
        context = {'user_infomation':user_infomation, "user_name":user_name, "user_id":user_id, "count":count}
        return render(request, 'homepage/information_user.html',context)

    def post(self, request):
        user_name = ""
        user_id = ""
        count = 0
        id_user = request.POST.get('id_user')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gmail = request.POST.get('emailaddress')
        user = CustomerUser.objects.get(U_id=id_user)
        user.U_name = name
        user.U_phone = phone
        user.U_address = address
        user.U_gmail = gmail
        user.save()
        user_infomation = CustomerUser.objects.get(U_id=id_user)
        if "login" in request.session:
            user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
            user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
            count = get_number_product_cart(user_id, count)
        context = {'user_infomation':user_infomation, "user_name":user_name, "user_id":user_id, "count": count}
        messages.success(request, "Cập nhật thông tin thành công")
        return render(request, 'homepage/information_user.html', context)
    


class View_resetpass(View):
    def get(self, request):
        user_name = ""
        user_id = ""
        count = 0
        if "login" in request.session:
            user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
            user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
            count = get_number_product_cart(user_id, count)
        context = {"user_name": user_name, "user_id":user_id, "count":count}
        return render(request, 'homepage/resetpass.html', context)

    def post(self, request):
        user_name = ""
        user_id = ""
        count = 0
        id_user = request.session["login"]
        mk = request.POST.get('Matkhaucu')
        mkmoi = request.POST.get('Matkhaumoi')
        nhaplaimkmoi = request.POST.get('Nhaplaimatkhau')

        user = CustomerUser.objects.get(U_id=id_user)
        mk_user = user.U_password
        if mk_user == mk:
            if mkmoi == nhaplaimkmoi:
                user.U_password = mkmoi
                user.save()
                messages.success(request, "Đổi mật khẩu thành công")
            else:
                messages.error(request, "Nhập lại mật khẩu không khớp")
        else:
            messages.error(request, "Mật khẩu cũ không đúng")
        if "login" in request.session:
            user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
            user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
            count = get_number_product_cart(user_id, count)
        context = {"user_name": user_name, "user_id":user_id, "count": count}
        return render(request, 'homepage/resetpass.html', context)



@csrf_exempt
def check_login(request):
    if request.is_ajax() and request.method == "GET":
        if 'login' in request.session:
            return JsonResponse({"login": True})
        else:
            return JsonResponse({"login": False})



@csrf_exempt
def addcart(request):
    if request.is_ajax() and request.method == "POST":
        if request.session['login']:
            id_user = request.session["login"]
            id = int(request.POST.get('id'))
            product = Product.objects.get(Pr_id=id)
            quantity = int(request.POST.get('quantity'))
            real_quantity = product.Pr_quantity

            try:
                cart_product = Cart.objects.get(Cart_pr_id=id, Cart_user_id=id_user)
                if quantity > real_quantity:
                    return JsonResponse({"message": "Số lượng sản phẩm chỉ còn %s" % real_quantity}, status=400)
                cart_product.Cart_quantity = cart_product.Cart_quantity + quantity
                cart_product.save()

            except ObjectDoesNotExist:
                if quantity > real_quantity:
                    return JsonResponse({"message": "Số lượng sản phẩm chỉ còn %s" % real_quantity}, status=400)

                cart = Cart(Cart_user_id=id_user, Cart_price=product.Pr_price, Cart_pr_id=product.Pr_id,
                            Cart_pr_name=product.Pr_name,
                            Cart_quantity=quantity,
                            Cart_product_image=product.Pr_image)
                cart.save()

            product.Pr_quantity -= quantity
            product.save()

            return JsonResponse({"login": True, "status": True, "quantity": quantity})

        else:

            return JsonResponse({"login": False})


def detailcart(request, id):
    user_name = ""
    user_id=""
    cart_detail = Cart.objects.filter(Cart_user_id=id)
    total = 0
    count = 0
    for cart in cart_detail:
        total += (cart.Cart_quantity * cart.Cart_price)
    request.session["total"] = total
    if "login" in request.session:
        user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
        user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
        count = get_number_product_cart(user_id, count)
    context = {'cart_detail': cart_detail, "user_name": user_name, "user_id":user_id, "count":count}
    return render(request, 'homepage/cart.html', context)



@csrf_exempt
def removecart(request):
    if request.is_ajax() and request.method == "POST":
        if request.session['login']:
            id_user = request.session["login"]
            id = int(request.POST.get('id').split("#")[1])
            cart_id = Cart.objects.get(Cart_user_id=id_user, Cart_pr_id=id)
            cart_id.delete()
    return JsonResponse({'message': True})



class detailcheckout(View):
    def get(self, request):
        user_name = ""
        user_id= ""
        count = 0
        id_user = request.session["login"]
        user_infomation = CustomerUser.objects.get(U_id=id_user)
        total = request.session["total"]
        if "login" in request.session:
            user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
            user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
            count = get_number_product_cart(user_id, count)
        context = {"total": total, "user": user_infomation, "user_name": user_name, "user_id":user_id, "count":count}
        return render(request, 'homepage/checkout.html', context=context)

    def post(self, request):
        id_user = request.session["login"]
        cartcheckout = Cart.objects.filter(Cart_user_id=id_user)
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        time_stamp = int(datetime.today().timestamp())
        today = date.today().strftime("%Y-%m-%d")
        for cart in cartcheckout:
            order = Order(Od_id=time_stamp, Od_user_id=id_user, Od_pr_id=cart.Cart_pr_id,
                          Od_quantity=cart.Cart_quantity, Od_price=cart.Cart_price * cart.Cart_quantity, Od_name=name,
                          Od_address=address, Od_phone=phone)
            order.save()
            try:
                product_exist = ProductSold.objects.get(name=cart.Cart_pr_name,create_at=today)
                product_exist.quantity = product_exist.quantity + int(cart.Cart_quantity)
                product_exist.price = product_exist.price + (cart.Cart_price * cart.Cart_quantity)
                product_exist.save()
            except ObjectDoesNotExist:
                product_sold = ProductSold(name=cart.Cart_pr_name,create_at=today, quantity=cart.Cart_quantity, price=cart.Cart_price * cart.Cart_quantity)
                product_sold.save()

            product = Product.objects.get(Pr_id=cart.Cart_pr_id)
            product.Pr_buy = product.Pr_buy + cart.Cart_quantity
            product.save()

            cart.delete()
        messages.success(request, "Bạn đã đặt hàng thành công")

        return redirect("/product")




def Views_pendingpPr(request):
    user_name = ""
    user_id=""
    count = 0
    id_user = request.session["login"]
    pending_products = Order.objects.filter(Od_user_id=id_user)
    list_order = []
    for item in pending_products:
        temp_object = {
            "time": datetime.fromtimestamp(item.Od_id).strftime('%d-%m-%y %H:%M'),
            "od_id": item.Od_id,
            "price": item.Od_price,
            "status": item.Od_status
        }
        flag = False
        if list_order:
            for order in list_order:
                if order["od_id"] == temp_object["od_id"]:
                    order["price"] += temp_object["price"]
                    flag = True
                    break
            if not flag:
                list_order.append(temp_object)
        else:
            list_order.append(temp_object)
    if "login" in request.session:
        user_name = CustomerUser.objects.get(U_id=request.session["login"]).U_name
        user_id = CustomerUser.objects.get(U_id=request.session["login"]).U_id
        count = get_number_product_cart(user_id, count)
    context = {'pending_products': list_order, "user_name": user_name, "user_id":user_id, "count":count}
    return render(request, 'homepage/pendingproduct.html',context)



@csrf_exempt
def detailorder(request):
    if request.is_ajax and request.method == "GET":

        madonhang = request.GET.get("order_id")
        order = Order.objects.filter(Od_id=madonhang)

        # thông tin chung cả đơn hàng
        detail_order = {
            "id": madonhang,
            "time":  datetime.fromtimestamp(int(madonhang)).strftime('%d-%m-%y %H:%M'),
            "total": 0,
            "address": order[0].Od_address,
            "name":  order[0].Od_name,
            "phone":  order[0].Od_phone
        }
        list_product = []
        for sanpham in order:
            a = Product.objects.get(Pr_id=sanpham.Od_pr_id)

            temp_object = {
                'image': str(a.Pr_image),
                'name': a.Pr_name,
                "quality": sanpham.Od_quantity,
                "price": sanpham.Od_price

            }
            detail_order["total"] += temp_object["price"]
            list_product.append(temp_object)


        detail_order["detail_order"] = list_product
    return JsonResponse(detail_order, status=200)



@login_required(login_url='/admin/login/')
def manage(request):
    user_object = User.objects.get(username=request.user)
    context = {"user": user_object, "has_permission": True, "site_url": '/'}
    return render(request,'admin/quanlydonhang.html', context)


@login_required(login_url='/admin/login/')
def statistic(request):
    user_object = User.objects.get(username=request.user)
    context = {"user": user_object, "has_permission": True, "site_url": '/'}
    return render(request,'admin/thongke.html', context)



def get_all_order(request):
    if request.is_ajax and request.method == "GET":
        result = []
        orders = Order.objects.all().order_by('Od_id')
        for order in orders:
            if len(result) > 0:
                if order.Od_id not in [t["ord_id"] for t in result]:
                    result.append({
                        "ord_id": order.Od_id,
                        "time": datetime.fromtimestamp(int(order.Od_id)).strftime('%d-%m-%y %H:%M'),
                        "status": order.Od_status
                    })
                else:
                    continue
            else:
                result.append({
                    "ord_id": order.Od_id,
                    "time": datetime.fromtimestamp(int(order.Od_id)).strftime('%d-%m-%y %H:%M'),
                    "status": order.Od_status
                })
        response = {"result": result}
        return JsonResponse(response, status=200)


def change_state(request):
    if request.is_ajax and request.method == "GET":
        madonhang = request.GET.get("order_id")
        orders = Order.objects.filter(Od_id=madonhang)
        for order in orders:
            order.Od_status = order.Od_status + 1
            order.save()

        response = {"status": True}
        return JsonResponse(response, status=200)


def change_state_remove(request):
    if request.is_ajax and request.method == "GET":
        madonhang = request.GET.get("order_id")
        orders = Order.objects.filter(Od_id=madonhang)
        for product in orders:
            a = Product.objects.get(Pr_id=product.Od_pr_id)
            a.Pr_quantity = a.Pr_quantity + int(product.Od_quantity)
            product.Od_status = 4
            product.save()
        response = {"status": True}
        return JsonResponse(response, status=200)


def export_invoice(request, id):

    dir = os.path.dirname(os.path.abspath(__file__))
    dir_font = os.path.join(dir, r'dejavufont\\ttf\\DejaVuSansCondensed.ttf')

    order = Order.objects.filter(Od_id=id)

    # thông tin chung cả đơn hàng

    data_user = []
    ord_id = f'Mã đơn hàng: {id}'
    time = f'Thời gian: {datetime.fromtimestamp(int(id)).strftime("%d-%m-%y %H:%M")}'
    name = f'Họ tên: {order[0].Od_name}'
    phone = f'Số điện thoại: {order[0].Od_phone}'
    address = f'Địa chỉ: {order[0].Od_address}'
    data_user.append([ord_id, time, name, phone, address])

    data_product = [['Sản phẩm', 'Số lượng', 'Đơn giá', 'Tổng tiền']]
    sum_money = 0
    ship = 10
    for sanpham in order:
        a = Product.objects.get(Pr_id=sanpham.Od_pr_id)

        data_product.append([a.Pr_name, sanpham.Od_quantity, int(sanpham.Od_price / sanpham.Od_quantity), sanpham.Od_price])
        sum_money += sanpham.Od_price

    class PDF(FPDF):
        def header(self):
            # logo
            # self.image('../static/images/rau2.jpg',8,4,25)
            # font
            self.add_font('DejaVu', 'B', dir_font, uni=True)
            self.set_font('DejaVu', 'B', 15)
            # padding
            # title
            self.cell(0, 0, '', align='C')
            # ngắt dòng
            self.ln(1)

        def footer(self):
            self.set_y(-15)
            self.set_font('helvetica', 'I', 10)
            # số trang
            self.cell(0, 10, f'Trang {self.page_no()}', align='C')

    pdf = PDF('P', 'mm', (100, 200))

    # tạo tự động ngắt trang
    pdf.set_auto_page_break(auto=True, margin=15)

    # thêm trang
    pdf.add_page()
    #title
    pdf.set_font('DejaVu', 'B', 16)
    pdf.cell(30)
    pdf.cell(10, 10, 'Hóa đơn',ln=True)

    # thêm font chữ
    pdf.set_font('DejaVu', 'B', 14.0)
    # nội dung
    # width
    # height

    for row in data_user:
        for datum in row:
            # Enter data in colums
            pdf.cell(140, 10, str(datum), ln=True)

    pdf.cell(0, 5, '-------------------------------------------------', ln=True)
    epw = pdf.w - 2 * pdf.l_margin

    col_width = epw / 4

    # Text height is the same as current font size
    th = pdf.font_size
    pdf.ln(0)

    pdf.set_font('DejaVu', 'B', 10.0)
    pdf.ln(0.5)

    # Here we add more padding by passing 2*th as height
    for row in data_product:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 2 * th, str(datum), align='R')

        pdf.ln(2 * th)

    pdf.set_font('DejaVu', 'B', 14.0)
    pdf.cell(0, 5, '-------------------------------------------------', ln=True)
    pdf.cell(70, 5, 'Tổng:')
    pdf.cell(0, 5, str(sum_money), ln=True)

    pdf.set_font('DejaVu', 'B', 14.0)
    pdf.cell(0, 5, '-------------------------------------------------', ln=True)
    pdf.cell(73, 5, 'Ship:')
    pdf.cell(0, 5, str(ship), ln=True)

    pdf.set_font('DejaVu', 'B', 14.0)
    pdf.cell(0, 5, '-------------------------------------------------', ln=True)
    pdf.cell(70, 5, 'Tổng thanh toán:')
    pdf.cell(0, 5, str(sum_money+ship), ln=True)

    file_name = f'bill_{id}.pdf'
    pdf.output(os.path.join(dir, file_name))
    file_path = os.path.join(dir, file_name)
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/pdf")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response


def product_sold(request):
    if request.is_ajax and request.method == "GET":
        time = request.GET.get('time')
        products = ProductSold.objects.filter(create_at=time)
        result = []
        for product in products:
            result.append({
                "name": product.name,
                "quantity": product.quantity,
                "price": product.price
            })
        response = {'data': result}
        return JsonResponse(response, status=200)


def order_sold(request):
    if request.is_ajax and request.method == "GET":
        status_order = request.GET.get('status_order')
        time = request.GET.get('time')
        order = Order.objects.filter(Od_status=int(status_order),UpdateAt=time)
        result = []
        for orders in order:
            temp_object = {
                "id": orders.Od_id,
                "name": orders.Od_name,
                "price": orders.Od_price
            }
            flag = False
            if result:
                for order in result:
                    if order["id"] == temp_object["id"]:
                        order["price"] += temp_object["price"]
                        flag = True
                        break
                if not flag:
                    result.append(temp_object)
            else:
                result.append(temp_object)

        response = {'data': result}
        return JsonResponse(response, status=200)


def all_product(request):
    if request.is_ajax and request.method == "GET":
        products = Product.objects.all()
        result = []
        for product in products:
            result.append({
                "id": product.Pr_id,
                "name": product.Pr_name,
                "quantity": product.Pr_quantity,
                "quantity_sold": product.Pr_buy
            })
        response = {'data': result}
        return JsonResponse(response, status=200)


def product_import(request):
    if request.is_ajax and request.method == "GET":
        time = request.GET.get('time')
        products = ProductImport.objects.filter(UpdateAt=time)
        result = []
        for product in products:
            result.append({
                "name": product.name,
                "quantity": product.quantity,
                "price_import": product.import_price,
                "import": product.supplier,
                "total_money": product.import_price * product.quantity
            })
        response = {'data': result}
        return JsonResponse(response, status=200)