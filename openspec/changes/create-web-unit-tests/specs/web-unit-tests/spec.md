## ADDED Requirements

### Requirement: Unit tests for web module functions
The system SHALL provide unit tests for all public functions in the web module to enable regression testing and CI/CD integration.

#### Scenario: get_rendered_html returns expanded HTML
- **WHEN** `get_rendered_html` is called with a Playwright page object
- **THEN** the function SHALL return the outerHTML of the document with Shadow DOM content expanded

#### Scenario: scroll_page scrolls until no new content
- **WHEN** `scroll_page` is called with a Playwright page object
- **THEN** the function SHALL scroll the page up to 30 times, stopping early if no new property cards load after 3 consecutive scrolls

#### Scenario: leer_config loads valid YAML file
- **WHEN** `leer_config` is called with a path to a valid YAML file
- **THEN** the function SHALL return a dictionary with the parsed YAML content

#### Scenario: leer_config raises FileNotFoundError for missing file
- **WHEN** `leer_config` is called with a path to a non-existent file
- **THEN** the function SHALL raise `FileNotFoundError`

#### Scenario: leer_config raises ValueError for non-file path
- **WHEN** `leer_config` is called with a path to a directory
- **THEN** the function SHALL raise `ValueError`