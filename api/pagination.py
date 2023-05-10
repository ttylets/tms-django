from rest_framework import viewsets, filters, pagination


class DefaultPagination(pagination.PageNumberPAgination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


