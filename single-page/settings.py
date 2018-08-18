# The directory for output files.
DST_DIR = 'dist'


# The directory with templates.
TEMPLATE_DIRS = 'templates'


PROCESSING_RULES = (
    # The rules for all .css files.
    {
        # The pattern to pick our files up.
        'test': '*.css',  # index.css

        # The chain of the processors. Each processor will do its own work with our files.
        # In this case, there's only one processor in the chain.
        'processors': (
            # The processor copies the file (src/index.css -> dist/index.css).
            {'processor': 'gena.processors.SavingProcessor'},
        ),
    },

    # The rules for all .md files.
    {
        'test': '*.md',  # index.md
        'processors': (
            # The processor opens the file (src/index.md), reads its contents, and converts Markdown syntax into HTML.
            {'processor': 'gena.processors.MarkdownProcessor'},

            # The processor renders the template (templates/index.html).
            {
                'processor': 'gena.processors.TemplateProcessor',
                'options': {
                    'template': 'index.html',
                },
            },

            # The processor renames the file (src/index.md -> src/index.html).
            {
                'processor': 'gena.processors.FileNameProcessor',
                'options': {
                    'name': 'index.html',
                },
            },

            # The processor saves the file (src/index.html -> dist/index.html).
            {'processor': 'gena.processors.SavingProcessor'},
        ),
    },
)
