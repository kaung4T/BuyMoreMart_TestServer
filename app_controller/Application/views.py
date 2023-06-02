from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import auth
from django.contrib import messages
from django.http import Http404
from app_controller.Application.models import User, Category, Product, Product_type
from app_controller.Application.verification import send_otp, send_email
from app_controller.Application.check_phone import check_phone_num
from app_controller.Order.models import Cart
from app_controller.Website_Interface.models import Info, Header_ImageGroup, Index_ImageGroup

# Create your views here.


'Index Page Start'
class Index:
    def home(self, request):
        # Info
        if Info.objects.filter(id=1).exists():
            info = Info.objects.get(id=1)
        else:
            info = None

        # Header Image
        if Header_ImageGroup.objects.filter(id=1).exists():
            header_image = Header_ImageGroup.objects.get(id=1)
        else:
            header_image = None


        # Index Image
        if Index_ImageGroup.objects.filter(id=1).exists():
            index_image = Index_ImageGroup.objects.get(id=1)
        else:
            index_image = None

        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

        all_products = Product.objects.all().order_by('-id')[:12]
        
        new_arrivals = Product().limit_new_items()
        discount = Product().limit_discount_items()

        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        if Category.objects.filter(id=1).exists():
            foods_id = Category.objects.get(id=1)
            foods = Product.objects.filter(category=foods_id.id).order_by('-id')[:12]
        else:
            foods = None

        if Category.objects.filter(id=2).exists():
            accessories_id = Category.objects.get(id=2)
            accessories = Product.objects.filter(category=accessories_id.id).order_by('-id')[:12]
        else:
            accessories = None

        if Category.objects.filter(id=3).exists():
            beauty_id = Category.objects.get(id=3)
            beauty = Product.objects.filter(category=beauty_id.id).order_by('-id')[:12]
        else:
            beauty = None


        context = {
            'info': info,
            'header_image': header_image,
            'index_image': index_image,
            
            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            'all_products': all_products,
            'foods': foods,
            'accessories': accessories,
            'beauty': beauty,
            'discount': discount,
            'new_arrivals': new_arrivals,
            'cart_noti': cart_len     
        }
        return render(request, 'index.html',
                    context)

    
    def search(self, request):
        # header product types
        header_food = Product_type.objects.filter(category=1)
        header_accessories = Product_type.objects.filter(category=2)
        header_beauty = Product_type.objects.filter(category=3)

        if request.method == "POST":
            search = request.POST["search"]

            if request.user.is_authenticated:
                cart = Cart.objects.filter(user=request.user)
                cart_len = len(list(cart))
            else:
                cart_len = 0

            if Product.objects.filter(title__icontains=search).exists():
                product = Product.objects.filter(title__icontains=search)
                total_item = len(list(product.values()))
            else:
                product = None
                total_item = 0
            
            p = Paginator(product, 12)
            page = request.GET.get("page")

            if product is not None:
                items = p.get_page(page)
            else:
                items = None

            context = {
                'header_food': header_food,
                'header_accessories': header_accessories,
                'header_beauty': header_beauty,

                "search": search,
                "items": items,
                "total_item": total_item,
                "cart_noti": cart_len
            }
            return render(request, 'search.html',
                    context)

        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            cart_len = len(list(cart))
        else:
            cart_len = 0

        context = {
            'header_food': header_food,
            'header_accessories': header_accessories,
            'header_beauty': header_beauty,

            "cart_noti": cart_len
        }
        
        return render(request, 'search.html',
                    context)



class Account:
    def registration(self, request):
        if request.method == "POST":
            phone = request.POST["phone"]
            name = request.POST["name"]
            email = request.POST["email"]
            password = request.POST["password"]
            password2 = request.POST["password2"]
            address = request.POST["address"]
            city = request.POST["city"]
            country = request.POST["country"]

            new_phone_method = check_phone_num(phone)

            if password == password2:
                if User.objects.filter(username=name).exists():
                    user = User.objects.get(username=name)
                    if user.is_verified == True:
                        messages.info(request, "Username already exists!")
                        return redirect("/registration")
                    else:
                        user.delete()

                if User.objects.filter(phone_number=new_phone_method).exists():
                    user = User.objects.get(phone_number=new_phone_method)
                    if user.is_verified == True:
                        messages.info(request, "Phone number already exists!")
                        return redirect("/registration")
                    else:
                        user.delete()

                if User.objects.filter(email=email).exists():
                    user = User.objects.get(email=email)
                    if user.is_verified == True:
                        messages.info(request, "Email already exists!")
                        return redirect("/registration")
                    else:
                        user.delete()


                otp = send_otp(phone)
                # send_email(name, email, otp)

                user = User.objects.create_user(username=name, email=email, password=password, phone_number=new_phone_method, address=address, city=city, country=country, otp=otp)
                user.is_verified = True
                user.save()

                # we skip verify step
                # return redirect(f"/account_verification/{user.id}")

                messages.success(request, "Your account has been successfully created! You can now login and access our service.")
                return redirect("login")

            else:
                messages.info(request, "Passwords do not match!")
                return redirect("/registration")


            return redirect("/login")

        return render(request, "registration.html")
    

    def login(self, request):
        if request.method == "POST":
            phone = request.POST["phone"]
            password = request.POST["password"]

            phone = check_phone_num(phone)

            if User.objects.filter(phone_number=phone).exists():
                # for customer
                check_user = User.objects.get(phone_number=phone)

                user = auth.authenticate(username=check_user.username, password=password)

            else:
                user = None

            
            if user:
                if user.is_verified == True:
                    auth.login(request, user)
                    
                    return redirect("index")
                else:
                    messages.info(request, "Your account wasn't verified. Please try again with same phone-number and email!")
                    return redirect("login")

            else:
                messages.info(request, "Sorry, we couldn't find an account with that phone number!")
                return redirect("login")

        return render(request, "login.html")
    

    def logout(self, request):
        auth.logout(request)
        return redirect("/")


    def account_verification(self, request, pk):
        if request.method == "POST":
            otp = request.POST["otp"]

            try:
                user = User.objects.get(id=pk)
            except Exception:
                raise Http404

            if user.otp == otp:
                user.is_verified = True
                user.save()

                messages.success(request, "Your account has been successfully created! You can now login and access our service.")
                return redirect("/login")
            
            messages.info(request, "Entered a wrong code. Please check the number and try again!")
            return redirect(f"/account_verification/{pk}")

        try:
            user = User.objects.get(id=pk)
        except Exception:
            raise Http404

        context = {
            "user_id": pk
        }

        return render(request, "account_verification.html",
                    context)

    
    def account_resend_otp(self, request, pk):

        user = User.objects.get(id=pk)
        
        otp = send_otp(user.phone_number)
        send_email(user.username, user.email, otp)

        user.otp = otp
        user.save()
        
        return redirect(f"/account_verification/{pk}")
