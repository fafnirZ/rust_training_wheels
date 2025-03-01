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
    ("Day: Monday", r"Sunday"),
    ("The quick brown fox jumps over the lazy dog.", r"fox"),
    ("123-456-7890", r"\d{3}-\d{3}-\d{4}"),
    ("example@email.com", r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"),
    ("Hello, World!", r"Hello"),
    ("This is a test string.", r"test"),
    ("Python is a powerful language.", r"Python"),
    ("12345", r"\d+"),
    ("apple banana cherry", r"\b\w+\b"),
    ("http://www.example.com", r"https?://[\w.-]+.\w+"),
    ("A1B2C3D4", r"[A-Z]\d"),
    ("My name is John.", r"John"),
    ("The cat sat on the mat.", r"cat"),
    ("1.23 4.56 7.89", r"\d\.\d{2}"),
    ("This is a sentence with some words.", r"\w+"),
    ("Date: 2023-10-27", r"\d{4}-\d{2}-\d{2}"),
    ("Price: $99.99", r"\$\d+\.\d{2}"),
    ("User ID: 123456", r"\d{6}"),
    ("File name: document.txt", r"\w+\.\w+"),
    ("IP address: 192.168.1.1", r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"),
    ("Status: OK", r"OK"),
    ("Error code: 404", r"\d{3}"),
    ("Version: 1.2.3", r"\d\.\d\.\d"),
    ("Color: red", r"red"),
    ("Size: large", r"large"),
    ("Product: Widget", r"Widget"),
    ("Location: New York", r"New York"),
    ("Time: 12:30", r"\d{2}:\d{2}"),
    ("Message: Hello there!", r"Hello there!"),
    ("Count: 10", r"\d+"),
    ("Value: 3.14", r"\d\.\d{2}"),
    ("Key: abc", r"abc"),
    ("Code: XYZ123", r"[A-Z]{3}\d{3}"),
    ("ID: 56789", r"\d{5}"),
    ("Token: aBcDeFg", r"[a-zA-Z]+"),
    ("Path: /home/user", r"/[\w/]+"),
    ("URL: https://example.org", r"https?://[\w.-]+\.\w+"),
    ("Word: example", r"example"),
    ("Number: 987", r"\d{3}"),
    ("Text: some text", r"some text"),
    ("Data: 1,2,3", r"\d,\d,\d"),
    ("Info: details", r"details"),
    ("Name: Alice", r"Alice"),
    ("City: London", r"London"),
    ("Country: France", r"France"),
    ("Job: Developer", r"Developer"),
    ("Animal: Dog", r"Dog"),
    ("Fruit: Orange", r"Orange"),
    ("Vegetable: Carrot", r"Carrot"),
    ("Month: December", r"December"),
    ("Day: Monday", r"Monday")
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
    

    # print(results)
    t_1 = time.time()
    print(f"Python took: {(t_1 - t_0) * 1000}ms")

def test_threaded_rust():
    
    from concurrent.futures import ThreadPoolExecutor

    def worker_fn(content, regex, results):
        results.append(
            regex_maturin.regex_match(content, regex)
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

    # print(results) 
    t_1 = time.time()
    print(f"Rust took: {(t_1 - t_0) * 1000}ms")


def test_threaded_rust_indices():
    
    from concurrent.futures import ThreadPoolExecutor

    def worker_fn(content, regex, results):
        r = []
        nullable_result = regex_maturin.regex_match_index(content, regex)
        if nullable_result is None:
            results.append(None)
            return

        for index_tuple in nullable_result:
            if index_tuple is not None:
                r.append(content[index_tuple[0]:index_tuple[1]])

        results.append(r)

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

    # print(results) 
    t_1 = time.time()
    print(f"Rust took: {(t_1 - t_0) * 1000}ms")

if __name__ == "__main__":
    test_threaded_python()
    test_threaded_rust()
    test_threaded_rust_indices()
