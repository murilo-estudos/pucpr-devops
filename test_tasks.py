"""Unit tests for tasks.py using pytest."""
import os
import pytest
from tasks import add_task, list_tasks, complete_task, remove_task

TEST_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_tasks.json")


@pytest.fixture(autouse=True)
def cleanup():
    """Ensure a clean test file before and after each test."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_add_task():
    tasks = add_task("Estudar CI/CD", tasks=[], path=TEST_FILE)
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Estudar CI/CD"
    assert tasks[0]["done"] is False


def test_list_tasks_empty():
    tasks = list_tasks(tasks=[], path=TEST_FILE)
    assert tasks == []


def test_complete_task():
    tasks = add_task("Fazer commits", tasks=[], path=TEST_FILE)
    task_id = tasks[0]["id"]
    result = complete_task(task_id, tasks=tasks, path=TEST_FILE)
    assert result is True
    assert tasks[0]["done"] is True


def test_complete_task_not_found():
    tasks = add_task("Fazer commits", tasks=[], path=TEST_FILE)
    result = complete_task(999, tasks=tasks, path=TEST_FILE)
    assert result is False


def test_remove_task():
    tasks = add_task("Abrir PR", tasks=[], path=TEST_FILE)
    task_id = tasks[0]["id"]
    result = remove_task(task_id, tasks=tasks, path=TEST_FILE)
    assert result is True
    assert len(tasks) == 0


def test_add_multiple_tasks_increments_id():
    tasks = add_task("Tarefa 1", tasks=[], path=TEST_FILE)
    tasks = add_task("Tarefa 2", tasks=tasks, path=TEST_FILE)
    assert tasks[0]["id"] == 1
    assert tasks[1]["id"] == 2