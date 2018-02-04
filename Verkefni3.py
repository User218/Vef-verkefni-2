from bottle import route, run, template, static_file

frettir = [

    {
        'fyrirsogn': 'Frett 1',
        'texti': 'Meginmal Frettar 1',
        'mynd': 'mynd1.jpg',
        'email': 'aoe@gmail.com'

    },

    {
        'fyrirsogn': 'Frett 2',
        'texti': 'Meginmal Frettar 2',
        'mynd': 'frett2.jpg',
        'email': 'aoe@gmail.com'

    },

    {
        'fyrirsogn': 'Frett 3',
        'texti': 'Meginmal Frettar 3',
        'mynd': 'frett3.jpg',
        'email': 'aoe@gmail.com'

    },

    {
        'fyrirsogn': 'Frett 4',
        'texti': 'Meginmal Frettar 4',
        'mynd': 'frett4.jpg',
        'email': 'aoe@gmail.com'

    }
]

@route('/')
def index():
    return template("verk3")

@route("/a")
def lidurA():
    return template("lidurA")

@route('/kt/<kennitala>')
def kt(kennitala):
    return template('kt', kennitala=kennitala)

@route('/b')
def lidurB():
    return template('index', frettir=frettir)

@route('/frettir/<n>')
def frett(n):
    return template('frett', n=n, frettir=frettir)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./myfiles")

run()