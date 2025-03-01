import regex_maturin


def main():

    contents = "HELLO MYNAME IS ACKY, ACKY"
    regex_pattern = r"ACK"

    res = regex_maturin.regex_match(
        contents,
        regex_pattern,
    )

    print(type(res))


if __name__ == "__main__":
    main()
