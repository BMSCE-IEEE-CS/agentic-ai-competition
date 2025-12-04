from simple_project.cli import greet


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
