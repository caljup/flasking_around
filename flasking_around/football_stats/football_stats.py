from flask import (Blueprint, request, render_template)

import requests
from bs4 import BeautifulSoup
import pandas as pd

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


football_stats_bp = Blueprint('football_stats_bp', __name__)

base_url = 'https://www.espn.com/nfl/team/schedule/_/name/cin/season/2021'

def scrape_espn(base_url):
    html = fetch_espn_results(base_url)
    results = parse_espn_results(html)
    return results

def fetch_espn_results(base_url):
    assert isinstance(base_url, str)
    response = requests.get(base_url, headers=USER_AGENT)
    response.raise_for_status()

    return response.text

def parse_espn_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    espn_table_name = soup.find('h1', class_='headline').text
    espn_table_columns = soup.find('colgroup').contents
    espn_table_body = soup.find('tbody')
    espn_table_rows = espn_table_body.find_all('tr')

    data_set = [[espn_table_name]]

    for row in espn_table_rows:
        espn_data_values = row.find_all('td')

        data_row = [data.get_text(separator=' ') for data in espn_data_values]

        data_set.append(data_row)
    
    pandas_column_names = [ 'Col_' + str(i) for i in range(1, len(espn_table_columns) + 1) ]

    df = pd.DataFrame(data_set, columns=pandas_column_names)

    df.fillna('', inplace=True)

    return df
    


@football_stats_bp.route('/football-stats', methods=('GET', 'POST'))
def football_statistics():
    if request.method == 'POST':
        schedule_table = scrape_espn(base_url)

        schedule = schedule_table.to_html(header=False, index=False, classes='center')

        recieved = True

        return render_template('football_statistics.html', schedule=schedule, recieved=recieved )

    return render_template('football_statistics.html')

