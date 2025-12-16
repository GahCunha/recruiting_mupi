from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render

def landpage(request):
    return render(request, "landpage.html")

def logout_confirm(request):
    if request.method == "POST":
        logout(request)
        return redirect("landpage")
    return render(request, "logout_confirm.html")

@login_required
def messages_list(request):
    return render(request, "messages_list.html")

@login_required
def message_detail(request, pk):
    return render(request, "message_detail.html", {"pk": pk})

@login_required
def message_edit(request, pk):
    return render(request, "message_edit.html", {"pk": pk})

@login_required
def message_delete_confirm(request, pk):
    return render(request, "message_delete_confirm.html", {"pk": pk})
