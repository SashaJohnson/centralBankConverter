
def convertMoney(convert_to, as_of_date, amount):
    
    import requests
    from bs4 import BeautifulSoup

    base_url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='

    resp = requests.get(base_url + as_of_date)
    soup = BeautifulSoup(resp.content, 'xml')

    raw_value = soup.find('CharCode', text=convert_to).find_next_sibling('Value').string
    value = float(raw_value.replace(',', '.'))

    return value * amount



