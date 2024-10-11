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
- **Support for Nested JSON**: Extend the parsing logic to handle nested JSON objects and arrays, which are common in real-world data.
- **Integration with External APIs**: Add functionality to fetch JSON data from external APIs or URLs, enhancing the class's utility in web applications.
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
# Usage Example for JsonGo Class

from jsongo import JsonGo  # Assuming the class is saved in a file named json_go.py

# Initialize JsonGo with a JSON file path
json_parser = JsonGo(path='json2.json')

# Print the number of JSON objects
print(f"Number of JSON objects: {json_parser.length()}")

# Convert JSON data to a list of dictionaries
json_data = json_parser.convertToDic(path='json2.json')
print(f"Converted JSON data: {json_data}")

# Add a new dictionary to the current JSON data
new_data = {"name": "John Doe", "age": 30}
json_parser.add(new_data)

# Convert the current JSON data to a JSON string and save it to a file
json_parser.convertToJson(path='output.json')

# Display the first few entries of the JSON data
print("First few entries:")
print(json_parser.head(number=3))

# Fetch and validate JSON data from an API
try:
    api_data = json_parser.getAPI('https://dummyapi.online/api/users')
    json_parser.json_data = api_data
    print(f"Fetched API data: {json_parser.head()}")
except Exception as e:
    print(f"Error fetching API data: {e}")
```

## Upcoming Features 🚀

More features are coming soon to JsonGo! Here's a sneak peek at what's in development:

- **Error Handling Improvements**: Improve error handling by using custom exception classes. This can make it easier to debug and understand issues when they arise.
- **Search and Filter Functionality**:
  - Add methods to search for specific keys or values within the JSON data.
  - Implement filtering capabilities to extract subsets of the data based on certain criteria.
- **Delete Operations**: Provide methods to update or delete entries within the JSON data, allowing for more dynamic data manipulation.
- **Performance Optimization**: Review the code for performance bottlenecks, especially in parsing large JSON files, and optimize where possible.
- **Command-Line Interface (CLI)**: Create a CLI tool that utilizes this class for processing JSON files from the command line, offering features like conversion, validation, and formatting.

Stay tuned for these updates, and feel free to contribute if you'd like to help bring these features to life! 🤝

## Contributing 🤝

Contributions are welcome! Feel free to submit issues or pull requests. Please make sure to follow the coding standards and include tests when adding new features.

### License 📄

This project is licensed under the MIT License. For more details, please refer to the LICENSE file in the repository.

