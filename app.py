import requests
import csv23
from datetime import datetime

URL="https://dnpedia.com/tlds/ajax.php"

HEADER = {
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Host": "dnpedia.com",
    "Referer": "https://dnpedia.com/tlds/topm.php",
    "X-Requested-With": "XMLHttpRequest"
}

csv_file = "tld_list_{}.csv".format(datetime.today().strftime('%Y-%m-%d'))

print(csv_file)
with csv23.open_writer(csv_file, encoding='utf-8') as writer:
    writer.writerow(["id","domain","rank","tld","site"])
    for page in range(1,21):
        PARAM = {
            "cmd":"alexa",
            "columns":"id,domain,rank,tld,site",
            "_search":"false",
            "nd":1590286803117,
            "rows":1000,
            "page":page,
            "sidx":"active_in_zone",
            "sord":"asc"
        }
        response = requests.get(URL, params= PARAM, headers=HEADER)
        data = response.json()['rows']
        print("Writing page {:d} to csv".format(page))
        for line in data:
            writer.writerow(line.values())

