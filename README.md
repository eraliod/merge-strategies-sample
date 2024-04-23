# Color Text Box CLI

This is a simple CLI application that prints text in a colored box.

## Installation

To install the required dependencies, run:
```
pip install -r requirements.txt
```

## Usage

To use the application, navigate to the root folder and call the module with:
```
python -m src "sample text"
```

## Sample Output

Here is a sample of the output you would get by running the command:

```
+------------+
| sample text |
+------------+
```

The default color of the text is yellow, but you can specify the color using the `--color` option.

## Supported Colors

- white
- yellow
- red

For example, to print the text in red, use:
```
python -m src "sample text" --color red
```
