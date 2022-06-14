from tree_sitter import Language

Language.build_library(
    # Store the library in the `result` directory for now
    "result/grammar.so",
    # Include the languages we want to build
    [
        "vendor/tree-sitter-c",
        "vendor/tree-sitter-c-sharp",
        "vendor/tree-sitter-cpp",
        "vendor/tree-sitter-go",
        "vendor/tree-sitter-java",
        "vendor/tree-sitter-javascript",
        "vendor/tree-sitter-kotlin",
        "vendor/tree-sitter-php",
        "vendor/tree-sitter-python",
        "vendor/tree-sitter-ruby",
        "vendor/tree-sitter-typescript/typescript",
    ],
)
