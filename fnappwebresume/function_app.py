import azure.functions as func
import datetime
import json
import logging

#PYTHON DEV MODEL FOR AZFUNCTIONS
#la version 1  basado en functiones por carpetas
# version2  permite manejar las AZF desde un solo FUNCTION APP, evitando codigo y config files repetidos


# v2 model #


app = func.FunctionApp() # registro central de las functions
#app.function_name = "fnappwebresume" # nombre de la function app, se puede cambiar en el portal de azure
@app.route(route="roleDescriptions",methods=["GET"], auth_level=func.AuthLevel.FUNCTION)# cada function utiliza ste metodo para registrar su url, HTTP methods
#Cuales son las config del app.route?
def getRoleDescriptions(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. https GET")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )

@app.route(route="roleDescriptions", methods=["POST"], auth_level= func.AuthLevel.FUNCTION)
def postRoleDescriptions(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()

        name = req_body.get('name')
        return func.HttpResponse(f"Hello,{name} POST")
    except ValueError:
        raise func.HttpResponse("Invalid input", status_code=400)

