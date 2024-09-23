import os
import requests

class IMDbAPIHandler:
    def __init__(self, content_type):
        """
        Инициализирует обработчик API для заданного типа контента (фильмы или сериалы).
        :param content_type: Тип контента, который нужно запросить ('movies' или 'series').
        """
        self.content_type = content_type
        self.api_url = "https://imdb-top-100-movies.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com",
            "X-RapidAPI-Key": os.getenv("RapidAPI_Key")
        }

    def get_top_10(self):
        """
        Запрашивает данные у API и возвращает 10 лучших элементов (фильмов или сериалов) в обратном порядке.
        :return: Список из 10 лучших элементов, либо пустой список в случае ошибки.
        """
        # Определяем URL на основе типа контента
        if self.content_type == 'series':
            url = self.api_url + 'series'
        else:
            url = self.api_url

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            content = response.json()
            # Сортируем элементы по рейтингу от лучшего к худшему
            sorted_content = sorted(content, key=lambda x: x['rating'], reverse=True)
            # Получаем лучшие 10 элементов и переворачиваем их, чтобы они выводились от худшего к лучшему
            top_10_content = sorted_content[:10][::-1]

            # Формируем список сообщений для отправки в Telegram
            content_info = []
            for item in top_10_content:
                title = item['title']
                rating = item['rating']
                description = item.get('description', "Описание недоступно.")
                image_url = item.get('image', None)

                content_message = {
                    'title': title,
                    'rating': rating,
                    'description': description,
                    'image_url': image_url
                }

                content_info.append(content_message)

            return content_info
        else:
            return []
