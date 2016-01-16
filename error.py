import sys

def failfast(response):
    try:
        print("Error code: " + str(response.status_code) + " - " + response.json()["error"])
        print(response.json()["message"])
    except:
        print("Unexpected error while failing fast because of invalid request. " + sys.exc_info()[0])
    sys.exit(-1)

