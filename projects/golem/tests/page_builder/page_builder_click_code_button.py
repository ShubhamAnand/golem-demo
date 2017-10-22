
description = 'Verify that the user can see the code of a page by clicking Code button'

pages = ['login',
         'index',
         'project',
         'page_builder',
         'page_builder_code']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    project.create_access_page('test_view_code_' + random('ddd'))
    click(page_builder.code_button)
    verify_exists(page_builder_code.preview_button)


def teardown(data):
    close()

