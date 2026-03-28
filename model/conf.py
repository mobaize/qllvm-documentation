# -*- coding: utf-8 -*-
#
# Sphinx文档构建器的配置文件。
#
# 本文件只包含最常用的配置选项。完整列表请参阅文档：
# http://www.sphinx-doc.org/en/master/config

# -- 路径设置 --------------------------------------------------------------

# 如果扩展（或使用autodoc记录的模块）位于其他目录，
# 请在此处将这些目录添加到sys.path。如果目录相对于文档根目录，
# 请使用os.path.abspath将其设为绝对路径，如下所示。
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- 项目信息 -----------------------------------------------------

# 项目名称
project = 'QLLVM'
# 版权信息
copyright = '2026, Yuqiong Jin,Yu Zhu'
# 作者信息
author = 'Yuqiong Jin,Yu Zhu'

# 简短的X.Y版本号
version = ''
# 完整版本号，包括alpha/beta/rc标签
release = 'v1'


# -- 一般配置 ---------------------------------------------------

# 如果您的文档需要最低版本的Sphinx，请在此处声明。
#
# needs_sphinx = '1.0'

# 在此处添加Sphinx扩展模块名称，作为字符串。它们可以是
# Sphinx自带的扩展（命名为'sphinx.ext.*'）或您的自定义扩展。
extensions = [
    'sphinx.ext.autodoc',      # 自动生成API文档
    'sphinx.ext.doctest',      # 执行文档中的测试
    'sphinx.ext.intersphinx',  # 交叉引用其他文档
    'sphinx.ext.todo',         # 支持todo项
    'sphinx.ext.mathjax',      # 支持数学公式
    'sphinx.ext.ifconfig',     # 条件内容
    'sphinx.ext.viewcode',     # 显示源代码
    'sphinx.ext.githubpages',  # 支持GitHub Pages
]

# 禁用搜索功能
html_theme_options = {
    'style_nav_header_background': '#2980B9',  # 设置导航栏背景色
    'collapse_navigation': False,  # 不折叠导航，显示完整目录
    'sticky_navigation': True,  # 导航栏固定在顶部
    'navigation_depth': 4,  # 导航深度
    'includehidden': True,  # 包含隐藏的目录项
    'titles_only': False,  # 显示完整的标题层次结构
}

# 添加包含模板的路径，相对于此目录。
templates_path = ['_templates']

# 源文件名的后缀。
# 您可以指定多个后缀作为字符串列表：
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'  # 使用reStructuredText格式

# 主toctree文档。
master_doc = 'index'  # 主文档文件

# Sphinx自动生成内容的语言。请参阅文档
# 了解支持的语言列表。
#
# 这也用于通过gettext目录进行内容翻译的情况。
# 通常，您会从命令行设置"language"。
# language = 'zh_CN'  # 使用中文

# 多语言支持配置
# 参考: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

# 语言设置
language = 'zh_CN'  # 默认使用中文

# 多语言文档的构建配置
# 使用Sphinx的内置多语言支持
# 参考: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-locales

# 支持的语言
locales = [
    ('en', 'English'),
    ('zh_CN', '中文'),
]

# 默认语言
default_language = 'en'

# 相对于源目录的模式列表，用于匹配在查找源文件时要忽略的文件和目录。
# 此模式也会影响html_static_path和html_extra_path。
exclude_patterns = []

# 要使用的Pygments（语法高亮）样式。
pygments_style = None


# -- HTML输出选项 -------------------------------------------------

# 用于HTML和HTML帮助页面的主题。请参阅文档
# 了解内置主题列表。
#
#html_theme = 'alabaster'
#html_theme = 'classic'  # 使用经典主题
html_theme = 'sphinx_rtd_theme'  # 使用Read the Docs主题，更美观现代




# 在此处添加包含自定义静态文件（如样式表）的路径，
# 相对于此目录。它们会在内置静态文件之后复制，
# 因此名为"default.css"的文件将覆盖内置的"default.css"。
html_static_path = ['_static']

# 自定义JavaScript文件和CSS文件
# def setup(app):
#     app.add_js_file('search_autocomplete.js')
#     app.add_css_file('custom.css')

# 自定义侧边栏模板，必须是将文档名称映射到模板名称的字典。
#
# 默认侧边栏（对于与任何模式都不匹配的文档）由
# 主题本身定义。内置主题默认使用这些模板：
# ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``。
#
# 恢复源码链接功能
# html_sidebars = {
#     '**': ['localtoc.html', 'relations.html', 'searchbox.html']
# }


# -- HTMLHelp输出选项 ---------------------------------------------

# HTML帮助构建器的输出文件基名。
htmlhelp_basename = 'QLLVMdoc'


# -- LaTeX输出选项 ------------------------------------------------

latex_elements = {
    # 纸张大小（'letterpaper'或'a4paper'）。
    #
    # 'papersize': 'letterpaper',

    # 字体大小（'10pt'，'11pt'或'12pt'）。
    #
    # 'pointsize': '10pt',

    # LaTeX前言的附加内容。
    #
    # 'preamble': '',

    # LaTeX图形（浮动）对齐
    #
    # 'figure_align': 'htbp',
}

# 将文档树分组到LaTeX文件中。元组列表
# （源起始文件，目标名称，标题，
#  作者，文档类[howto，manual或自己的类]）。
latex_documents = [
    (master_doc, 'QLLVM.tex', 'QLLVM Documentation',
     'Yuqiong Jin,Yu Zhu', 'manual'),
]


# -- 手册页输出选项 ------------------------------------------

# 每个手册页一个条目。元组列表
# （源起始文件，名称，描述，作者，手册部分）。
man_pages = [
    (master_doc, 'qllvm', 'QLLVM Documentation',
     [author], 1)
]


# -- Texinfo输出选项 ----------------------------------------------

# 将文档树分组到Texinfo文件中。元组列表
# （源起始文件，目标名称，标题，作者，
#  目录菜单条目，描述，类别）
texinfo_documents = [
    (master_doc, 'QLLVM', 'QLLVM Documentation',
     author, 'QLLVM', 'One line description of project.',
     'Miscellaneous'),
]


# -- Epub输出选项 -------------------------------------------------

# 书目Dublin Core信息。
epub_title = project

# 文本的唯一标识符。这可以是ISBN号
# 或项目主页。
#
# epub_identifier = ''

# 文本的唯一标识。
#
# epub_uid = ''

# 不应打包到epub文件中的文件列表。
epub_exclude_files = ['search.html']


# -- 扩展配置 -------------------------------------------------

# -- intersphinx扩展选项 ---------------------------------------

# intersphinx的示例配置：引用Python标准库。
# 暂时注释掉，避免配置错误
# intersphinx_mapping = {'https://docs.python.org/3/': ('https://docs.python.org/3/objects.inv', None)}

# -- todo扩展选项 ----------------------------------------------

# 如果为true，`todo`和`todoList`会产生输出，否则不会产生任何输出。
todo_include_todos = True
