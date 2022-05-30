from django.http.response import Http404
from album.models import Image, Location
from django.shortcuts import render

# Create your views here.
def album(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'album.html', {'images': images[::-1], 'locations': locations})

def search(request):

    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any images in that category"
        return render(request, 'search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except Exception:
        raise Http404()
    return render(request,"images.html", {"image":image})

def location_image(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'location_image': images})        