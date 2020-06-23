# Files in Python

We open files, to make them available to the program.

```
handle = open(filename,mode)
```

r -> read
w -> write

A text file has '\n' at the end of each line.

To read the whole file, use:
```
xfile = open('text.txt')
input = xfile.read()
print(input)
```
The 'input' var has the entire file stored.

print() -> adds a newline after printing.

 ### range()
 The range() returns a list.

 ```
 range(n)
 ```

 Will generate a list with 'n' numbers, upto, but not including 'n'

 # RE

* ^ -> Startswith
* . -> any character
* '*' -> zero or more characters
* /s -> Non white space character
* '+' -> One or more

```
re.search()
re.findall()
```

## Greedy Matching
Regular expression tries to give the largest possible string that is matching.

* ? -> Will gie the smallest possible string that is matching

<a hre="https://www.coursera.org/learn/python-network-data/supplement/2WnqH/python-regular-expression-quick-guide">Regex Cheatsheat</a>

# Unicode characters and strings
To print the UNICODE value of character - 
```
print(ord('H'))
```
**UTF-8** is the recommeded mode of encoding
- It is the best practice to move data betwenn computers

When we alk to an external source like a network socket, we send bytes, so we need to encode Python 3 strings into a given character encoding.

When we read data from an external source, we must decode it based on the character set it uses, so it is properly represented in python3 as a string. While python uses UTF-8 encoding, other sources of data may use any type of encoding - ASCII, UTF-8, UTF-16, UTF-32 etc.

# WEB SCRAPING
- Program pretends to be a browser and extracts information
- Spidering or crawling the web

### Beautiful soup

## XML (eXtendsible Markup Language)

- Share structured data

It has the following components:
- Start tag
- End tag
- Text content
- **Attributes**
- Self Closing tag

### XML Schema
It is the legal formal of an XML Document

## JSON (JavaScript Object Notation)
