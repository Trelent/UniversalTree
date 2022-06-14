# UniveralTree
UniversalTree (UTree for short) is an opinionated source code parsing module for Python. It acts as an abstraction layer on top of [Tree-Sitter](https://tree-sitter.github.io/tree-sitter/) to return useful metadata about a snippet of source code.

> Warning: UTree is still in active development! Minor releases may contain breaking changes.

___
### Abstract:
UTree is a python module providing an easy way to parse code in the world's most popular programming languages for common patterns, such as functions, methods, classes and variable declarations. UTree also provides access to the low-level abstract syntax tree for a parsed piece of text, in case the provided abstractions aren't enough.