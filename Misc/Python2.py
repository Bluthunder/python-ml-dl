
def listComp(sym):
    beyond_ascii = [ord(s) for s in sym if ord(s) > 127]
    return beyond_ascii



if "__name__" == "main":

    print(listComp('$&A*^%'))
