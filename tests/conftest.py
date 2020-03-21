import pytest


@pytest.fixture
def data_for_test_01_get_posts():
    expected_entries = ["userId", "id", "title", "body"]
    return expected_entries


@pytest.fixture
def data_for_test_02_get_post_with_post_id():
    expected_data = {
       'post_id': 40,
       'expected_user_id': 4,
       'expected_title': 'enim quo cumque',
       'expected_body': 'ut voluptatum aliquid illo tenetur nemo sequi quo facilis\nipsum rem optio mollitia ' \
                        'quas\nvoluptatem eum voluptas qui\nunde omnis voluptatem iure quasi maxime voluptas nam'
    }
    return expected_data


@pytest.fixture
def data_for_test_03_get_comments_with_post_id():
    expected_data = {
        'postId': 4,
        'id': 17,
        'name': 'eos est animi quis',
        'email': 'Preston_Hudson@blaise.tv',
        'body': 'consequatur necessitatibus totam sed sit dolorum\nrecusandae quae odio excepturi voluptatum harum '
                'voluptas\nquisquam sit ad eveniet delectus\ndoloribus odio qui non labore'
    }
    return expected_data


@pytest.fixture
def data_for_test_04_get_post_with_user_id():
    expected_data = {
        'userId': 5,
        'id': 42,
        'title': 'commodi ullam sint et excepturi error explicabo praesentium voluptas',
        'body': 'odio fugit voluptatum ducimus earum autem est incidunt voluptatem\nodit reiciendis aliquam sunt sequi '
                'nulla dolorem\nnon facere repellendus voluptates quia\nratione harum vitae ut'
    }
    return expected_data


@pytest.fixture
def body_for_new_post():
    body = {
        'title': 'foo',
        'body': 'bar',
        'userId': '938'
    }
    return body
