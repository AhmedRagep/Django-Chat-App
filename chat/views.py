from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room, Message
# Create your views here.
def home(request):
    return render(request, 'home.html')


def room(request, room):
    # جلب الاسم من المستخدم
    username = request.GET.get('username')
    # جلب الروم من المودل
    # الcheck والروم هو متغير ياتي من 
    detail = Room.objects.get(name=room)
    return render(request, 'room.html', {
        "detail": detail,
        "username" : username,
        "room" : room,
    })


# هو اكشن في فورم الهوم
def check(request):
    # جلب اسم الروم
    room = request.POST['room_name']
    #  جلب الاسم
    username = request.POST['username']

    # لو الغرفة موجوده روحلها
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    # لو مش موجوده
    else:
        # انشئ روم بالمعلومات اللي جت واحفظها وروحلها
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
# موجود في الاجكس
def send(request):
    # جلب الرسالة اللي اتكتبت
    message = request.POST["message"]
    # جلب الاسم
    username = request.POST["username"]
    # جلب رقم الغرفة
    room_id = request.POST["room_id"]

    # انشاء رسالة جديدة قيمتها الرسالة واليوزر هو الاسم والغرفة هيا رقم الغرفة
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    # اظهار هذه الرسالة بعد الاتمام
    return HttpResponse('Messge Sent Saccessfully')