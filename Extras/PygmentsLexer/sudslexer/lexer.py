from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class SudsLexer(RegexLexer):
    name = 'SUDS'
    aliases = ['suds']
    filenames = ['*.sud']

    tokens = {
        'root': [
            (r'===\s*\n', Generic.Heading),
            # Choices
            (r'\s*\*\s+[^\@\n]+[\@\n]', String),
            (r'\s*#.*\n', Comment),
            # Speaker lines
            (r'\s*\S+\:', Name.Class, 'speakerline'),
            # Close bracket for all special lines
            (r'\]', Operator),       
            (r'\b(and|or|&&|\|\||not)\b', Operator),
            # Set commands so we can highlight variable differently
            (r'(\[)\s*(set)(\s+)(\S+)', bygroups(Operator, Keyword, Text, Name.Variable)),
            (r'(\[)\s*(if|else|elseif|endif|event|return|goto|gosub|go to|go sub)\b', bygroups(Operator, Keyword)),
            # Variables
            (r'(\{)([\w\.]+)(\})', bygroups(Operator, Name.Variable, Operator)),
            (r'(\|)(plural|gender)(\()(.*?)(\))', bygroups(Operator, Keyword, Operator, Keyword, Operator)),
            (r'\b([tT]rue|[fF]alse|[mM]asculine|[fF]eminine|[nN]euter)\b', Name.Constant),
            (r'\+\/\-\*\!', Operator),
            (r'\"[^\"]*\"', String.Single),
            (r'\`[^\`]*\`', String.Escape),
            (r'\d+(\.\d+)?', Number),
            # Line IDs
            (r'\@[0-9a-fA-F]+\@', Comment.Special),
            # Embedded markup
            (r'\<\w+\>', Name.Decorator),
            (r'\<\/\>', Name.Decorator),
            # Goto labels
            (r'\s*:\S+\n', Name.Label),
            # Fallback for all other text
            # Needs an optional \n on the end to finish lines correctly
            (r'\s+[\n]?', Text),
            (r'\S+?[\n]?', Text), # non-greedy so we don't consume all non-whitespace


        ],
        # While in a speaker line, we ignore everything else except variables & markup
        'speakerline' : [
            # Variables
            (r'(\{)([\w\.]+)(\})', bygroups(Operator, Name.Variable, Operator)),
            (r'(\|)(plural|gender)(\()(.*?)(\))', bygroups(Operator, Keyword, Operator, Keyword, Operator)),
            (r'[\@\n]', Text, '#pop'),
            # Embedded markup
            (r'\<\w+\>', Name.Decorator),
            (r'\<\/\>', Name.Decorator),
            (r'[^\@\n\<\{]+', Text),

        ]
    }