import mechanize

nav = mechanize.Browser()
nav.set_handle_robots(False)
nav.set_handle_equiv(False)
nav.addheaders = [('User-Agent','Firefox')]
nav.open("https://juice-shop.herokuapp.com/#/login")
nav.select_form(nr=0)

nav['username'] = 'admin'
nav['password'] = 'password'
nav.submit()
print(nav.response().read())
