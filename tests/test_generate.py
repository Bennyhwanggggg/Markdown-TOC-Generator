from toc_generator import get_content


def test_generate_toc():
    res = generate('.')
    print(res)