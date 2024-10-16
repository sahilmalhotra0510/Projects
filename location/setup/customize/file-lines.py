# file-lines.py
# Used by both customize.py and sync.py

phrases = {
    # "cypress.config.ts": [
    #     "env: {",
    #     "    SKIP_OLLAMA_TESTS: 'false'",
    #     "}"
    # ],
    "docker-compose.api.yaml": [
        'services:',
        '  ollama:',
        '    # Expose Ollama API outside the container stack',
        '    ports:',
        '      - ${OLLAMA_WEBAPI_PORT-11434}:11434'
    ],
    "docker-compose.yaml": [
        'ollama:',
        '  volumes:',
        '    - ollama:/root/.ollama',
        '  container_name: ollama',
        '  pull_policy: always',
        '  tty: true',
        '  restart: unless-stopped',
        '  image: ollama/ollama:${OLLAMA_DOCKER_TAG-latest}',

        'args:',
        "  OLLAMA_BASE_URL: '/ollama'",

        "depends_on:",
        "  - ollama",

        "environment:",
        "  - 'OLLAMA_BASE_URL=http://ollama:11434'",
        "  - 'WEBUI_SECRET_KEY='",

        "ollama: {}"
    ],

    ".github/workflows/integration-test.yml" : [
        '- name: Wait for Ollama to be up',
        'timeout-minutes: 5',
        'run: |',
        '  until curl --output /dev/null --silent --fail http://localhost:11434; do',
        "    printf '.'",
        '    sleep 1',
        '  done',
        '  echo "Service is up!"',

        '- name: Preload Ollama model',
        'run: |',
        '  docker exec ollama ollama pull qwen:0.5b-chat-v1.5-q2_K',
    ],

    "chat.cy.ts" : [
        'env: {',
        "    SKIP_OLLAMA_TESTS: 'false'",
        '},',
    ],

    "cypress/e2e/chat.cy.ts": [
        'beforeEach(function () {',
        "    if (Cypress.env('SKIP_OLLAMA_TESTS')) {",
        "        cy.log('Skipping all tests in the Settings suite');",
        '        this.skip();',
        '    } else {',
        '        // Login as the admin user',
        '        cy.loginAdmin();',
        '        // Visit the home page',
        "        cy.visit('/');",
        '    }',
    ],

    ".github/workflows/format-backend.yaml": [
        "      - '*'"
    ],

    ".github/workflows/integration-test.yml": [
        
    ]
}


# 
# SKIP_OLLAMA_TESTS: 'true'