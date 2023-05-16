from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from Application.models import User, Category, Product
from Application.verification import send_otp, send_email
from Application.check_phone import check_phone_num

# Create your views here.


'Index Page Start'
class Index:
    def home(self, request):
        all_products = Product.objects.all().order_by('-id')[:12]
        
        new_arrivals = Product().limit_get_new_arrivals_items() 

        if Category.objects.filter(name='Accessories').exists():
            accessories_id = Category.objects.get(name='Accessories')
            accessories = Product.objects.filter(category=accessories_id.id).order_by('-id')[:12]
        else:
            accessories = None

        if Category.objects.filter(name='Beauty').exists():
            beauty_id = Category.objects.get(name='Beauty')
            beauty = Product.objects.filter(category=beauty_id.id).order_by('-id')[:12]
        else:
            beauty = None


        context = {
            'all_products': all_products,
            'accessories': accessories,
            'beauty': beauty,
            'new_arrivals': new_arrivals
        }

        return render(request, 'index.html',
                    context)


    def product(self, request, id):

        context = {
            "id": id
        }
        return render(request, 'others/product.html',
                      context)

    
    def search(self, request):
        if request.method == "POST":
            search = request.POST["search"]
            context = {
                "search": search
            }
            return render(request, 'search.html',
                    context)
        
        return render(request, 'search.html')



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
                send_email(name, email, otp)

                user = User.objects.create_user(username=name, email=email, password=password, phone_number=new_phone_method, address=address, city=city, country=country, otp=otp)
                user.save()

                return redirect(f"/account_verification/{user.id}")


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

            user = User.objects.get(id=pk)
            if user.otp == otp:
                user.is_verified = True
                user.save()

                return redirect("/login")
            
            messages.info(request, "Entered a wrong code. Please check the number and try again!")
            return redirect(f"/account_verification/{pk}")

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
