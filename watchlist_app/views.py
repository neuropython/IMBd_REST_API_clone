from django.shortcuts import render
from watchlist_app.models import Movies
from django.http import JsonResponse

# Create your views here.
def movie_list(request):
    """
    View all movies in the database
    
    Args:
        request (HttpRequest): The Django request object.
    
    Returns:
        HttpResponse: A HTTP response object containing a list of movies in JSON format.
    """
    movies = Movies.objects.all()
    data = {'movies': list(movies.values())}
    return JsonResponse(data)

def movie_details(request, pk):
    """
    Handle a request for a specific movie.
    
    Args:
        request (HttpRequest): The Django request object.
        pk (int): The primary key of the movie.
    
    Returns:
        HttpResponse: A HTTP response object containing the requested movie in JSON format.
    """
    movie = Movies.objects.get(pk = pk)
    data = {
        'name': movie.name,
        'desc': movie.description,
        'is active': movie.active
    }
    return JsonResponse(data)
    