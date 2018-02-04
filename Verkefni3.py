from bottle import route, run, template, static_file

frettir = [

    {
        'fyrirsogn': 'Frett 1',
        'texti': 'Þetta gerðist einu sinni!!',
        'mynd': 'mynd1.jpg',
        'email': 'aoe@gmail.com'

    },

    {
        'fyrirsogn': 'Frett 2',
        'texti': 'Las Vegas Skotárásin gerðist hér!!',
        'mynd': 'mynd2.jpg',
        'email': 'aoe@gmail.com'

    },

    {
        'fyrirsogn': 'Frett 3',
        'texti': 'Cloud 9 vinna úrslitariðil eSports!!',
        'mynd': 'mynd3.jpeg',
        'email': 'aoe@gmail.com'

    },

    {
        'fyrirsogn': 'Frett 4',
        'texti': 'Pepsi Max er með alvöru bragð en engan sykur!!',
        'mynd': 'mynd4.png',
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
