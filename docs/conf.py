__author__ = 'alain ivars'
# -*- coding: utf-8 -*-
import sys, os

# check to see if this file is getting loaded on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if on_rtd is False:
    import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.join(os.path.abspath('.'), '_ext'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
#   'sphinx.ext.doctest',
#   'sphinx.ext.intersphinx',
#   'sphinx.ext.todo',
#   'sphinx.ext.coverage',
#   'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    # 'djangodjango_base_appdocs',
]

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'django contact_form_bootstrap'
copyright = u'2013-2021, Alain Ivars'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
version = "1.0rc1"
release = "beta"

# The language for content autogenerated by Sphinx. Refer to documentation for
# a list of supported languages.
language = "en"

# List of directories, relative to source directory, that shouldn't be
# searched for source files.
exclude_trees = ['build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description unit
# titles (such as .. function::).
add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['static']
