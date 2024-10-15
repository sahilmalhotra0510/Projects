# customize.py

import sys
import importlib
import re
import os

file_lines = importlib.import_module("file-lines")
phrases = file_lines.phrases

def removing_ollama_lines(phrases):
    pathToRoot = "/Users/dhananjaysurti/model_earth/open-webui/"
    if len(sys.argv) > 1:
        pathToRoot = sys.argv[1]
        if not pathToRoot.endswith('/'):
            pathToRoot += '/'
    in_branches_section = False  # Flag to track when inside the branches section
    star_exists = False  # Flag to track if '- '*' already exists
    capture_checkout = False  # Flag to track when to append the lines after checkout@v4
    found_wildcard = False
    in_pr_line = False
    for filename, phrase_list in phrases.items():
        file_path = pathToRoot + filename
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist. Skipping.")
            continue
        print(f"Processing file: {pathToRoot}{filename}")

        with open(pathToRoot + filename, 'r') as file:
            lines = file.readlines()

        updated_lines = []
        env_block_added = False
        env_block_exists = False
        in_beforeEach = False
        if filename == "cypress.config.ts":
            # Check if env block already exists
            env_block_exists = any("env:" in line for line in lines)

        for line in lines:
            stripped_line = line.strip()

            if filename == "cypress.config.ts":
                if "defineConfig({" in line:
                    updated_lines.append(line)
                    if not env_block_exists:
                        # Add the env block after defineConfig({
                        updated_lines.extend([f"  {phrase}\n" for phrase in phrase_list])
                        env_block_added = True
                elif "}" in line and not any(char.isalnum() for char in line) and not env_block_added and not env_block_exists:
                    # If we reached the end and haven't added the env block, add it before the closing brace
                    updated_lines.extend([f"  {phrase}\n" for phrase in phrase_list])
                    updated_lines.append(line)
                    env_block_added = True
                else:
                    updated_lines.append(line)
            elif filename == "cypress/e2e/chat.cy.ts":
                if "beforeEach(() =>" in line:
                    # Replace the arrow function with the full beforeEach block
                    updated_lines.extend([f"{phrase}\n" for phrase in phrase_list])
                    in_beforeEach = True
                elif in_beforeEach and "});" in line:
                    updated_lines.append(line)
                    in_beforeEach = False
                elif not in_beforeEach:
                    updated_lines.append(line)

            #Updated so that its correct now
            elif filename == ".github/workflows/format-backend.yaml":
                # Check if the '- *' line exists, if not, add it under the branches in both push and pull_request
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
            
            elif filename == ".github/workflows/integration-test.yml":
                
                if "pull_request" in line:
                    in_pr_line = True
                # Adding the *
                if "branches:" in line:
                    in_branches_section = True
                    updated_lines.append(line)
                elif in_branches_section:
                    # Check for branch lines
                    if line.strip().startswith("-"):
                        if "'*'" in line:
                            star_exists = True  # Set flag if '- '*' already exists
                        updated_lines.append(line)
                    else:
                        # We are leaving the branches section, insert '- *' if not already present
                        if not star_exists and in_pr_line:
                            updated_lines.append("      - '*'\n")  # Add the '- *' after existing branches
                        in_branches_section = False  # Exit the branches section
                        updated_lines.append(line)  # Continue processing the rest of the file
                        in_pr_line = False

                # Adding the name: Free up disk space code
                # Detect `checkout@v4` and add the three lines after it (not the uncommented one)
                elif 'uses: actions/checkout@v4' in line and '#' not in line:
                    capture_checkout = True
                    updated_lines.append(line)  # Add the checkout@v4 line itself
                elif capture_checkout:
                    # Add the specified three lines after `checkout@v4`
                    updated_lines.append("\n      - name: Free up Disk Space\n")
                    updated_lines.append("        run: bash ./.github/script/free-disk-space.sh\n\n")
                    capture_checkout = False  # Reset the flag after adding the lines
                        # Detect `config:` and add the `env:` and `SKIP_OLLAMA_TESTS` lines after it
                elif 'config:' in line:
                    updated_lines.append(line)  # Add the config: line itself
                    # Insert the two lines after config:
                    updated_lines.append("        env:\n")
                    updated_lines.append("          SKIP_OLLAMA_TESTS: 'true'\n")
                else:
                    for phrase in phrase_list:
                        if stripped_line == phrase:
                            if not line.lstrip().startswith('#'):
                                line = f"# {line}"
                            break
                    updated_lines.append(line)

            else:
                # For other files, add hashtags to matching lines
                for phrase in phrase_list:
                    if stripped_line == phrase:
                        if not line.lstrip().startswith('#'):
                            line = f"# {line}"
                        break
                updated_lines.append(line)
            

        if filename == "cypress.config.ts" and env_block_exists:
            print("env block already exists in cypress.config.ts. Skipping addition.")
        elif filename == "cypress.config.ts" and env_block_added:
            print("env block added to cypress.config.ts.")
        elif filename == "chat.cy.ts":
            print("beforeEach block updated in chat.cy.ts.")
        
        with open(pathToRoot + filename, 'w') as file:
            file.writelines(updated_lines)

removing_ollama_lines(phrases)