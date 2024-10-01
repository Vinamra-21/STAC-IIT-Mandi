from django.shortcuts import render

#rendering Photogallery page
def photogallery(request):
    # context_ = {
    #     "photogallery": photogallery.objects.all().order_by("-id"),
    #     "title": "Photos",
    #     "photos": "active",
    #     "gallery_": "active",
    # }
    return render(request, "photogallery.html", )

# context_

# rendering videogallery page
def videogallery(request):
    # context_ = {
    #     "videogallery": videogallery.objects.all().order_by("-id"),
    #     "title": "Videos",
    #     "videos": "active",
    #     "gallery_": "active",
    # }
    return render(request, "videogallery.html", )

# context_