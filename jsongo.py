from datetime import datetime

class JsonGo:
    def __init__(self, path = None):        
        
        if path:
            self.json_data = self.convertToDic(path=path)
        else: 
            self.json_data = []
 
    def length(self) -> int:
        return len(self.json_data)
    
    def convertToDic(self, path = None, json_string = None) -> list:
        
        """
        Converts a JSON file into a list of dictionaries.

        Args:
            path (str): The path to the JSON file.
            json_string (str): JSON formated string value 

        Returns:
            list: A list of dictionaries, where each dictionary represents a JSON object from the file.

        Raises:
            Exception: If the file does not contain valid JSON.
            Exception: If the given string does not contain valid JSON.
        """
        if path:   
            try:
                with open(path, 'rb') as file:
                    byte_code = file.read()
                    json_file = byte_code.decode('utf-8')
            except Exception as e:
                raise Exception(f"An error occured while converting: {e}")
        elif json_string:
            json_file = json_string
        else:
            raise Exception("No path or string given!")
        
        # Call JSON validator function
        self.JSON_Validator(json_string=json_file)
        
        json_object = []
        
        # Remove '[' and ']' from the JSON string if they exist
        inside_array = json_file.strip()
        if json_file.startswith("["):
            inside_array = json_file.strip()[1:-1].strip()
        
        current_object = ''
        open_braces = 0
        
        for char in inside_array:
            if char == '{':
                open_braces += 1
            elif char == '}':
                open_braces -= 1
            
            current_object += char
            
            if open_braces == 0 and current_object.strip():
                json_object.append(current_object.strip())
                current_object = ''

        cleaned_objects = []
        open_braces = 0
                
        cleaned_objects = [obj for obj in json_object if obj != ","]
        
        python_dicts = []
        
        for obj in cleaned_objects:
            result = {}
            json_str = obj.strip('{} ')
            entries = json_str.split(',\r\n')
            for entry in entries:
                key, value = entry.split(':')
                key = key.strip().strip('"')
                value = value.strip().strip('"')
                if "[" in value:
                    value = value.strip('[]').strip()
                    list_of_values = value.split(",")
                    for i in range(len(list_of_values)):
                        list_of_values[i] = list_of_values[i].strip().strip('"')
                    result[key] = list_of_values
                else:    
                    result[key] = value
            python_dicts.append(result)
        
        return python_dicts   
    def convertToJson(self, dic=None, path=None):
        """
        Converts a given dictionary or the dictionaries stored in the object itself to a JSON string and writes it to a file.

        Args:
            dic (dict): The dictionary to be converted to a JSON. If not provided, the dictionaries stored in the object itself will be used.
            path (str): The path to the file that the JSON string will be written to. If not provided, a file with a name in the format "YYYY-MM-DD_HH-MM-SS_json.json" will be created in the same directory as the script.

        Raises:
            Exception: If the method is called without providing a dictionary and the object itself does not contain any dictionaries.
        """
        if not path:
            now = datetime.now()
            date_timer_str = now.strftime("%Y-%m-%d_%H-%M-%S")
            path = date_timer_str + "_json.json" 

        if dic:
            string = self.toString(dic=dic)
            string = string.replace("'",'"')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(string)
            return

        if self.json_data:
            string = self.toString(dic=self.json_data)
            string = string.replace("'",'"')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(string)
            return

        raise Exception("Wrong usage!")
    
    def __str__(self) -> str:
        if self.json_data:
            string = "["
            for entry in self.json_data:
                string += "\n\t{"
                for key, value in entry.items():
                     string += f'\n\t\t"{key}" : "{value}",'
                string = string[:-1]
                string += "\n\t},"
            string = string[:-1]
            string += "\n]"
            return string
        return ""

    def toString(self, dic) -> str:
        if dic:
            string = "["
            for entry in self.json_data:
                string += "\n\t{"
                for key, value in entry.items():
                     string += f'\n\t\t"{key}" : "{value}",'
                string = string[:-1]
                string += "\n\t},"
            string = string[:-1]
            string += "\n]"
            return string
        return ""
        
    def head(self, number=5) -> str:
        """
        Returns a string representation of the first n elements of the JSON data.

        Args:
            number (int): The number of elements to return. Defaults to 5.

        Returns:
            str: A string representation of the first n elements of the JSON data.
        """
        if self.json_data:
            counter = 1
            string = "["
            for entry in self.json_data:
                string += "\n\t{"
                for key, value in entry.items():
                     string += f'\n\t\t"{key}" : "{value}",'
                string = string[:-1]
                string += "\n\t},"
                if counter == number:
                    string = string[:-1]
                    string += "\n]"
                    return string
                counter += 1
            string = string[:-1]
            string += "\n]"
            return string
        return ""
    
    def add(self, json):
        """
        Adds a dictionary or a JSON string to the internal data structure.
        
        Args:
            json (dict or str): The dictionary or JSON string to add.
        
        Raises:
            Exception: If the argument is not a dictionary or a string, or if the string is empty.
        """
        if json:
            if isinstance(json, dict):
                self.json_data.append(json)
            elif isinstance(json, str):
                self.JSON_Validator(json_string=json)
                converted_string = self.convertToDic(json_string=json)
                self.json_data.extend(converted_string)
            else:
                raise Exception("Only dictionary or string accepted!")
        else:
            raise Exception(f"{json} is empty!")
        
    def JSON_Validator(self, path = None, json_string = None):
        
        """
        Validates a JSON file against the standard JSON format.

        Args:
            path (str): The path to the JSON file.

        Raises:
            Exception: If the file does not exist or the JSON is not valid.
        """
        if path:
            try:
                with open(path, 'rb') as file:
                    byte_code = file.read()
                    json_file = byte_code.decode('utf-8')
            except Exception as e:
                e.add_note("File not found!")
        elif json_string:
            json_file = json_string
        else:
            json_file = self.json_string
        
        if json_file.count('[') != json_file.count(']'):
            raise Exception("The number of '[' does not equal with the number of ']'!")
        
        if json_file.count('{') != json_file.count('}'):
            raise Exception("The number of '{' does not equal with the number of '}'!")
        
        if json_file.count('"') % 2 != 0:
            raise Exception("Not valid JSON format!")
        
        for i, char in enumerate(json_file):
            if char == ':':
                if i - 2 <= 0:
                    raise Exception("Not valid JSON format!")
                if json_file[i - 1] not in ' "':
                    raise Exception("Not valid JSON format!")
                elif json_file[i - 1] in ' ' and json_file[i - 2] not in '"':
                    raise Exception("Not valid JSON format!")
        return True
