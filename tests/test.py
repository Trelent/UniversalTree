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

test_func="""class apple:

    def __init__():
        print("apple")

    def test(self):
        print("This is a test method")

def not_a_method():
    print("This is not a method")
"""

result = parser.parse(test_func, "python")

funcs = result["functions"]
for func in funcs:
    print(func.name)