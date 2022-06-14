from enum import Enum
from typing import Union, List


class NodeType(Enum):
    FUNCTION = 1
    METHOD = 2
    CLASS = 3
    VARIABLE = 4
    EXCEPTION = 5
    RETURN = 6


class Point:
    def __init__(self, col: int, line: int) -> None:
        self.col = col
        self.line = line

    def __str__(self) -> str:
        return f"{self.line}:{self.col}"


class JsonNode:
    def __init__(self, type: NodeType, start: Point, end: Point, children) -> None:
        self.type = type
        self.start = start
        self.end = end
        self.children = children or []

    def __str__(self) -> str:
        return f"JsonNode::{str(self.type)}"


class Class:
    def __init__(self, name: str, start: Point, end: Point, text: str) -> None:
        self.name = name
        self.start = start
        self.end = end
        self.text = text

    def __str__(self) -> str:
        return f"Class::{self.name}"


class Docstring:
    def __init__(self, does_exist: bool, start: Point, end: Point, text: str) -> None:
        self.does_exist = does_exist
        self.start = start
        self.end = end
        self.text = text


class Function:
    def __init__(
        self,
        body: str,
        definition: str,
        docstring: Docstring,
        name: str,
        params: List[str],
    ) -> None:
        self.body = body
        self.definition = definition
        self.docstring = docstring
        self.name = name
        self.params = params

    def __str__(self) -> str:
        return f"Function::{self.name}"

    def rebuild(self):
        return f"{self.definition + self.body}"


class Method:
    def __init__(
        self,
        body: str,
        definition: str,
        docstring: Docstring,
        name: str,
        params: List[str],
        parent: Class,
    ) -> None:
        self.body = body
        self.definition = definition
        self.docstring = docstring
        self.name = name
        self.params = params
        self.parent = parent

    def __str__(self) -> str:
        return f"Method::{self.name}"

    def rebuild(self):
        return f"{self.definition + self.body}"

    def get_surrounding_context(self):
        context = self.parent.text
        return context.replace(self.rebuild(), "<<<METHOD_REPLACEMENT>>>")