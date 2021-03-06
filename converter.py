def convertMoney(convert_from, convert_to, as_of_date, amount):

    '''The user has to provide the following arguments:

           -currency code to convert from (str),
           -currency code to convert to (str),
           -date (dd/mm/yyyy)
           -amount(int)

       The function makes a call to the public API of the Russian Central Bank and returns a converted value rounded to 2

       Example: convertMoney('USD', 'EUR', '05/11/2018', 150) => 131.18

       '''
    
    import requests
    import sqlite3
    from bs4 import BeautifulSoup

    base_url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
    
    resp = requests.get(base_url + as_of_date)
    soup = BeautifulSoup(resp.content, 'xml')
    
    raw_value_from = soup.find('CharCode', text=convert_from).find_next_sibling('Value').string
    raw_value_to = soup.find('CharCode', text=convert_to).find_next_sibling('Value').string

    value_from = float(raw_value_from.replace(',', '.'))
    value_to = float(raw_value_to.replace(',', '.'))

    answer_preliminary = value_from * amount / value_to
    answer = round(answer_preliminary, 2)

    ###### saving to sqlite3 DB

    conn = sqlite3.connect('request_history.db')
    c = conn.cursor()
    #c.execute("CREATE TABLE rates (source text, target text, date text, amount integer, total real)")
    c.execute("INSERT INTO request_history VALUES(?,?,?,?,?)",(convert_from, convert_to, as_of_date, amount, answer))
    conn.commit()
    conn.close()
    
    ######
    
    return answer


