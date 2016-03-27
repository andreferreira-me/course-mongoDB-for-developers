import bottle

@bottle.route('/')
def home_page():
    mythings = ['apple', 'orange', 'banana', 'peach']
    return bottle.template('hello_world', username="Andre", things=mythings)
#   return bottle.template('hello_world', {'username':"Andre", 'things':mythings})
    return "<html><head></head><body><p>Hello World\n</p></body></html>"


@bottle.route('/testpage')
def test_page():
    return "this is a test page"

bottle.debug(True)
bottle.run(host='localhost', port=8080)
