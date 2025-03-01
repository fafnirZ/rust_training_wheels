import re
import time
import regex_maturin


data = [
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", r"(a+)+$"),  # Very slow on long strings
    ("1234567890123456789012345678901234567890", r"^(1?){30}1?$"), # Very slow on long strings
    ("The quick brown fox jumps over the lazy dog.", r"unicorn"),
    ("123-456-7890", r"abc"),
    ("example@email.com", r"invalid_pattern"),
    ("Hello, World!", r"Goodbye"),
    ("This is a test string.", r"\d+"),
    ("Python is a powerful language.", r"Java"),
    ("12345", r"[a-z]+"),
    ("apple banana cherry", r"\d+"),
    ("http://www.example.com", r"ftp://"),
    ("A1B2C3D4", r"[a-z]\d"),
    ("My name is John.", r"Jane"),
    ("The cat sat on the mat.", r"dog"),
    ("1.23 4.56 7.89", r"[A-Z]+"),
    ("This is a sentence with some words.", r"\d+"),
    ("Date: 2023-10-27", r"Monday"),
    ("Price: $99.99", r"free"),
    ("User ID: 123456", r"[a-z]+"),
    ("File name: document.txt", r"\d+"),
    ("IP address: 192.168.1.1", r"[A-Z]+"),
    ("Status: OK", r"Error"),
    ("Error code: 404", r"[a-z]+"),
    ("Version: 1.2.3", r"[A-Z]+"),
    ("Color: red", r"blue"),
    ("Size: large", r"small"),
    ("Product: Widget", r"Gadget"),
    ("Location: New York", r"London"),
    ("Time: 12:30", r"morning"),
    ("Message: Hello there!", r"Goodbye there!"),
    ("Count: 10", r"[a-z]+"),
    ("Value: 3.14", r"[A-Z]+"),
    ("Key: abc", r"\d+"),
    ("Code: XYZ123", r"[a-z]+"),
    ("ID: 56789", r"[A-Z]+"),
    ("Token: aBcDeFg", r"\d+"),
    ("Path: /home/user", r"[A-Z]+"),
    ("URL: https://example.org", r"ftp://"),
    ("Word: example", r"sample"),
    ("Number: 987", r"[a-z]+"),
    ("Text: some text", r"other text"),
    ("Data: 1,2,3", r"[A-Z]+"),
    ("Info: details", r"summary"),
    ("Name: Alice", r"Bob"),
    ("City: London", r"Paris"),
    ("Country: France", r"Germany"),
    ("Job: Developer", r"Designer"),
    ("Animal: Dog", r"Cat"),
    ("Fruit: Orange", r"Apple"),
    ("Vegetable: Carrot", r"Broccoli"),
    ("Month: December", r"January"),
    ("Day: Monday", r"Sunday")
]


def test_threaded_python():
    from concurrent.futures import ThreadPoolExecutor

    def worker_fn(content, regex, results):
        results.append(
            re.findall(regex, content)
        )

    results = []

    t_0 = time.time()

    with ThreadPoolExecutor(max_workers=8) as tp:
        
        futures = []
        for content, regex_pattern in data:
            futures.append(
                tp.submit(
                    worker_fn,
                    content,
                    regex_pattern,
                    results,
                )
            )

        for future in futures:
            future.result()
    
    t_1 = time.time()
    print(f"Python took: {t_1 - t_0}s")

def test_threaded_rust():
    
    from concurrent.futures import ThreadPoolExecutor

    def worker_fn(content, regex, results):
        results.append(
            regex_maturin.regex_match(regex, content)
        )

    results = []

    t_0 = time.time()

    with ThreadPoolExecutor(max_workers=8) as tp:
        
        futures = []
        for content, regex_pattern in data:
            futures.append(
                tp.submit(
                    worker_fn,
                    content,
                    regex_pattern,
                    results,
                )
            )

        for future in futures:
            future.result()
    
    t_1 = time.time()
    print(f"Rust took: {t_1 - t_0}s")

if __name__ == "__main__":
    test_threaded_python()
    test_threaded_rust()
