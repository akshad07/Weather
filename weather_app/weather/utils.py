import requests

def fetch_weather_data(url):
    response = requests.get(url)
    data = response.text
    lines = data.split('\n')
    weather_data_list = []

    for line in lines[6:]:
        if line.strip():
            parts = line.strip().split()
            if len(parts) >= 17:  # Ensure the line has at least 17 elements
                year = parts[0]  # Assuming the first part is the year
                monthly_data = parts[1:18]  # Assuming the next 17 parts are monthly data
                weather_data = {
                    'year': year,
                    'jan': monthly_data[0],
                    'feb': monthly_data[1],
                    'mar': monthly_data[2],
                    'apr': monthly_data[3],
                    'may': monthly_data[4],
                    'jun': monthly_data[5],
                    'jul': monthly_data[6],
                    'aug': monthly_data[7],
                    'sep': monthly_data[8],
                    'oct': monthly_data[9],
                    'nov': monthly_data[10],
                    'dec': monthly_data[11],
                    'win': monthly_data[12],
                    'spr': monthly_data[13],
                    'sum': monthly_data[14],
                    'aut': monthly_data[15],
                    'ann': monthly_data[16],
                }
                weather_data_list.append(weather_data)

    return weather_data_list
