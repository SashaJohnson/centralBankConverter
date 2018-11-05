
def convertMoney(convert_from, convert_to, as_of_date, amount):
    
    import requests
    from bs4 import BeautifulSoup

    base_url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
    
    resp = requests.get(base_url + as_of_date)
    soup = BeautifulSoup(resp.content, 'xml')
    
    raw_value_from = soup.find('CharCode', text=convert_from).find_next_sibling('Value').string
    raw_value_to = soup.find('CharCode', text=convert_to).find_next_sibling('Value').string

    value_from = float(raw_value_from.replace(',', '.'))
    value_to = float(raw_value_to.replace(',', '.'))

    

    return value_from * amount / value_to



