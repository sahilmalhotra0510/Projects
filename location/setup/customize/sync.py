# sync.py

import sys
import importlib
import os

file_lines = importlib.import_module("file-lines")
phrases = file_lines.phrases

def adding_ollama_lines(phrases):
    pathToRoot = "../../../"
    if len(sys.argv) > 1:
        pathToRoot = sys.argv[1]
        if not pathToRoot.endswith('/'):
            pathToRoot += '/'

    for filename, phrase_list in phrases.items():
        file_path = pathToRoot + filename
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist. Skipping.")
            continue
        print(f"\rProcessing file: {pathToRoot}{filename}")

        with open(pathToRoot + filename, 'r') as file:
            lines = file.readlines()

        updated_lines = []
        skip_env_block = False
        in_beforeEach = False

        for line in lines:
            stripped_line = line.strip()
            if filename == "cypress.config.ts":
                if "env: {" in line:
                    skip_env_block = True
                    continue
                elif skip_env_block:
                    if "}" in line and not any(char.isalnum() for char in line):
                        skip_env_block = False
                    continue
                else:
                    updated_lines.append(line)

            elif filename == "chat.cy.ts":
                if "beforeEach(function ()" in line:
                    updated_lines.append("\tbeforeEach(() => {\n")
                    in_beforeEach = True
                elif in_beforeEach:
                    if "cy.loginAdmin();" in line or "cy.visit('/');" in line:
                        updated_lines.append(line)
                    elif "});" in line:
                        updated_lines.append(line)
                        in_beforeEach = False
                else:
                    updated_lines.append(line)

            elif filename == ".github/workflows/format-backend.yaml":
                # Check if the '- *' line exists, if not, add it under the branches in both push and pull_request
                found_wildcard = False
                for line in lines:
                    if "- '*'" in line:
                        found_wildcard = True
                        break
                if not found_wildcard:
                    # Locate the branches section under 'push' and 'pull_request'
                    for i, line in enumerate(lines):
                        if "branches:" in line and "push" in lines[i-1]:
                            lines.insert(i+1, "      - '*'\n")

                updated_lines = lines

            else:
                # Process other files as before
                for phrase in phrase_list:
                    if stripped_line == phrase:
                        if line.lstrip().startswith('#'):
                            line = line.replace('#', '', 1)
                        break
                updated_lines.append(line)

        with open(pathToRoot + filename, 'w') as file:
            file.writelines(updated_lines)

adding_ollama_lines(phrases)