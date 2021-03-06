# Markdown-TOC-Generator
Markdown Table of Content Generator that generator based on all markdown files from the root folder.

## How to use?
There's no external dependencies! Just clone this repository and run
```
python3 toc_generator.py
```

To get more info on the different options such as save path and target path.

```
python3 toc_generator.py --help
```

## Testing
Install test dependencies
```
python3 -m pip install test_requirements.txt
``` 

Running the tests
```
pytest
```

## Example
```
python3 toc_generator.py -p './tests' -s './tests/Example_TOC.md'
```
Output:
See [Example_TOC.md](/tests/Example_TOC.md)
```
# Table of Content


- [Top Level](Top_Level.md#top-level)

	* [Heading1](Top_Level.md#heading1)

	* [Heading2](Top_Level.md#heading2)

		+ [Subheading 2](Top_Level.md#subheading-2)

			- [SubSubHeading 3](Top_Level.md#subsubheading-3)

	* [Heading 3](Top_Level.md#heading-3)

- [Top Level 2](Top_Level_2.md#top-level-2)

	* [Top Level 2 Heading 1](Top_Level_2.md#top-level-2-heading-1)

- [Inner Level](Inner_Level.md#inner-level)

	* [Inner Heading 1](Inner_Level.md#inner-heading-1)

		+ [Sub Inner Heading 1](Inner_Level.md#sub-inner-heading-1)

		+ [Sub Inner Heading 2](Inner_Level.md#sub-inner-heading-2)

			- [Sub SUb Inner Heading1](Inner_Level.md#sub-sub-inner-heading1)

	* [Inner Heading 2](Inner_Level.md#inner-heading-2)

- [Inner Level 2](Inner_Level_2.md#inner-level-2)

	* [Inner Level 2 Heading](Inner_Level_2.md#inner-level-2-heading)

- [Inner Inner Level](Inner_Inner_Level.md#inner-inner-level)

	+ [Sub Sub Heading](Inner_Inner_Level.md#sub-sub-heading)


```