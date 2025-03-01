import regex_maturin


def main():

    contents = "HELLO MYNAME IS JACKY, JACKY"
    regex_pattern = r"JACK"

    res = regex_maturin.regex_match(
        contents,
        regex_pattern,
    )

    print(res)


if __name__ == "__main__":
    main()
