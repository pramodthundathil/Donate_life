from django.shortcuts import redirect

def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.all().exists():
            group = request.user.groups.all()[0].name
        if group == None:
            return redirect("UserConfirm")
        if group == "donners":
            return view_func(request,*args,**kwargs)
        if group == "organisation":
            return redirect('OrganasationHome')
        if group == "admin":
            return redirect('AdminHome')
    return wrapper_func