# customize.py

import sys
import importlib
import re
import os

file_lines = importlib.import_module("file-lines")
phrases = file_lines.phrases

def removing_ollama_lines(phrases):
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
            elif filename == "chat.cy.ts":
                if "beforeEach(() =>" in line:
                    # Replace the arrow function with the full beforeEach block
                    updated_lines.extend([f"{phrase}\n" for phrase in phrase_list])
                    in_beforeEach = True
                elif in_beforeEach and "});" in line:
                    updated_lines.append(line)
                    in_beforeEach = False
                elif not in_beforeEach:
                    updated_lines.append(line)

            elif filename == "format-backend.yaml":
                # Remove the '- *' line using phrases defined in file-lines.py
                updated_lines = []
                for line in lines:
                    should_remove = False
                    for phrase in phrase_list:
                        if phrase in line:
                            should_remove = True
                            break
                    if not should_remove:
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