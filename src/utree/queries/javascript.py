classes = """
[
    (class_definition
        name: (identifier) @function.name
        parameters: (parameters) @function.params
        body: (block) @function.body
    ) @function.def
]
"""

functions="""
[
    (function_definition
        name: (identifier) @function.name
        parameters: (parameters) @function.params
        body: (block) @function.body
    ) @function.def
]
"""

methods="""
[
    (function_definition
        name: (identifier) @function.name
        parameters: (parameters) @function.params
        body: (block) @function.body
    ) @function.def
]
"""