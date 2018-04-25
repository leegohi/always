# -*- coding=utf-8 -*-

def extract_path(json_item,stack,find_str=None):
    if type(json_item)==dict:
        temp_len=len(stack)
        for k,v in json_item.items():
            stack.append(k)
            extract_path(v,stack,find_str)
            del stack[temp_len:]
    elif type(json_item)==list:
        for it in json_item:
            temp_len=len(stack)
            extract_path(it,stack,find_str)
            del stack[temp_len:]
    else:
        if find_str and find_str==json_item:
            print ".".join(stack)
        stack.pop()
def find_path_in_json(json_item,find_str):
    stack=[]
    extract_path(json_item,stack,find_str)
if __name__ =="__main__":
    json_data={
        "a":"x",
        "b":"y",
        "c":[
            {
                "d":"z",
                "e":"m",
                "f":"n",
            }
        ]
    }
    find_path_in_json(json_data,u"n")