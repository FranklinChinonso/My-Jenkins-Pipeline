def reverse_and_upper(s: str) -> str:
    """
    Reverse the input string and convert to uppercase.
    Example: "hello" -> "OLLEH"
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1].upper()


def main():
    example = "Hello, Jenkins!"
    result = reverse_and_upper(example)
    print(f"Input : {example}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()
