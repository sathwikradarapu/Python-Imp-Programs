def convert_to_string_list(string):
    string=string.split(",")
    return string
def convert_to_dictionary(string_list):
    dictionary=dict()
    for i in string_list:
        j=i.split(":")
        color,weight=j[0],j[1]
        if color in dictionary:
            dictionary[color]=dictionary[color]+int(weight)
        else:
            dictionary[color]=int(weight)
    return dictionary
string=input()
string_list=convert_to_string_list(string)
final_dictionary=convert_to_dictionary(string_list)
print(final_dictionary)