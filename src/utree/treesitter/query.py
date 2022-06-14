from utree.languages import QUERIES

def execute_query(language_obj, query_string, tree):
    query = language_obj.query(query_string)
    return query.captures(tree.root_node)

def generic_query(self, language, tree, query_type):
    """
    The generic_query function is used to make queries on trees for which
    we have pre-defined functions.
    
    Args:
        self: Access the attributes of the class
        language: Look up the correct language object
        tree: Get the root of the tree
        query_type: Specify which query to run
    
    Returns:
        A list of tuples
    
    Doc Author:
        Trelent
    """
    language_object = self.language_objects.get(language, None)
    if language_object is None:
        return None

    functions_query = QUERIES[language][query_type]

    return execute_query(language_object, functions_query, tree)