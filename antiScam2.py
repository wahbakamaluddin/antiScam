import requests
import random
import threading

with open("path-to-passList.txt", "r") as file:
    passw = file.read().splitlines()


url1 = "1st URL"    #paste the 1st url here
url2 = "2nd URL"    #paste the 2nd url here
url3 = "3rd URL"    #paste the 3rd url here

def do_Request():
    global i
    while True:
        randPhoneNum = random.randint(1000000000, 1999999999)
        
        # Generate a random PIN (5 digits)
        randPin = ''.join(str(random.randint(0, 9)) for _ in range(5))
        
        randPass = random.choice(passw)

        # POST data as a dictionary
        data1 = {
        'var-1' : randPhoneNum    #paste variable name for the phone number on varName
        }
        data2 = {
            'pin1': randPin[0],
            'pin2': randPin[1],
            'pin3': randPin[2],
            'pin4': randPin[3],
            'pin5': randPin[4]
        }
        data3 = {'var-3': randPass}
        try:
            # Send POST requests
            response1 = requests.post(url1, data=data1)
            # response2 = requests.post(url2, data=data2)
            response3 = requests.post(url3, data=data3)

            print(f"Iteration {i}: {randPhoneNum}, {randPass}")
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