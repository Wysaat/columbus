inet_addr = "192.168.233.128"
path = '/home/user/webpages' 
homepage = 'app.html'

# mapping urls to relative pathes
mapping = {}

mapping['/googlehk'] = '/google_hk.htm'

mapping['/form/success'] = '/form_success.html'

# some urls needn't be mapped, for example,
# the following mappings can be ommited:
# mapping['/'] = 'app.html' (when app.html is homepage)
# mapping['/doc'] = '/doc.html'
# mapping['/doc'] = '/doc.htm'
# mapping['/about/us'] = '/about/us'
# mapping['/about/licence'] = '/about/licence.html'

# mapping the urls used in forms to suggest database used
# to the redirected urls
redirect = {}

redirect['/form/old/create/0'] = '/form/success'
redirect['/form/young/create/0'] = '/form/success'

# database configuration
db_type = 'mysql'
db_passwd = ''
db_name = 'expdb'
user_name = 'user'

# configuration for ssl
ssl_port = 443
ssl_certfile = '/home/user/webpages/cert.pem'
ssl_keyfile = '/home/user/webpages/cert.pem'