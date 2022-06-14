from tree_sitter import Language, Parser
from typing import Dict, Union

from utree.languages import SUPPORTED_LANGUAGES
from utree.treesitter.util import _fix_language_names

def load_language_objects(
    grammar_path: str, languages_to_load: list, should_ignore_errors: bool
) -> Dict[str, Union[Language, None]]:
    did_load_all_languages = True
    resultant_languages = dict.fromkeys(SUPPORTED_LANGUAGES)
    for language in languages_to_load:
        # Account for multiple C# name variations
        language = _fix_language_names(language)

        if language not in SUPPORTED_LANGUAGES:
            did_load_all_languages = False
            continue
        
        language_obj = _load_language(grammar_path, language)
        if language_obj:
            resultant_languages[language] = language_obj
        else:
            did_load_all_languages = False
            continue
        
    if not did_load_all_languages:
        # Warn the user if any of the languages failed to load
        if should_ignore_errors:
            print(
                "UTREE WARNING: Failed to load all languages specified. Continuing with {lang_count}/{intended_count} languages.".format(
                    lang_count=len(resultant_languages), intended_count=len(languages_to_load)
                )
            )
            return resultant_languages
        else:
            print("UTREE ERROR: Failed to load all languages specified.")
            return None
    
    return resultant_languages

    

def load_language_parsers(
    language_objects
) -> Dict[str, Union[Language, None]]:
    """
    The _load_languages function loads the languages specified in the languages_to_load list.
    If a language fails to load, it is not added to the loaded_languages list and a warning is printed.

    :param self: Reference the object instance of the Parser class
    :param languages_to_load: Specify which languages to load
    :return: A list of all the 'Language' objects that were successfully loaded
    :doc-author: Trelent
    """
    language_parsers = dict.fromkeys(SUPPORTED_LANGUAGES)
    for language_obj in language_objects:
        language_obj = language_objects[language_obj]
        parser = Parser()
        parser.set_language(language_obj)
        language_parsers[language_obj.name] = parser
    
    return language_parsers


def _load_language(
    grammar_path: str, language: str
) -> Union[Language, None]:
    """
    Attempts to load the language from the specified grammar file. If it
    fails, it prints an error message and returns None.

    :param grammar_path: Specify the path to the grammar file
    :param language: Load the grammar file for a specific language
    :return: A language object
    :doc-author: Trelent
    """
    try:
        return Language(grammar_path, language)
    except Exception as e:
        print("UTREE WARNING: Failed to load language: " + language)
        print(str(e.with_traceback()))
        return None
