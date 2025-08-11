from django.shortcuts import render, redirect
from django.urls import *
from . models import *
from django.core.mail import send_mail
from django.conf import settings
import random
import razorpay
from django.conf import settings
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.cache import never_cache
from django.http import HttpResponseBadRequest
# Create your views here.

@never_cache
def index(request):
    try:
        user = User.objects.get(email=request.session['email'])
        product = Product.objects.all()
        return render(request, "index.html",{'product': product})
    except:
        return render(request, "index.html")


def sindex(request):
    return render(request, "sindex.html")

def about(request):
    return render(request, "about.html")


def addToWishlist(request):
    return render(request, "addToWishlist.html")


def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")


def men(request):
    return render(request, "men.html")


def women(request):
    return render(request, "women.html")


def orderComplete(request):
    return render(request, "orderComplete.html")

@never_cache
def signup(request):
    if request.session.get('email'):
        # Redirect based on usertype
        if request.session.get('usertype') == "buyer":
            return redirect('index')  # Replace 'index' with your buyer's dashboard URL
        else:
            return redirect('sindex')  # Replace 'sindex' with your seller's dashboard URL
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            msg = "Account already exist!"
            return render(request,'signup.html',{'msg':msg})

        except:
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password'],
                    profile = request.FILES['profile'],
                    usertype = request.POST['usertype']
                )
                msg = "Sign-up Successfull"

                return render(request, 'login.html',{'msg':msg})
            else:
                msg = "Password and Confirm Password doesn't match!"
                return render(request, 'signup.html',{'msg':msg})


    else:
        return render(request, "signup.html")
    
@never_cache
def login(request):
    if request.session.get('email'):
        # Redirect based on usertype
        if request.session.get('usertype') == "buyer":
            return redirect('index')  # Replace 'index' with your buyer's dashboard URL
        else:
            return redirect('sindex')  # Replace 'sindex' with your seller's dashboard URL

    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])

            if user.password == request.POST['password']:
                request.session['email']=user.email
                request.session['profile']=user.profile.url
                request.session['usertype'] = user.usertype
                if user.usertype=="buyer":
                    return redirect('index')
                else:
                    return redirect('sindex')
            else:
                msg = 'Invalid Credentials'
                return render(request, 'login.html',{'msg':msg})

        except:
            msg = 'Invalid Credentials'
            return render(request, 'login.html',{'msg':msg})

    else:
        return render(request, "login.html")
    
def  logout(request):
    del request.session['email']
    del request.session['profile']

    return redirect('login')

def cpass(request):
    user=User.objects.get(email=request.session['email'])
    if request.method == "POST":
        try:  
            if user.password == request.POST['opassword']:
                if request.POST['npassword'] == request.POST['cnpassword']:
                    user.password = request.POST['npassword'] 
                    user.save()
                    msg = "Password Updated Successfully"
                    return redirect('logout')
                else:
                    msg = "Confirm New Password doesn't match"
                    if user.usertype == "buyer":
                        return render(request,'cpass.html',{'msg':msg})
                    else:
                        return render(request,'scpass.html',{'msg':msg})
            else:
                msg = "Old Password doesnot match"
                if user.usertype == "buyer":
                    return render(request,'cpass.html',{'msg':msg})
                else:
                    return render(request,'scpass.html',{'msg':msg})
        except:
            if user.usertype == "buyer":
                return render(request,'cpass.html')
            else:
                return render(request,'scpass.html')
    
    else:
        if user.usertype == "buyer":
            return render(request,'cpass.html')
        else:
            return render(request,'scpass.html')
    
def fpass(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            email = request.POST['email']
            otp = random.randint(1001,9999)
            request.session['mobile']=user.mobile
            request.session['otp']=otp
            # Sending OTP through mail
            subject="OTP verifivation for changing password"
            message=f"Your OTP is {otp}"
            from_email=settings.EMAIL_HOST_USER
            recipient_list= [email]
            send_mail(
                subject,
                message,
                from_email,
                recipient_list
            )
            return render(request,'otp.html')
            

            
        except:
            msg = "Invalid Email Address"
            return render(request,'fpass.html',{'msg':msg})
            
            
    else:
        return render(request,'fpass.html')
    
def otp(request):
    otp = int(request.session['otp'])
    uotp = int(request.POST['uotp'])
    try:
        if otp == uotp:
            del request.session['otp']
            return render(request,'newpass.html')
        
        else:
            msg = "Invalid OTP"
            return render(request,'otp.html',{'msg':msg})
    except:
        return render(request,'otp.html')
    
def newpass(request):
    if request.method == "POST":
        user = User.objects.get(mobile=request.session['mobile'])
        try:
            if request.POST['npassword']==request.POST['cnpassword']:
                user.password = request.POST['npassword']
                user.save()
                del request.session['mobile']
                return redirect('login')
            
            else:
                msg = "Password and Confirm Password doesn't match!! "
                return render(request,'newpass.html',{'msg':msg})
        except:
            return render(request,'newpass.html')
    else:
        return render(request,'newpass.html')
    
def profile(request):
    user = User.objects.get(email=request.session['email'])
    if request.method == "POST":
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.mobile=request.POST['mobile']
        try:
            user.profile=request.FILES['profile']
            user.save()
        except:
            pass
        
        request.session['profile']=user.profile.url
        user.save()
        if user.usertype == "buyer":
            return redirect('index')
        else:
            return redirect('sindex')
    else:
        if user.usertype == "buyer":
            return render(request,'profile.html',{'user':user})
        else:
            return render(request,'sprofile.html',{'user':user})

def sadd_details(request):
    seller = User.objects.get(email=request.session['email'])
    if request.method == "POST":
        try:
            Product.objects.create(
                seller = seller,
                gen = request.POST['gen'],
                cat = request.POST['cat'],
                sz = request.POST['sz'],
                bname = request.POST['bname'],
                pname = request.POST['pname'],
                price = request.POST['price'],
                desc = request.POST['desc'],
                pimage = request.FILES['pimage'],
            )
            msg = "Product Added Successfully!"
            return render(request,'sindex.html',{'msg':msg})
        except:
            return render(request,'sadd_details.html')
    
    else:
       return render(request,'sadd_details.html')

def viewprod(request):
    seller = User.objects.get(email=request.session['email'])
    product = Product.objects.filter(seller=seller)
    return render(request,'viewprod.html',{'product':product})


def spdetails(request,pk):
    seller = User.objects.get(email=request.session['email'])
    product = Product.objects.filter(pk=pk)
    return render(request,'spdetails.html',{'product':product})

def spupdate(request,pk):
    seller = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        product.gen = request.POST['gen']
        product.cat = request.POST['cat']
        product.sz = request.POST['sz']
        product.pname = request.POST['pname']
        product.bname = request.POST['bname']
        product.price = request.POST['price']
        product.desc = request.POST['desc']

        try:
            product.pimage = request.FILES['pimage']
            product.save()
        
        except:
            pass

        product.save()
        return redirect('sindex')
    else:
        return render(request,'spupdate.html',{'product':product})

def spdelete(request,pk):
    product = Product.objects.filter(pk=pk)
    product.delete()
    
    return redirect('sindex')

def pdetails(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.filter(pk=pk)
    wish = Wishlist.objects.filter(user=user).values_list('product_id', flat=True)
    
    return render(request,'pdetails.html',{'product':product,'wish':list(wish)})

def wishlist(request):
    user = User.objects.get(email=request.session['email'])
    try:
        wish = Wishlist.objects.filter(user=user)       
    except:
        pass
    return render(request,'wishlist.html',{'wish':wish})

def addwish(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)

    Wishlist.objects.create(
        user = user,
        product = product
    )
    return redirect('wishlist')

def delwish(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)
    wish = Wishlist.objects.filter(user=user,product=product)
    wish.delete()       
    return redirect('wishlist') 

def addcart(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)
    Cart.objects.create(

        user = user,
        product = product,
        payment = False,
        qty = 1,
        total = product.price,
        roundtotal = product.price
    )
    return redirect("cart")


def cart(request):
    user = User.objects.get(email=request.session['email'])
    cart_items = Cart.objects.filter(user=user, payment=False)
    net = sum(item.roundtotal for item in cart_items)  # total amount

    if net <= 0:
        # Cart empty or zero amount, no Razorpay order created
        context = {
            'cart': cart_items,
            'net': net,
            'razorpay_key': settings.RAZORPAY_KEY_ID,
            'order_id': None,
            'amount': None,
        }
        return render(request, 'cart.html', context)

    amount_paise = int(net * 100)  # convert to paise (int)

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    payment_order = client.order.create({
        "amount": amount_paise,
        "currency": "INR",
        "payment_capture": "1"
    })

    context = {
        'cart': cart_items,
        'net': net,
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'order_id': payment_order['id'],
        'amount': payment_order['amount'],
        'error': None
    }
    return render(request, 'cart.html', context)


def dcart(request,pk):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.get(pk=pk)
    cart = Cart.objects.filter(user=user,product=product)
    cart.delete()
    return redirect('cart')
    

def changeqty(request,pk):
    try:
        cart = Cart.objects.get(pk=pk)

        cart.qty = int(request.POST['qty'])
        cart.roundtotal = cart.total * cart.qty
        cart.save()
        

        return redirect('cart')
     
    except:
        return redirect('cart')
    
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        payment_id = data.get('payment_id')
        order_id = data.get('order_id')
        signature = data.get('signature')

        # Verify payment signature to ensure payment is legit
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)
        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({'status': 'fail'})

        # If signature is valid, mark cart items as paid or clear them
        user = User.objects.get(email=request.session['email'])
        Cart.objects.filter(user=user, payment=False).update(payment=True)

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})