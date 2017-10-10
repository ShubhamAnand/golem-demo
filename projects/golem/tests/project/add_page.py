
description = 'Verify that the user can create a new page from the project page'

pages = ['login',
         'index',
         'project']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    store('page_name', random('ccccc'))
    project.add_page(data.page_name)
    project.verify_page_exists(data.page_name)


def teardown(data):
    close()
