def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description="Simple greeting CLI")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args(argv)
    print(greet(args.name))


if __name__ == "__main__":
    main()
