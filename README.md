# JsonGo: Simplify Your JSON Handling in Python 📦

## Overview 🌍

JsonGo is a Python library for parsing, manipulating, and validating JSON data. It offers a simple interface to convert JSON files and strings into Python dictionaries and vice versa, while also providing basic validation checks to ensure the integrity of the JSON structure.

### Table of Contents 📑
- [Features](#features-✨)
- [Installation](#installation-🔧)
- [Usage](#usage-📖)
- [Upcoming Features](#upcoming-features-🚀)
- [Contributing](#contributing-🤝)
- [License](#license-📄)

### Features ✨

- **Convert JSON Files to Dictionaries**: Load and parse JSON data from files into Python dictionaries.
- **Convert Strings to Dictionaries**: Parse JSON strings directly into Python dictionaries.
- **Convert Dictionaries to JSON**: Serialize Python dictionaries back into JSON format and save them to files.
- **Basic JSON Validation**: Check the structural integrity of JSON data, including balanced brackets and proper formatting.
- **Add New Entries**: Add new JSON objects or strings to existing data.
- **Retrieve Data Length**: Get the number of entries in the current JSON data.
- **Output Formatted JSON Strings**: Generate human-readable string representations of the JSON data.
- **Preview Data with `head` Method**: Preview the first n entries of the JSON data.

### Installation 🔧

To use JsonGo, ensure you have Python installed. Clone the repository from GitHub:

```bash
git clone https://github.com/davidgalfi/JsonGo.git
```

### Usage 📖

Below are some examples of how to use the JsonGo library:

```python
from jsongo import JsonGo

# Initialize with a path to a JSON file
json_parser = JsonGo("path/to/your/jsonfile.json")

# Convert file content to dictionary
data = json_parser.convertToDic("path/to/your/jsonfile.json")

# Add new entry
json_parser.add({"new_key": "new_value"})

# Convert dictionary back to a JSON file
json_parser.convertToJson(path="output.json")

# Print formatted JSON string
print(json_parser)

# Validate a JSON string
is_valid = json_parser.JSON_Validator_string('{"key": "value"}')
print("Is valid:", is_valid)
```

## Upcoming Features 🚀

More features are coming soon to JsonGo! Here's a sneak peek at what's in development:

- **Support for Nested JSON**: Extend the parsing logic to handle nested JSON objects and arrays, which are common in real-world data.
- **Error Handling Improvements**: Improve error handling by using custom exception classes. This can make it easier to debug and understand issues when they arise.
- **Search and Filter Functionality**:
  - Add methods to search for specific keys or values within the JSON data.
  - Implement filtering capabilities to extract subsets of the data based on certain criteria.
- **Delete Operations**: Provide methods to update or delete entries within the JSON data, allowing for more dynamic data manipulation.
- **Integration with External APIs**: Add functionality to fetch JSON data from external APIs or URLs, enhancing the class's utility in web applications.
- **Performance Optimization**: Review the code for performance bottlenecks, especially in parsing large JSON files, and optimize where possible.
- **Serialization/Deserialization Support**: Implement serialization and deserialization methods to easily convert Python objects into JSON strings and vice versa.
- **Command-Line Interface (CLI)**: Create a CLI tool that utilizes this class for processing JSON files from the command line, offering features like conversion, validation, and formatting.

Stay tuned for these updates, and feel free to contribute if you'd like to help bring these features to life! 🤝

## Contributing 🤝

Contributions are welcome! Feel free to submit issues or pull requests. Please make sure to follow the coding standards and include tests when adding new features.

### License 📄

This project is licensed under the MIT License. For more details, please refer to the LICENSE file in the repository.

