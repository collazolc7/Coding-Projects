#luiscarloscollazo
#mar142024

#declare functions
def fahrenheitToCelsius(tempFahr):
    return (tempFahr - 32) * (5/9)

def celsiusToFahrenheit(tempCels):
    return (tempCels *(9/5)) + 32

def fahrenheitToKelvin(tempFahr):
    return (tempFahr - 32) * (5/9) + 273.15

def kelvinToFahrenheit(tempKelv):
    return (tempKelv - 273.15) * (9/5) + 32

def celsiusToKelvin(tempCels):
    return tempCels + 273.15

def kelvinToCelsius(tempKelv):
    return tempKelv - 273.15

