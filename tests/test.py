from utree.parser import Parser

grammar_path = "grammar.so"
parser = Parser(
    grammar_path=grammar_path,
    languages=[
        "c_sharp",
        "java",
        "javascript",
        "python",
    ]
)

test_func="""def test():
    print("This is a test function")
"""

test_func = bytes(test_func, "utf-8")

result = parser.parse(test_func, "python")
print(result)