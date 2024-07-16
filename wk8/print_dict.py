#!/usr/bin/env python3

def print_dict(d):
    """
    Displays the contents of d in the following format:

         key: value
      Andrew: green
        Anne: red
        John: blue
           a: ligned
    """
    for item in d.items():
        print(f"{item[0]:>10}: {item[1]}")

if __name__ == "__main__":
    print_dict({
        "key": "value",
        "a": "ligned",
    })
