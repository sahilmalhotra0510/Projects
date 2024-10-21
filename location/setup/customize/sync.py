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
        skip_next_line = False  # Flag to skip the line after detecting a blank line before Free up Disk Space
        skip_next_line_OLLAMA = False  # Flag to skip the next line if `env:` is found with SKIP_OLLAMA_TESTS
        lines_to_skip = 0 # Counter for how many lines to skip

        for i, line in enumerate(lines):
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

            elif filename == "cypress/e2e/chat.cy.ts":
                if "beforeEach(function ()" in line:
                    updated_lines.append("\tbeforeEach(() => {\n")
                    in_beforeEach = True
                elif in_beforeEach:
                    if "cy.loginAdmin();" in line or "cy.visit('/');" in line:
                        line = line.replace("\t", "", 1)
                        if "cy.loginAdmin();" in line:
                            updated_lines.append("		// Login as the admin user\n")
                            updated_lines.append("		cy.loginAdmin();\n")
                        elif "cy.visit('/');" in line:
                            updated_lines.append("		// Visit the home page\n")
                            updated_lines.append("		cy.visit('/');\n")
                    elif "});" in line:
                        updated_lines.append(line)
                        in_beforeEach = False
                else:
                    updated_lines.append(line)

            elif filename == ".github/workflows/format-backend.yaml":
                # Don't include the - '*' line
                if "*" in line:
                    continue
                else:
                    updated_lines.append(line)
            
            elif filename == ".github/workflows/integration-test.yml":

                if "      - '*'" in line:
                    #Remove the line with the - '*'
                    continue

                # Detect `env:` followed by `SKIP_OLLAMA_TESTS: 'true'`
                elif 'env:' in line and i + 1 < len(lines) and "SKIP_OLLAMA_TESTS: 'true'" in lines[i + 1]:
                    skip_next_line_OLLAMA = True
                    continue  # Skip the `env:` line

                # Skip the `env:` and `SKIP_OLLAMA_TESTS` lines
                elif skip_next_line_OLLAMA:
                    if "SKIP_OLLAMA_TESTS: 'true'" in line:
                        skip_next_line_OLLAMA = False  # Reset the flag after skipping this line
                        continue  # Skip the `SKIP_OLLAMA_TESTS:` line
                
                # Skip the blank line and the '- name: Free up Disk Space' line
                elif skip_next_line:
                    if line.strip() == "":
                        continue  # Skip the blank line
                    elif "- name: Free up Disk Space" in line:
                        skip_next_line = False  # Reset the flag after skipping this line
                        continue  # Skip the 'Free up Disk Space' line

                # Detect the blank line followed by `- name: Free up Disk Space`
                elif line.strip() == "" and i + 1 < len(lines) and "- name: Free up Disk Space" in lines[i + 1]:
                    skip_next_line = True
                    continue  # Skip the blank line

                elif 'run: bash ./.github/script/free-disk-space.sh' in line:
                    continue

                else:
                    #Uncomment commented lines
                    for phrase in phrase_list:
                        if stripped_line == phrase:
                            if line.lstrip().startswith('#'):
                                line = line.replace('#', '', 1)
                            break
                    updated_lines.append(line)
            
            elif filename == "docker-compose.api.yaml":
                updated_lines.append(line[2:])

            else:
                # Process other files as before
                for phrase in phrase_list:
                    if phrase in stripped_line:
                        if line.lstrip().startswith('#'):
                            line = line.replace('# ', '', 1)
                        break
                updated_lines.append(line)

        with open(pathToRoot + filename, 'w') as file:
            file.writelines(updated_lines)

adding_ollama_lines(phrases)