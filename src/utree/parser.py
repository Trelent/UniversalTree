from utree.languages import SUPPORTED_LANGUAGES
from utree.treesitter.loader import load_language_objects, load_language_parsers
from utree.treesitter.query import generic_query

import os


class Parser:
    def __init__(
        self, grammar_path, languages=SUPPORTED_LANGUAGES, ignore_errors=False
    ):
        self.grammar_path = os.path.abspath(grammar_path)
        self.language_objects = load_language_objects(self.grammar_path, languages, ignore_errors)
        self.language_parsers = load_language_parsers(self.language_objects)

    def parse(self, source_code, language):
        """
        The parse function takes a string of source code and returns a JSON
        representation of the classes, functions, and methods defined in that code.
        
        Args:
            self: Reference the class itself
            source_code: Pass the source code to be parsed
            language: Determine which language the source code is written in
        
        Returns:
            A dictionary with three keys: classes, functions and methods
        
        Doc Author:
            Trelent
        """
        # Try to parse our text into an AST using tree-sitter
        tree = self._parse_text(source_code, language)
        if tree is None:
            return None

        # Let's create a JSON representation of the parsed code
        result = {
            "classes": self._get_classes(language, tree),
            "functions": self._get_functions(language, tree),
            "methods": self._get_methods(language, tree)
        }

        return result

    def _get_classes(self, language, tree):
        return generic_query(language, tree, "classes")

    def _get_functions(self, language, tree):
        return generic_query(language, tree, "functions")
    
    def _get_methods(self, language, tree):
        return generic_query(language, tree, "methods")

    def _parse_text(self, text: str, language: str):
        language_parser = self.language_parsers.get(language, None)
        if language_parser is None:
            return None

        return language_parser.parse(text)