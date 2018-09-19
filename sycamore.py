# -*- coding: utf-8 -*-
"""
sycamore
---------------------
Port of the Tomorrow colour scheme https://github.com/chriskempson/tomorrow-theme
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


BACKGROUND = "#282828"
CURRENT_LINE = "#525252"
SELECTION = CURRENT_LINE
FOREGROUND = "#ebebeb"
COMMENT = "#7a7a7a"
RED = "#e57373"
ORANGE = "#ffa726"
# YELLOW = "#eab700"
GREEN = "#b2ff59"
GREEN_DARK = "#388e3c"
AQUA = "#80deea"
BLUE = "#1976d2"
PURPLE = "#9575cd"


class SycamoreStyle(Style):

    """
    Port of the Tomorrow colour scheme https://github.com/chriskempson/tomorrow-theme
    """

    default_style = ''

    background_color = BACKGROUND
    highlight_color = SELECTION

    styles = {
        # No corresponding class for the following:
        Text:                      FOREGROUND,  # class:  ''
        Whitespace:                "",          # class: 'w'
        Error:                     RED,         # class: 'err'
        Other:                     "",          # class 'x'

        Comment:                   COMMENT,   # class: 'c'
        Comment.Multiline:         "",        # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'

        Keyword:                   BLUE,    # class: 'k'
        Keyword.Constant:          "",        # class: 'kc'
        Keyword.Declaration:       "",        # class: 'kd'
        Keyword.Namespace:         "",      # class: 'kn'
        Keyword.Pseudo:            "",        # class: 'kp'
        Keyword.Reserved:          "",        # class: 'kr'
        Keyword.Type:              "",    # class: 'kt'

        Operator:                  FOREGROUND,      # class: 'o'
        Operator.Word:             "",        # class: 'ow' - like keywords

        Punctuation:               FOREGROUND,  # class: 'p'

        Name:                      PURPLE,  # class: 'n'
        Name.Attribute:            GREEN,        # class: 'na' - to be revised
        Name.Builtin:              AQUA,          # class: 'nb'
        Name.Builtin.Pseudo:       "",          # class: 'bp'
        Name.Class:                FOREGROUND,      # class: 'nc' - to be revised
        Name.Constant:             "",         # class: 'no' - to be revised
        Name.Decorator:            "",        # class: 'nd' - to be revised
        Name.Entity:               "",          # class: 'ni'
        Name.Exception:            RED,         # class: 'ne'
        Name.Function:             RED,        # class: 'nf'
        Name.Property:             "",          # class: 'py'
        Name.Label:                "",          # class: 'nl'
        Name.Namespace:            FOREGROUND,      # class: 'nn' - to be revised
        Name.Other:                "",        # class: 'nx'
        Name.Tag:                  RED,        # class: 'nt' - like a keyword
        Name.Variable:             GREEN,         # class: 'nv' - to be revised
        Name.Variable.Class:       "",          # class: 'vc' - to be revised
        Name.Variable.Global:      "",          # class: 'vg' - to be revised
        Name.Variable.Instance:    "",          # class: 'vi' - to be revised

        Number:                    GREEN_DARK,    # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'

        Literal:                   ORANGE,    # class: 'l'
        Literal.Date:              GREEN,     # class: 'ld'

        String:                    ORANGE,       # class: 's'
        String.Backtick:           "",          # class: 'sb'
        String.Char:               FOREGROUND,  # class: 'sc'
        String.Delimiter:           FOREGROUND,  # class: ?
        String.Doc:                COMMENT,     # class: 'sd' - like a comment
        String.Double:             "",          # class: 's2'
        String.Escape:             "",      # class: 'se'
        String.Heredoc:            "",          # class: 'sh'
        String.Interpol:           "",      # class: 'si'
        String.Other:              "",          # class: 'sx'
        String.Regex:              "",          # class: 'sr'
        String.Single:             "",          # class: 's1'
        String.Symbol:             "",          # class: 'ss'

        Generic:                   "",                    # class: 'g'
        Generic.Deleted:           RED,                   # class: 'gd',
        Generic.Emph:              "italic",              # class: 'ge'
        Generic.Error:             "",                    # class: 'gr'
        Generic.Heading:           "bold " + FOREGROUND,  # class: 'gh'
        Generic.Inserted:          GREEN,                 # class: 'gi'
        Generic.Output:            "",                    # class: 'go'
        Generic.Prompt:            "bold " + COMMENT,     # class: 'gp'
        Generic.Strong:            "bold",                # class: 'gs'
        Generic.Subheading:        "bold " + AQUA,        # class: 'gu'
        Generic.Traceback:         "",                    # class: 'gt'
    }
