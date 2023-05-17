def temperature_conversion(celcius):
     """
     Converts temperature in celcius to fahrenheit
     """
     return celcius + 273.15

def mean_temperature(data):
     """
     Get mean temperature

     Args:
           data (pandas.DataFrame): data with air temperature measurements.

     Returns:
           float: mean temperature

     """
     temperatures=data['Air temperature (degC)']
     return sum(temperatures)/len(temperatures)