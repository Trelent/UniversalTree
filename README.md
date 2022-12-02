# UniveralTree
UniversalTree (UTree for short) is an opinionated source code parsing module for Python.
It acts as an abstraction layer on top of
[Tree-Sitter](https://tree-sitter.github.io/tree-sitter/) to return useful metadata about
a snippet of source code.

> Warning: UTree is still in active development! Minor releases may contain breaking
changes. Production use is not recommended.
___
### Setup
Before you can use UTree, you must first create a "grammar". This is used to tell the
underlying library, TreeSitter, how to parse code in any given language. A utility to
do so is provided in the `grammar_builder` folder. You must install the tree-sitter
python module, then run `grammar_builder/vendors/_clone_vendors.sh`. This script will
clone several git repos to this folder, which contain the grammars for various languages.

Combined, these scripts will create a grammar that allows you to parse:
- C
- C++
- C#
- Go
- Java
- JavaScript
- Kotlin
- Python
- PHP
- Ruby
- TypeScript

This grammar will be forwards compatible as we add the languages listed above. Supported
languages (those you can query using UTree) are currently limited to:
- C#
- Java
- JavaScript
- Python
___
### General Usage
UTree is very simple to use. Once you have a grammar file on hand, you can use Utree as
follows:

```python
from utree.parser import Parser

parser = Parser("./path/to/grammar.so")

code_snippet = """def some_func():
    print("hello, world")

def another_function():
    print("Hmm...")

class test:
    def __init__():
        print("It's a class!")

    def some_method(self):
        print("and a method!")
"""

result = parser.parse(code_snippet, "python")
print(result)
```

And with that, you should get a nice dictionary like so:
```javascript
{
    "classes": {
        ...
    },
    "functions": {
        ...
    },
    "methods": {
        ...
    }
    
}
```
