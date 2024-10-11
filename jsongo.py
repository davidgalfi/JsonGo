from datetime import datetime
import urllib.error
import urllib.request

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
        
        json_file = json_file.replace("\n", "").replace("\r", "").replace(" ", "").strip('[] ')
        
        return self.parse_json(json_str=json_file)

    def parse_json(self, json_str) -> list:
        def parse_value(index):
            if json_str[index] == '{':
                return parse_object(index)
            elif json_str[index] == '[':
                return parse_array(index)
            elif json_str[index] == '"':
                return parse_string(index)
            else:
                return parse_primitive(index)

        def parse_object(index):
            obj = {}
            index += 1  # Skip '{'
            while index < len(json_str) and json_str[index] != '}':
                key, index = parse_string(index)
                index += 1  # Skip ':'
                value, index = parse_value(index)
                obj[key] = value
                if index < len(json_str) and json_str[index] == ',':
                    index += 1  # Skip ','
            return obj, index + 1  # Skip '}'

        def parse_array(index):
            array = []
            index += 1  # Skip '['
            while index < len(json_str) and json_str[index] != ']':
                value, index = parse_value(index)
                array.append(value)
                if index < len(json_str) and json_str[index] == ',':
                    index += 1  # Skip ','
            return array, index + 1  # Skip ']'

        def parse_string(index):
            end_index = index + 1
            while end_index < len(json_str):
                if json_str[end_index] == '"':
                    break
                end_index += 1
            return json_str[index + 1:end_index], end_index + 1

        def parse_primitive(index):
            end_index = index
            while end_index < len(json_str) and json_str[end_index] not in ',]}':
                end_index += 1
            value_str = json_str[index:end_index].strip()
            if value_str.isdigit() or (value_str.startswith('-') and value_str[1:].isdigit()):
                return int(value_str), end_index
            try:
                return float(value_str), end_index
            except ValueError:
                pass
            if value_str.lower() == 'true':
                return True, end_index
            elif value_str.lower() == 'false':
                return False, end_index
            elif value_str.lower() == 'null':
                return None, end_index
            else:
                return value_str.strip('"'), end_index

        results = []
        index = 0
        while index < len(json_str):
            if json_str[index] in '{[':  # Start of an object or array
                result, new_index = parse_value(index)
                results.append(result)
                index = new_index
            else:
                index += 1
        return results
    
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
    
    def getAPI(self, url: str) -> str:
        
        if not url:
            raise Exception("No URL given!")
        
        try:
            with urllib.request.urlopen(url) as response:
                raw_data = response.read().decode('utf-8')
                self.JSON_Validator(json_string=raw_data)
                return raw_data
        except urllib.error.HTTPError as e:
            raise Exception(f"HTTP error: code: {e.code} reason: {e.reason}")
        except urllib.error.URLError as e:
            raise Exception(f"URL error: reason: {e.reason}")
    
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

    def toString(self, dic = None) -> str:
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
        elif self.json_data:
            self.head(number=len(self.json_data)-1)
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
        
    def JSON_Validator(self, path=None, json_string=None):
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
            json_file = self.toString(dic=self.json_data)

        if json_file.count('[') != json_file.count(']'):
            raise Exception("The number of '[' does not equal with the number of ']'!")

        if json_file.count('{') != json_file.count('}'):
            raise Exception("The number of '{' does not equal with the number of '}'!")

        if json_file.count('"') % 2 != 0:
            raise Exception("Not valid JSON format!")
        return True
