from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import vvappForm
from .models import vvapp

# Create your views here.
def index(request):

    item_list = vvapp.objects.order_by("-date")
    if request.method == "POST":
        form = vvappForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vvapp')
    form = vvappForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "vvapp LIST",
    }
    return render(request, 'vvapp/index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = vvapp.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('vvapp')