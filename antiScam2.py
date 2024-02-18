import requests
import random
import threading

with open("passList.txt", "r") as file:
    passw = file.read().splitlines()
with open("names.txt", "r") as file:
    names = file.read().splitlines()

url1 = "https://sumbangan-tunai-rahmah1.malaysia2024.my.id/data.php"
#url2 = "https://bantuankerann.mlysia.my.id/req/code.php"
url3 = "https://sumbangan-tunai-rahmah1.malaysia2024.my.id/bola.php"

def do_Request():
    global i
    while True:
        randPhoneNum = random.randint(1000000000, 1999999999)
        
        # Generate a random PIN (4 digits)
        #randPin = ''.join(str(random.randint(0, 9)) for _ in range(5))
        
        randPass = random.choice(passw)

        randName = random.choice(names) + random.choice(names)

        # POST data as a dictionary
        data1 = {
        'Pengguna' : randName,
        'phoneNumber' : randPhoneNum,
        'sendPhone' : ""
        }
        # data2 = {
        #     'pin1': randPin[0],
        #     'pin2': randPin[1],
        #     'pin3': randPin[2],
        #     'pin4': randPin[3],
        #     'pin5': randPin[4]
        # }
        data3 = {'password': randPass}
        try:
            # Send POST requests
            response1 = requests.post(url1, data=data1)
            # response2 = requests.post(url2, data=data2)
            response3 = requests.post(url3, data=data3)

            print(f"Iteration {i}: {randName}, {randPass}")
            i += 1

        except requests.exceptions.ConnectTimeout as e:
            print(f"Connect timeout error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


threads = []

for _ in range(50):
    t = threading.Thread(target=do_Request)
    t.daemon = True
    threads.append(t)

i = 1  # Initialize i
for t in threads:
    t.start()

for t in threads:
    t.join()