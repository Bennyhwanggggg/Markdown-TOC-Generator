from toc_generator import get_content
from . import PATH


def test_generate_toc():
    expected = ['- [Table of Content](Example_TOC.md#table-of-content)\n', '- [Top Level](Top_Level.md#top-level)\n',
                '\t* [Heading1](Top_Level.md#heading1)\n', '\t* [Heading2](Top_Level.md#heading2)\n',
                '\t\t+ [Subheading 2](Top_Level.md#subheading-2)\n',
                '\t\t\t- [SubSubHeading 3](Top_Level.md#subsubheading-3)\n',
                '\t* [Heading 3](Top_Level.md#heading-3)\n', '- [Top Level 2](Top_Level_2.md#top-level-2)\n',
                '\t* [Top Level 2 Heading 1](Top_Level_2.md#top-level-2-heading-1)\n',
                '- [Inner Level](Inner_Level.md#inner-level)\n',
                '\t* [Inner Heading 1](Inner_Level.md#inner-heading-1)\n',
                '\t\t+ [Sub Inner Heading 1](Inner_Level.md#sub-inner-heading-1)\n',
                '\t\t+ [Sub Inner Heading 2](Inner_Level.md#sub-inner-heading-2)\n',
                '\t\t\t- [Sub SUb Inner Heading1](Inner_Level.md#sub-sub-inner-heading1)\n',
                '\t* [Inner Heading 2](Inner_Level.md#inner-heading-2)\n',
                '- [Inner Level 2](Inner_Level_2.md#inner-level-2)\n',
                '\t* [Inner Level 2 Heading](Inner_Level_2.md#inner-level-2-heading)\n',
                '- [Inner Inner Level](Inner_Inner_Level.md#inner-inner-level)\n',
                '\t+ [Sub Sub Heading](Inner_Inner_Level.md#sub-sub-heading)\n']

    assert get_content(PATH) == expected
