import uuid

import pytest
import jwt

import boto3
from fastapi import status
from starlette.testclient import TestClient

from main import app, get_task_store
from models import Task
from store import TaskStore, TaskStatus


@pytest.fixture
def task_store(dynamodb_table):
    return TaskStore(dynamodb_table)


@pytest.fixture
def client(task_store):
    app.dependency_overrides[get_task_store] = lambda: task_store
    return TestClient(app)


def test_health_check(client):
    """
    GIVEN
    WHEN health check endpoint is called with GET method
    THEN response with status 200 and body OK is returned
    """
    response = client.get("/api/health-check/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "OK"}


@pytest.fixture
def dynamodb_table():
    dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:4566")
    # print("*" * 80)
    # print(dynamodb.tables.all())
    # print("*" * 80)
    table_name = "test-table"
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
    )
    # print("*" * 80)
    # print(table.table_name)
    # print("*" * 80)

    # Wait until the table exists.
    table.meta.client.get_waiter("table_exists").wait(TableName=table_name)

    yield table_name

    # Clean up: delete the table
    table.delete()


def test_added_task_retrieved_by_id(dynamodb_table):
    print("*" * 80)
    print(dynamodb_table)
    print("*" * 80)
    repository = TaskStore(table_name=dynamodb_table)  # Use the table name here
    task = Task.create(uuid.uuid4(), "Clean your office", "john@doe.com")

    repository.add(task)

    assert repository.get_by_id(task_id=task.id, owner=task.owner) == task


@pytest.fixture
def user_email():
    return "bob@builder.com"


@pytest.fixture
def id_token(user_email):
    return jwt.encode({"cognito:username": user_email}, "secret")


def test_create_task(client, user_email, id_token):
    title = "Clean your desk"
    response = client.post(
        "/api/create-task",
        json={"title": title},
        headers={"Authorization": id_token},
    )
    body = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert body["id"]
    assert body["title"] == title
    assert body["status"] == "OPEN"
    assert body["owner"] == user_email


def test_list_open_tasks(client, user_email, id_token):
    title = "Kiss your wife"
    client.post(
        "/api/create-task",
        json={"title": title},
        headers={"Authorization": id_token},
    )

    response = client.get("/api/open-tasks", headers={"Authorization": id_token})
    body = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert body["results"][0]["id"]
    assert body["results"][0]["title"] == title
    assert body["results"][0]["owner"] == user_email
    assert body["results"][0]["status"] == TaskStatus.OPEN
