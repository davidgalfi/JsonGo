from jsongo import JsonGo

testcase = JsonGo()

path = "https://dummyapi.online/api/todos"
json_string = testcase.getAPI(path)


json_data = testcase.convertToDic(json_string=json_string)
print(json_data.head())