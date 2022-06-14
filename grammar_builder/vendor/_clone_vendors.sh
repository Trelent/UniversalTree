#! /bin/bash

LANGUAGE_REPOS="https://github.com/tree-sitter/tree-sitter-c https://github.com/tree-sitter/tree-sitter-cpp https://github.com/tree-sitter/tree-sitter-c-sharp https://github.com/tree-sitter/tree-sitter-go https://github.com/tree-sitter/tree-sitter-java https://github.com/tree-sitter/tree-sitter-javascript https://github.com/tree-sitter/tree-sitter-python https://github.com/fwcd/tree-sitter-kotlin https://github.com/tree-sitter/tree-sitter-php https://github.com/tree-sitter/tree-sitter-ruby https://github.com/tree-sitter/tree-sitter-typescript"
REPO_ARRAY=($LANGUAGE_REPOS)

# Iterate over all language repos using ' ' as a delimiter and run git clone on the resultant url
for repo in "${REPO_ARRAY[@]}"
do
    git clone $repo
done