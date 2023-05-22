from django.shortcuts import render, redirect
from app_controller.Application.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from app_controller.Application.verification import send_otp, send_email

class Profile:
    def home(self, request):
        if request.method == "POST":
            phone = request.POST["phone"]
            name = request.POST["name"]
            email = request.POST["email"]
            address = request.POST["address"]
            city = request.POST["city"]
            country = request.POST["country"]

            if request.user.is_authenticated:
                user = User.objects.get(id=request.user.id)
                
                if phone:
                    user.phone_number = phone
                elif name:
                    user.username = name
                elif email:
                    user.email = email
                elif address:
                    user.address = address
                elif city:
                    user.city = city
                elif country:
                    user.country = country

                user.save()

            messages.info(request, "Please register an account!")
            return redirect("profile")

        if request.user.is_authenticated == False:
            return redirect("login")

        return render(request, 'others/profile.html')


    def security(self, request):
        if request.method == "POST":
            password = request.POST["password"]
            password2 = request.POST["password2"]

            if password == password2:
                if request.user.is_authenticated:
                    user = User.objects.get(id=request.user.id)

                    otp = send_otp(user.phone_number)
                    send_email(user.username, user.email, otp)

                    user.otp = otp
                    user.save()

                    return redirect(f"profile_verification/{password}")
                
                messages.info(request, "Please register an account!")
                return redirect("security")
            
            else:
                messages.info(request, "Passwords do not match!")
                return redirect("security")

        return render(request, 'others/profile_password.html')
        

    def profile_verification(self, request, new_password):
        if request.method == "POST":
            otp = request.POST["otp"]
            
            if request.user.is_authenticated:
                user = User.objects.get(id=request.user.id)

                if user.otp == otp:
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)
                    return redirect("security")

                else:
                    context = {
                        "new_password": new_password
                    }
                    messages.info(request, "Entered a wrong code. Please check the number and try again!")
                    return render(request, "others/profile_verification.html",
                                    context)
            
            
            messages.info(request, "Please register an account!")
            return redirect("registration")
        
        if request.user.is_authenticated:
            context = {
                "new_password": new_password
            }

            return render(request, "others/profile_verification.html",
                                    context)
        
        else:
            return redirect("registration")

