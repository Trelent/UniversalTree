from utree.queries import c_sharp, java, javascript, python

SUPPORTED_LANGUAGES = [
    "c_sharp",
    "java",
    "javascript",
    "python",
]

QUERIES = {}

for language in [c_sharp, java, javascript, python]:
    lang_name = language.__name__.split('.')[-1]
    QUERIES[lang_name] = {
        "functions": language.functions,
        "methods": language.methods,
        "classes": language.classes
    }