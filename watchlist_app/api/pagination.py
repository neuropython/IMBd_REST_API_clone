from rest_framework.pagination import (PageNumberPagination, 
                                       LimitOffsetPagination, 
                                       CursorPagination) 

# class WatchListPagination(PageNumberPagination):
#     page_size = 2 # default page size
#     page_query_param = 'p' #use p instead of 'page'
#     page_size_query_param = 'size' # size might be overriden by the user
#     max_page_size = 10 # even if the user sets the size to 100, it will be 
#                        #overriden to 10
    
# class StreamLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 2
#     max_limit = 10
#     limit_query_param = 'start'
    
class WatchListPagination(CursorPagination):
    page_size = 2
    ordering = '-created'