TEMPLATE_DIRS = 'templates'


PROCESSING_RULES = (
    {
        'test': '*.css',
        'processors': (
            {
                'processor': 'gena.processors.FileNameProcessor',
                'options': {
                    'name': 'index.css',
                },
            },
            {
                'processor': 'gena.processors.SavingProcessor',
                'options': {
                    'append': True,
                },
            },
        ),
    },

    {
        'test': '*.md',
        'processors': (
            {'processor': 'gena.processors.MarkdownProcessor'},
            {
                'processor': 'gena.processors.TemplateProcessor',
                'options': {
                    'template': 'index.html',
                },
            },
            {
                'processor': 'gena.processors.FileNameProcessor',
                'options': {
                    'name': 'index.html',
                },
            },
            {'processor': 'gena.processors.SavingProcessor'},
        ),
    },
)


INITIAL_JOBS = (
    {'job': 'gena.jobs.clear_dst_dir'},
)
