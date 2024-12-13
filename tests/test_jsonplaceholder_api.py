def test_get_users(api_client):
    """
    Test fetching the list of users.
    """
    response = api_client.get("users")
    assert isinstance(response, list)
    assert len(response) > 0
    assert "id" in response[0]


def test_get_single_post(api_client):
    """
    Test fetching a single post by ID.
    """
    response = api_client.get("posts/1")
    assert response["id"] == 1
    assert "title" in response


def test_create_post(api_client):
    """
    Test creating a new post.
    """
    new_post = {"title": "foo", "body": "bar", "userId": 1}
    response = api_client.post("posts", data=new_post)
    assert response["title"] == new_post["title"]
    assert response["body"] == new_post["body"]
    assert response["userId"] == new_post["userId"]


def test_delete_post(api_client):
    """
    Test deleting a post by ID.
    """
    status_code = api_client.delete("posts/1")
    assert status_code == 200


def test_response_matches_schema(api_client, schema_validator):
    """
    Test that the API response matches a schema.
    """
    response = api_client.get("users")
    schema_validator.validate_schema(response, "schemas/user_schema.json")
