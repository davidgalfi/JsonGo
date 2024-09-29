from jsoncompiler import JsonGo

testcase = JsonGo(path="jsongo\json2.json")
string = """{
    "value1" : 123
}
"""
testcase.add(string)
print(testcase.head())
testcase.convertToJson()

