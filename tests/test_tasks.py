import pytest

from src.tasks import add_task, complete_task, get_tasks


def test_add_task():
    task = add_task("Learn Advanced Git")

    assert task["title"] == "Learn Advanced Git"
    assert task["completed"] is False


def test_get_tasks():
    assert len(get_tasks()) >= 0


def test_complete_task():
    task = add_task("Practice GitHub")

    completed = complete_task(task["id"])

    assert completed["completed"] is True


def test_empty_task():
    with pytest.raises(ValueError):
        add_task("")