menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 20

    def get_user_context(self, request,  **kwargs):
        context = kwargs
        user = request.user

        if not user.is_authenticated:

            return context
