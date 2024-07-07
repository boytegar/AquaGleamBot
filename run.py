import random
import requests
import time
import urllib.parse
import json
import base64
import socket
from datetime import datetime


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
    'content-length': '0',
    'priority': 'u=1, i',
    'Origin': 'https://app.gleam.bot',
    'Referer': 'https://app.gleam.bot/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
}

def load_credentials():
    # Membaca token dari file dan mengembalikan daftar token
    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        # print("Token berhasil dimuat.")
        return queries
    except FileNotFoundError:
        print("File token.txt tidak ditemukan.")
        return [  ]
    except Exception as e:
        print("Terjadi kesalahan saat memuat token:", str(e))
        return [  ]
    
    
def auth(query):
    url = 'https://prod-api.gleam.bot/api/v1/accounts/auth'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def list(token):
    url = 'https://prod-api.gleam.bot/api/v1/projects/list'
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def quest(token, slug):
    url = f'https://prod-api.gleam.bot/api/v1/projects/{slug}/quests'
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def start(token, id, query):
    url = f'https://prod-api.gleam.bot/api/v1/quests/{id}/start'
    headers['Authorization'] = f'Bearer {token}'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print(res.get('message'))
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def check(token, id, query):
    url = f'https://prod-api.gleam.bot/api/v1/quests/{id}/check'
    headers['Authorization'] = f'Bearer {token}'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print(res.get('message'))
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claim(token, id, query):
    url = f'https://prod-api.gleam.bot/api/v1/quests/{id}/claim'
    headers['Authorization'] = f'Bearer {token}'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print(res.get('message'))
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claimproject(token, slag, query):
    url = f'https://prod-api.gleam.bot/api/v1/projects/{slag}/farming/claim'
    headers['Authorization'] = f'Bearer {token}'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print(res.get('message'))
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claimrefill(token, query):
    url = 'https://prod-api.gleam.bot/api/v1/accounts/energy/refill/claim'
    headers['Authorization'] = f'Bearer {token}'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print(f" Status Claim : {res.get('message')}")
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def startrefill(token, query):
    url = 'https://prod-api.gleam.bot/api/v1/accounts/energy/refill/start'
    headers['Authorization'] = f'Bearer {token}'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print(f" Status Start : {res.get('message')}")
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def getreffstats(token):
    url = 'https://prod-api.gleam.bot/api/v1/referrals/stats'
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claimreffstats(token, query):
    url = 'https://prod-api.gleam.bot/api/v1/referrals/claim'
    headers['Authorization'] = f'Bearer {token}'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print(f" Status Claim : {res.get('message')}")
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claimdaily():

    while True:
        selector_ref = input("Claim ref point ? (default n) (y/n): ").strip().lower()
        if selector_ref in ['y', 'n', '']:
            selector_ref = selector_ref or 'n'
            break
        else:
            print("Input 'y' or 'n'.")

    while True:
        queries = load_credentials()
        for index, query in enumerate(queries):
            data_auth = auth(query)
            if data_auth is not None:
                token = data_auth.get('token')
                account = data_auth.get('account')
                energy = account['energyAmount']
                maxEnergy = account['maxEnergyAmount']
                print(f"ID : {account['id']} || Name : {account['firstName']} {account['lastName']} || Username : {account['beautyName']}")
                print(f"Energy : {account['energyAmount']}/{account['maxEnergyAmount']}")
                
                time.sleep(2) 
                data_list = list(token)
                if energy >= 5:
                    if data_list is not None:
                        for project in data_list['projects']:
                            print(f"Project : {project['title']}")
                            slug = project.get('slug')
                            data_claimproject = claimproject(token, slug, query)
                            if data_claimproject is not None:
                                print(f"Claim Amount Farming : {data_claimproject['farming']['claimedAmount']} ")
                            time.sleep(2)
                            data_quest = quest(token, slug)
                            if data_quest is not None:
                                for quests in data_quest['quests']:
                                    if energy != 0:
                                        completions = quests.get('completions')
                                        id = quests.get('id')
                                        if len(completions) == 0:
                                            print(f"Task : {quests['title']}")
                                            data_start = start(token, id, query)
                                            if data_start is not None:
                                                print('task opened...')
                                            time.sleep(2)
                                            data_check = check(token, id, query)
                                            if data_check is not None:
                                                print('task checked...')
                                            time.sleep(2)
                                            data_claim = claim(token, id, query)
                                            if data_claim is not None:
                                                print('task claimed...')
                                            time.sleep(2)
                                            energy-=1
                                        else:
                                            for comp in completions:
                                                state = comp.get('state')
                                                if state == 'Claimed':
                                                    print(f"Task : {quests['title']} DONE !!!")
                                                else:
                                                    print(f"Task : {quests['title']}")
                                                    data_check = check(token, id, query)
                                                    if data_check is not None:
                                                        print('task checked...')
                                                    time.sleep(2)
                                                    data_claim = claim(token, id, query)
                                                    if data_claim is not None:
                                                        print('task claimed...')
                                                    time.sleep(2)
                                    else:
                                        break
                            else:
                                print('detail quest not found')
                    else:
                        print('list quest not found')
                else:
                    print('Energy to low')
                
                if selector_ref == 'y':
                    statsref = getreffstats(token)
                    if statsref is not None:
                        reward = float(statsref.get('unclaimedRewardAmount'))
                        if reward > 0 :
                            claimreff = claimreffstats(token, query)
                            balance = claimreff.get('balance')
                            print(f"Claim Balance : {reward} : Total Claim Balance : {balance['totalAmount']}")

                if energy != maxEnergy:
                    data_claimrefill = claimrefill(token, query)
                    time.sleep(1)
                    if data_claimrefill is not None:
                        print("Energy Claimed")
                        time.sleep(1)

                    data_startrefill = startrefill(token, query)
                    if data_startrefill is not None:
                        print("Start Refill")
                        time.sleep(1)

            else:
                print('User Not Found')

        delay = random.randint(10800, 11000)
        printdelay(delay)
        time.sleep(delay)

#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################

def main():
    print(r"""
        
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sanscryptox
              
        select this one :
        1. claim daily (3 hours)
          
          """)

    selector = input("Select the one ? (default 1): ").strip().lower()

    if selector == '1':
        claimdaily()
    else:
        exit()

def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"{now} | Waiting Time: {hours} hours, {minutes} minutes, and {sec} seconds")


def print_welcome_message(serial=None):
    print(r"""
              
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sansxgroup
              
          """)
    print()
    if serial is not None:
        print(f"Copy, tag bot @SnailHelperBot and paste this key in discussion group t.me/sansxgroup")
        print(f"Your key : {serial}")

def read_serial_from_file(filename):
    serial_list = []
    with open(filename, 'r') as file:
        for line in file:
            serial_list.append(line.strip())
    return serial_list

serial_file = "serial.txt"
serial_list = read_serial_from_file(serial_file)


def get_serial(current_date, getpcname, name, status):
    formatted_current_date = current_date.strftime("%d-%m-%Y")
    # Encode each value using base64
    getpcname += "knjt"
    name    += "knjt"
    encoded_getpcname = base64.b64encode(getpcname.encode()).decode().replace("=", "")
    encoded_current_date = base64.b64encode(formatted_current_date.encode()).decode().replace("=", "")
    encoded_name = base64.b64encode(name.encode()).decode().replace("=", "")
    encoded_status = base64.b64encode(str(status).encode()).decode().replace("=", "")

    # Calculate the length of each encoded value
    getpcname_len = len(encoded_getpcname)
    current_date_len = len(encoded_current_date)
    name_len = len(encoded_name)
    status_len = len(encoded_status)

    # Concatenate the encoded values with their lengths
    serial = "S4NS-"
    serial += str(getpcname_len).zfill(2) + encoded_getpcname
    serial += str(current_date_len).zfill(2) + encoded_current_date
    serial += str(name_len).zfill(2) + encoded_name
    serial += str(status_len).zfill(2) + encoded_status
    return serial

def decode_pc(serial, getpcname, name, current_date):
    try:
        getpcname_len = int(serial[5:7])
        encoded_getpcname = serial[7:7+getpcname_len]
        current_date_len = int(serial[7+getpcname_len:9+getpcname_len])
        encoded_current_date = serial[9+getpcname_len:9+getpcname_len+current_date_len]
        name_len = int(serial[9+getpcname_len+current_date_len:11+getpcname_len+current_date_len])
        encoded_name = serial[11+getpcname_len+current_date_len:11+getpcname_len+current_date_len+name_len]
        status_len = int(serial[11+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len])
        encoded_status = serial[13+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len+status_len]

        # Decode each value using base64
        decoded_getpcname = base64.b64decode(encoded_getpcname + "==").decode()
        decoded_current_date = base64.b64decode(encoded_current_date + "==").decode()
        decoded_name = base64.b64decode(encoded_name + "==").decode()
        decoded_status = base64.b64decode(encoded_status + "==").decode()
        
        dates = compare_dates(decoded_current_date)

        if decoded_status != '1':
            print("Key Not Generated")
            return None
            
        elif decoded_getpcname.replace("knjt", "") != getpcname:
            print("Different devices registered")
            return None
        
        elif decoded_name.replace("knjt", "") != name:
            print("Different bot registered")
            return None
        
        elif dates > 7:
            print("Key Expired")
            return None
        else:
            print(f"            Key alive until : {decoded_current_date} ")
            return dates
    except Exception as e:
        print(f'Key Error : {e}')

def compare_dates(date_str):
    tanggal_compare_dt = datetime.strptime(date_str, '%d-%m-%Y')
    tanggal_now = datetime.now()
    perbedaan_hari = (tanggal_compare_dt - tanggal_now).days
    return perbedaan_hari

def started():
    getpcname = socket.gethostname()
    name = "AQUA GLEAM"
    current_date = datetime.now() # Get the current date
    status = '0'

    if len(serial_list) == 0:
        serial = get_serial(current_date, getpcname, name, status)
        print_welcome_message(serial)
    else:
        serial = serial_list[0]
        if serial == 'S4NS-XXWEWANTBYPASSXX':
            main()
        else:
            decodeds = decode_pc(serial, getpcname, name, current_date)
            if decodeds is not None:
                    print_welcome_message()
                    time.sleep(10)
                    main()         
            else:
                serial = get_serial(current_date, getpcname, name, status)
                print_welcome_message(serial)
                print("Please submit the key to bot for get new key")
            

if __name__ == "__main__":
    started()
