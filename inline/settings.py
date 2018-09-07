TEMPLATE_DIRS = 'templates'


RULES = (
    {
        'test': '*.css',
        'processors': (
            {
                'processor': 'gena.processors.BundleProcessor',
                'options': {
                    'name': 'css',  # `context.bundles.css` in the template
                },
            },
        ),
        'priority': 10,  # default: 100
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
