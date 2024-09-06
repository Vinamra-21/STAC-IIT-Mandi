from django.shortcuts import render

# Event-specific gallery
def Gallery(request):
    images = [
        {'url': 'https://picsum.photos/id/1/600/400', 'title': 'Space Event 1', 'description': 'Explore the stars!', 'event_id': 1},
        {'url': 'https://picsum.photos/id/2/600/400', 'title': 'Space Event 2', 'description': 'A journey to Mars.', 'event_id': 2},
        {'url': 'https://picsum.photos/id/3/600/400', 'title': 'Space Event 3', 'description': 'Lunar exploration.', 'event_id': 3}
    ]
    
    return render(request, 'gallery.html', {'images': images})

def GalleryEvent(request, event_id):
    # Event-specific images
    event_images = {
        1: [
            {'url': 'https://picsum.photos/id/10/600/400'},
            {'url': 'https://picsum.photos/id/11/600/400'}
        ],
        2: [
            {'url': 'https://picsum.photos/id/20/600/400'},
            {'url': 'https://picsum.photos/id/21/600/400'}
        ],
        3: [
            {'url': 'https://picsum.photos/id/30/600/400'},
            {'url': 'https://picsum.photos/id/31/600/400'}
        ]
    }
    images = event_images.get(event_id, [])
    
    return render(request, 'galleryEvent.html', {'images': images})
