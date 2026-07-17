# JavaScript

## Data Types:
- string ('' or "")
    - **Ex:** 'John', '1', 'Hello, Welcome to the world!', "Hello" + "  + "World!", 'Josh' + ' ' + 'Joe'
- number (integers(positive, negative), float(decimal numbers))
    - **Ex:** 1,2,-3, 9, 6, 2
    - **Ex:** 9.2, 5.9, 6.1
- bigint (ends with 'n')
    - **Ex:** 90071992547423453436n
- boolean (true, false)
- object ({}, function, class)
    - **Ex:** {"name": "Josh", "age": 32, ....}
    - new ClassName()
    - function_name
- undefined
- null

**Keywords:** (help to create variables)
- var (legacy keyword)(not recommanded for modern projects)
    - var name = "Josh";
    - var age = 32;
- let (variable mutable, modifiable)
    - let name = "Josh"; // assign
    - name = "Joe"; // reassign
    - let age;
    - age = 32;
- const (variable immutable, constant)
    - const age = 32; // immutable, constant
    - age = 30; // error not reassign
    - const name; // must initialize
    - name = "Josh"; // error