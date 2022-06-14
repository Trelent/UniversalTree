classes = """
[
    (class_definition
        name: (identifier) @class.name
        body: (block) @class.body
    ) @class.def
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
    (class_definition
        body: (block
            (function_definition
                name: (identifier) @method.name
                parameters: (parameters) @method.params
                body: (block) @method.body
            ) @method.def
        )
    )
]
"""