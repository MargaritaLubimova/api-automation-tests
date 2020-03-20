import os
import sys

import allure
import pytest
import random
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from helper.api import JsonPlaceholderAPI

json_placeholder_API = JsonPlaceholderAPI()


@allure.feature('Tests JSONPlaceholder')
@allure.story('Check entries in response for get posts')
def test_01_get_posts():
    response = json_placeholder_API.get_posts()

    assert response.status_code == 200, "Status code for response not equal 200"

    post = random.choice(response.json())
    expected_entries = ["userId", "id", "title", "body"]
    all_entries_exist = set(post.keys()) == set(expected_entries)

    assert len(post) == 4,     "Not all entries exist in the post"
    assert all_entries_exist,  "Not all name entries in the post is right"


@allure.feature('Tests JSONPlaceholder')
@allure.story('Check response for get post with post id')
def test_02_get_post_with_post_id():
    post_id = 40
    expected_user_id = 4
    expected_title = 'enim quo cumque'
    expected_body = 'ut voluptatum aliquid illo tenetur nemo sequi quo facilis\nipsum rem optio mollitia ' \
                    'quas\nvoluptatem eum voluptas qui\nunde omnis voluptatem iure quasi maxime voluptas nam'

    response = json_placeholder_API.get_post_with_post_id(post_id=post_id)
    assert response.status_code == 200, "Status code for response not equal 200"

    post = response.json()
    assert post['userId'] == expected_user_id, "Post was gotten has wrong user id"
    assert post['id'] == post_id,              "Post was gotten has wrong id"
    assert post['title'] == expected_title,    "Post was gotten has wrong title"
    assert post['body'] == expected_body,      "Post was gotten has wrong body"


@allure.feature('Tests JSONPlaceholder')
@allure.story('Check response for get comment with post id and id')
def test_03_get_comments_with_post_id():
    expected_result = {
        'postId': 4,
        'id': 17,
        'name': 'eos est animi quis',
        'email': 'Preston_Hudson@blaise.tv',
        'body': 'consequatur necessitatibus totam sed sit dolorum\nrecusandae quae odio excepturi voluptatum harum '
                'voluptas\nquisquam sit ad eveniet delectus\ndoloribus odio qui non labore'
    }

    response = json_placeholder_API.get_comments_with_post_id(post_id=expected_result['postId'])
    assert response.status_code == 200, "Status code for response not equal 200"
    if expected_result in response.json():
        assert True
    else:
        val = next(iter(filter(lambda x: x['id'] == expected_result['id'], response.json())), None)

        if val is None:
            assert False, "Does not exist comment for id: {}".format(expected_result['id'])
        else:
            def get_incorrect_values(key, expected, actual):
                if expected != actual:
                    return "Value for key: {} is incorrect".format(key)

            res = "\n".join(filter(lambda x: x is not None, map(lambda x: get_incorrect_values(x, expected_result[x], val[x]),
                                                                expected_result.keys())))

            assert len(res) == 0, "{}".format(res)


@allure.feature('Tests JSONPlaceholder')
@allure.story('Check response for get post with user id')
def test_04_get_post_with_user_id():
    expected_result = {
        'userId': 5,
        'id': 42,
        'title': 'commodi ullam sint et excepturi error explicabo praesentium voluptas',
        'body': 'odio fugit voluptatum ducimus earum autem est incidunt voluptatem\nodit reiciendis aliquam sunt sequi '
                'nulla dolorem\nnon facere repellendus voluptates quia\nratione harum vitae ut'
    }

    response = json_placeholder_API.get_post_with_user_id(user_id=expected_result['userId'])
    assert response.status_code == 200, "Status code for response not equal 200"
    if expected_result in response.json():
        assert True
    else:
        val = next(iter(filter(lambda x: x['id'] == expected_result['id'], response.json())), None)

        if val is None:
            assert False, "Does not exist post for user id: {} and id: {}".format(expected_result['userId'],
                                                                                  expected_result['id'])
        else:
            def get_incorrect_values(key, expected, actual):
                if expected != actual:
                    return "Value for key: {} is incorrect".format(key)

            res = "\n".join(
                filter(lambda x: x is not None, map(lambda x: get_incorrect_values(x, expected_result[x], val[x]),
                                                    expected_result.keys())))

            assert len(res) == 0, "{}".format(res)


@allure.feature('Tests JSONPlaceholder')
@allure.story('Check create new post')
@pytest.mark.dependency()
def test_05_create_new_post():
    body = {
        'title': 'foo',
        'body': 'bar',
        'userId': '999'
    }
    response = json_placeholder_API.create_post(body)

    assert response.status_code == 201, "Status code for response not equal 201"

    post = response.json()
    assert post['userId'] == body['userId'], "Post was created has wrong user id"
    assert post['title'] == body['title'], "Post was created has wrong title"
    assert post['body'] == body['body'], "Post was created has wrong body"


@allure.feature('Tests JSONPlaceholder')
@allure.story('Check create new post')
@pytest.mark.dependency(depends=['test_05_create_new_post'])
def test_06_deleted_created_post():
    body = {
        'title': 'foo',
        'body': 'bar',
        'userId': '938'
    }
    response = json_placeholder_API.create_post(body)
    post_id = response.json()['id']

    response = json_placeholder_API.delete_post(post_id, body['userId'])

    assert response.status_code == 200, "Status code for response not equal 200"


