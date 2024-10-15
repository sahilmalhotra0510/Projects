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
                        line = line.replace("\t", "", 1)
                        updated_lines.append(line)
                    elif "});" in line:
                        updated_lines.append(line)
                        in_beforeEach = False
                else:
                    updated_lines.append(line)

            elif filename == ".github/workflows/format-backend.yml":
                # Don't include the - '*' line
                if "- '*'" in line:
                    continue
                else:
                    updated_lines.append(line)
            
            elif filename == ".github/workflows/integration-test.yml":
                skip_next_lines = False # Flag to track when to start skipping lines
                lines_to_skip = 0 # Counter for how many lines to skip
                if "- '*'" in line:
                    #Remove the line with the - '*'
                    continue
                elif 'env:' in line:
                    #Remove the line with the env:
                    continue
                elif 'SKIP_OLLAMA_TESTS:' in line:
                    #Remove the line with SKIP_OLLAMA_TESTS:
                    continue
                elif 'uses: actions/checkout@v4' in line:
                    # Start skipping the next 3 lines
                    skip_next_lines = True
                    lines_to_skip = 3  # Set counter to 3 lines after this one
                    updated_lines.append(line)
                elif skip_next_lines:
                    if lines_to_skip > 0:
                        lines_to_skip -= 1  # Decrement the counter
                        continue  # Skip this line
                    else:
                        skip_next_lines = False  # Reset the flag after 3 lines are skipped
                else:
                    #Uncomment commented lines
                    if line.lstrip().startswith('#'):
                        line = line.replace('# ', '', 1) 
                    updated_lines.append(line)

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