def anzeige(*args):
    returnwert = ""
    for arg in args:
        try:
            returnwert = returnwert + skal(zahl(arg))
        except:
            returnwert = returnwert + arg


def skal(z):
    kilo = 1000
    mega = kilo * 1000
    giga = mega * 1000
    tera = giga * 1000
    penta = tera * 1000

    if (z > penta):
        return str(round(z / penta, 1), 1) + " P"
    elif (z > tera):
        return str(round(z / tera, 1)) + " T"
    elif (z > giga):
        return str(round(z / giga, 1)) + " G"
    elif (z > mega):
        return str(round(z / mega, 1)) + " M"
    elif (z > kilo):
        return str(round(z / kilo, 1)) + " K"
    else:
        return str(round(z, 1))


def zahl(p):
    try:
        return int(p)
    except:
        try:
            return float(p)
        except:
            try:
                return float(p.replace(',', '.'))
            except:
                raise


def anzeige(*args):
    returnwert = ""
    for arg in args:
        z = ""
        try:
            z = str(zahl(arg))
        except:
            z = arg
        returnwert = returnwert + z
    print(returnwert)
    return returnwert

