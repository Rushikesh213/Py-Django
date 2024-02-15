from django.shortcuts import render,redirect
from testapp.models import Recipe


def saverecipe(request):
    if request.method=='POST':
        title=request.POST.get('recipe')
        desc=request.POST.get('desc')
        image=request.FILES.get('image')
        
        print(title)
        print(desc)
        print(image)
        
        rc=Recipe.objects.create(recipe_title=title,
                    recipe_desc=desc,
                    recipe_image=image
                    )
        return redirect('/recipe')
    data=Recipe.objects.all()
    return render(request,'index.html',{'data':data})   

def delete_view(request,id):
    Recipe.objects.get(id=id).delete()
    return redirect('/recipe')


def update_view(request,id):
    data=Recipe.objects.get(id=id)
    if request.method=='POST':
        title=request.POST.get('title')
        descr=request.POST.get('descr')
        image=request.FILES.get('image_new')
     
        data.recipe_title=title
        data.recipe_desc=descr
        data.recipe_image=image
        data.save()
        return redirect("/recipe")
    return render(request,'update.html',{'data':data})
        
        
    
    



