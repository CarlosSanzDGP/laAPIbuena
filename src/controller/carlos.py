


def generateController(app):

    @app.route("/hola")
    def basicResponse():
        return {
            "hola":"que tal"
        } 