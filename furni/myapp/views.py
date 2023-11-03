from django.shortcuts import render,redirect
from . models import  Contact,User,Product,Wishlist,Cart
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.

def index(request):
    products=Product.objects.all()
    return render(request,"index.html",{'products':products})

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        msg="Contact Saved Successfully"
        return render(request,'contact.html',{'msg':msg})
    else:

        return render(request,'contact.html')

def signup(request):
    if request.method=='POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Is Already Registered"
            return render(request,'signup.html',{'msg':msg})

        except:
            if request.POST['password']==request.POST['cpassword']:   
            
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    phone=request.POST['phone'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    cpassword=request.POST['cpassword'],
                    usertype=request.POST['usertype'],
                    profile_pic=request.FILES['profile_pic'],
                )
                msg="User Sign Up Successfully"
                return render(request,'login.html',{"msg":msg})
            
            else:
                msg="Password And Confirm Password Does Not Match!Please Try Again"
                return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')
    
# def login(request):
#     if request.method=="POST":
#             try:
#                 user=User.objects.get(
#                         email=request.POST['email'],
#                         password=request.POST['password']
#                     )
#                 if user.usertype=='user':
#                             request.session['email']=user.email
#                             request.session['fname']=user.fname
#                             request.session['profile_pic']=user.profile_pic.url
#                             return render(request,'index.html')
#                 elif user.usertype=='seller':
#                             request.session['email']=user.email
#                             request.session['fname']=user.fname
#                             return render(request,'seller_index.html')
#             except:
#                 msg="Email Or Password Is Incorrect!"
#                 return render(request,'login.html',{'msg':msg})
#     else:
#         return render(request,'login.html')
    

def login(request):
    if request.method=="POST":
         try:
            user=User.objects.get(
                        email=request.POST['email'],
                        password=request.POST['password']
                    )
            if user.usertype=='user':
                            request.session['email']=user.email
                            request.session['fname']=user.fname
                            request.session['profile_pic']=user.profile_pic.url
                            return render(request,'index.html')
            elif user.usertype=='seller':
                            request.session['email']=user.email
                            request.session['fname']=user.fname
                            return render(request,'seller_index.html')
         except:
                msg="Email Or Password Is Incorrect!"
                return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    
    except:
        return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def services(request):
    return render(request,'services.html')

def shop(request):
    products=Product.objects.all()
    return render(request,'shop.html',{'products':products})

def thankyou(request):
    return render(request,'thankyou.html')

def change_password(request):
    if request.method=="POST":
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        cnewpassword=request.POST['cnewpassword']
        user=User.objects.get(email=request.session['email'])
        if user.password==oldpassword:
            if newpassword==cnewpassword:
                user.password=cnewpassword
                user.save()
                try:
                    del request.session['email']
                    del request.session['fname']
                    msg="Password Changed Successfully.Please Login Again"
                    return render(request,'login.html',{'msg':msg})
                except:
                    return render(request,'login.html')
            else:
                msg="New Password And Confirm New Password Does Not Match!"
                return render(request,'change_password.html',{'msg':msg})
        else:
            msg="Old Password Does Not Match!"
            return render(request,'change_password.html',{'msg':msg})
    else:
        return render(request,'change_password.html')

def seller_index(request):
    return render(request,'seller_index.html')

def seller_change_password(request):
    if request.method=="POST":
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        cnewpassword=request.POST['cnewpassword']
        user=User.objects.get(email=request.session['email'])
        if user.password==oldpassword:
            if newpassword==cnewpassword:
                user.password=cnewpassword
                user.save()
                try:
                    del request.session['email']
                    del request.session['fname']
                    msg="Password Changed Successfully.Please Login Again"
                    return render(request,'login.html',{'msg':msg})
                except:
                    return render(request,'login.html')
            else:
                msg="New Password And Confirm New Password Does Not Match!"
                return render(request,'seller_change_password.html',{'msg':msg})
        else:
            msg="Old Password Does Not Match!"
            return render(request,'seller_change_password.html',{'msg':msg})
    else:
        return render(request,'seller_change_password.html')
    

def seller_add_product(request):
    if request.method=="POST":
        seller=User.objects.get(email=request.session['email'])
        Product.objects.create(
            seller=seller,
            product_name=request.POST['product_name'],
            product_price=request.POST['product_price'],
            product_image=request.POST['product_image'],
            product_description=request.POST['product_description'],
        )
        msg="Product Added Successfully"
        products=Product.objects.filter(seller=seller)
        request.session['product_count']=len(products)
        return render(request,'seller_add_product.html',{'msg':msg})
    else:
        return render(request,'seller_add_product.html')
    
def seller_view_product(request):
    seller=User.objects.get(email=request.session['email'])
    products=Product.objects.filter(seller=seller)
    return render(request,'seller_view_product.html',{'products':products})

def seller_product_details(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'seller_product_details.html',{'product':product})

def seller_edit_product(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method=="POST":
        product.product_name=request.POST['product_name']
        product.product_price=request.POST['product_price']
        product.product_description=request.POST['product_description']

        try:
            product.product_image=request.FILES['product_image']

        except:
            pass

        product.save()
        msg="Product Edited Successfully"
        return render(request,'seller_edit_product.html',{'msg':msg,'product':product})
    else:
        return render(request,'seller_edit_product.html',{'product':product})


def seller_delete_product(request,pk):
    seller=User.objects.get(email=request.session['email'])
    product=Product.objects.get(pk=pk)
    product.delete()
    product=Product.objects.filter(seller=seller)
    return redirect('seller_view_product')

def product_details(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'product_details.html',{'product':product})

def wishlist(request):
    return render(request,'wishlist.html')

def forgot_password(request):
    if request.method=='POST':
        try:
            user=User.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            subject='OTP For Forgot Password'
            message = 'Hello' + user.fname+'OTP For Forgot Password is'+str(otp)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'otp.html',{'email':user.email,'otp':otp})
        except:
            msg="Email not registered"
            return render(request,'forgot_password.html',{'msg':msg})
    else:
        return render(request,'forgot_password.html')

def verify_otp(request):
    email=request.POST['email']
    otp=request.POST['otp']
    uotp=request.POST['uotp']

    if otp==uotp:
        return render(request,'new_password.html',{'email':email})
    
    else:
        msg='incorrect otp'
        return render(request,'otp.html',{'email':email,'otp':otp,'msg':msg})

def new_password(request):
    email=request.POST['email']
    np=request.POST['new_password']
    cnp=request.POST['cnew_password']

    if np==cnp:
        user=User.objects.get(email=email)
        user.password=np
        user.save()
        msg="Password Updated Successfully"
        return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'new_password.html',{'email':email})
    
def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=='POST':
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.email=request.POST['email']
        user.phone=request.POST['phone']
        user.address=request.POST['address']
        try:
            user.profile_pic=request.FILES['profile_pic']

        except:
            pass

        user.save()
        request.session['profile_pic']=user.profile_pic.url
        msg="Profile Updated Successfully"
        return render(request,'profile.html',{'user': user,'msg':msg})
    else:
        return render(request,'profile.html',{'user':user})
    

def wishlist(request):
    user=User.objects.get(email=request.session['email'])
    wishlists=Wishlist.objects.filter(user=user)
    return render(request,'Wishlist.html',{'wishlists':wishlists})

def add_to_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Wishlist.objects.create(
        user=user,
        product=product
    )
    return redirect('wishlist')


def remove_from_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    wishlist=Wishlist.objects.get(user=user,product=product)
    wishlist.delete()
    return redirect('wishlist')

def add_to_cart(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Cart.objects.create(
        user=user,
        product=product,
        product_price=product.product_price,
        total_price=product.product_price,
    )
    return redirect('cart')  

def remove_from_cart(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.get(user=user,product=product)
    cart.delete()
    return redirect('cart')