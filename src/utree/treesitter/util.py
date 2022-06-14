def _fix_language_names(language: str) -> str:
    if "c" in language and ("sharp" in language or "#" in language):
        return "c_sharp"
    return language

def get_sexpression(tree):
    root = tree.root_node
    return root.sexp()