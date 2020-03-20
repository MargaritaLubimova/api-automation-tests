import requests


class JsonPlaceholderAPI:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'

    def get_posts(self):
        url = self.base_url + '/posts'
        response = requests.get(url)

        return response

    def get_post_with_post_id(self, post_id):
        url = self.base_url + '/posts/{}'.format(post_id)
        response = requests.get(url)
        return response

    def get_comments_with_post_id(self, post_id):
        url = self.base_url + '/comments?postId={}'.format(post_id)
        response = requests.get(url)
        return response

    def get_post_with_user_id(self, user_id):
        url = self.base_url + '/posts?userId={}'.format(user_id)
        response = requests.get(url)
        return response

    def create_post(self, param):
        url = self.base_url + '/posts'
        response = requests.post(url, data=param)
        return response

    def delete_post(self, post_id, user_id):
        url = self.base_url + '/posts/{}?userId={}'.format(post_id, user_id)
        response = requests.delete(url)
        return response



