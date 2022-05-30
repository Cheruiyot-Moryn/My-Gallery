from django.shortcuts import render

# Create your views here.
def album(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'album.html', {'images': images[::-1], 'locations': locations})
