volume_name = '{{cookiecutter.volume_name}}'
filename = '{{cookiecutter.filename}}'

app_bundle = '{{cookiecutter.app_bundle_name}}'

files = [
    f'../{app_bundle}',
]
symlinks = {
    'Applications': '/Applications',
}

default_view = 'icon-view'
background = 'builtin-arrow'

text_size = 14
icon_size = 96

icon_locations = {
    'Applications': (500, 120),
    app_bundle: (140, 120),
}
