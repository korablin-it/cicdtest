import requests
import uuid
import random
import string
import json
url = 'http://89.108.117.158:7081/balancer/api/v1.0/request' 


#GUID
unique_id = uuid.uuid4()
random_guid = str(unique_id)

def generate_random_string(length):
    characters = string.ascii_uppercase + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
#DOCUMETID
random_docid = generate_random_string(25)

data = {
    "guid": random_guid,
    "urls": [
        {
            "id": "0",
            "url": "https://storage.googleapis.com/sm-pepsico-ru-po1-0x19007abd5a-upload/pepsico-ru-po1/2023/9/1/19eee759-d073-45b1-9dfd-76ec2f5dd2fe/19eee759-d073-45b1-9dfd-76ec2f5dd2fe_0.jpg",
            "xyz": [
                9.1986,
                0,
                90.0220463552935
            ],
            "roll": 90.0220463552935,
            "time": "1693566448",
            "accel": {
                "x": 0.2023,
                "y": 9.7187,
                "z": 1.2791
            },
            "floor": False,
            "pitch": 9.198573892607882,
            "azimuth": 0,
            "magnetic": {
                "x": 1.925,
                "y": -37.75,
                "z": -30.975
            },
            "md5_hash": "hrJADlPAw8fcaGbyODn/Dw==",
            "roll_real": 88.8075,
            "pitch_real": 7.4962,
            "orientation": 90,
            "azimuth_real": 0,
            "camera_model": "Nokia G50",
            "sending_time": "2023-09-01T11:07:43Z",
            "exif_orientation": 0,
            "index": 0
        },
        {
            "id": "1",
            "url": "https://storage.googleapis.com/sm-pepsico-ru-po1-0x19007abd5a-upload/pepsico-ru-po1/2023/9/1/19eee759-d073-45b1-9dfd-76ec2f5dd2fe/19eee759-d073-45b1-9dfd-76ec2f5dd2fe_1.jpg",
            "xyz": [
                8.7571,
                0,
                92.16938486460107
            ],
            "roll": 92.16938486460107,
            "time": "1693566452",
            "accel": {
                "x": -0.091,
                "y": 9.6193,
                "z": 1.3832
            },
            "floor": False,
            "pitch": 8.757051591106872,
            "azimuth": 0,
            "magnetic": {
                "x": -1.55,
                "y": -35.725,
                "z": -28.2
            },
            "md5_hash": "69jxw30fPB9N/fsDkdGfvA==",
            "roll_real": 90.5419,
            "pitch_real": 8.1826,
            "orientation": 90,
            "azimuth_real": 0,
            "camera_model": "Nokia G50",
            "sending_time": "",
            "exif_orientation": 0,
            "index": 1
        },
        {
            "id": "2",
            "url": "https://storage.googleapis.com/sm-pepsico-ru-po1-0x19007abd5a-upload/pepsico-ru-po1/2023/9/1/19eee759-d073-45b1-9dfd-76ec2f5dd2fe/19eee759-d073-45b1-9dfd-76ec2f5dd2fe_2.jpg",
            "xyz": [
                7.5452,
                0,
                90.78428919282423
            ],
            "roll": 90.78428919282423,
            "time": "1693566456",
            "accel": {
                "x": -0.1927,
                "y": 9.7079,
                "z": 1.2169
            },
            "floor": False,
            "pitch": 7.545197344721053,
            "azimuth": 0,
            "magnetic": {
                "x": -12.1625,
                "y": -38.15,
                "z": -27.3125
            },
            "md5_hash": "wSTpvVmPfPb4utuWzI1N2Q==",
            "roll_real": 91.1374,
            "pitch_real": 7.1432,
            "orientation": 90,
            "azimuth_real": 0,
            "camera_model": "Nokia G50",
            "sending_time": "",
            "exif_orientation": 0,
            "index": 2
        },
        {
            "id": "3",
            "url": "https://storage.googleapis.com/sm-pepsico-ru-po1-0x19007abd5a-upload/pepsico-ru-po1/2023/9/1/19eee759-d073-45b1-9dfd-76ec2f5dd2fe/19eee759-d073-45b1-9dfd-76ec2f5dd2fe_3.jpg",
            "xyz": [
                7.1097,
                0,
                91.5908329891767
            ],
            "roll": 91.5908329891767,
            "time": "1693566460",
            "accel": {
                "x": -0.4417,
                "y": 9.903,
                "z": 1.3533
            },
            "floor": False,
            "pitch": 7.109666036998746,
            "azimuth": 0,
            "magnetic": {
                "x": -8.4875,
                "y": -42.2,
                "z": -28.125
            },
            "md5_hash": "H64RMicVwq9h7goYWPZXjA==",
            "roll_real": 92.554,
            "pitch_real": 7.7741,
            "orientation": 90,
            "azimuth_real": 0,
            "camera_model": "Nokia G50",
            "sending_time": "",
            "exif_orientation": 0,
            "index": 3
        }
    ],
    "amount": 4,
    "status": 2,
    "userId": "RUMEGB",
    "version": 3,
    "visitId": "3f1723e7-2995-497a-97ba-5762aa972749",
    "settings": {
        "options": {
            "type": "before_po1_mt_omp_drinks",
            "type_collection": "photo"
        },
        "project_id": "1",
        "report_type": "default",
        "project_name": "test"
    },
    "rerun_url": "http://s.gate.smartmerch.it:5081/balancer/api/v1.0/request",
    "documentId": random_docid,
    "marketplaceId": "0200648704",
    "extension_data": {
        "gps": {
            "latitude": 55.7033891,
            "longitude": 37.9465672
        },
        "source": "smartmerch",
        "version": "1.0",
        "employee": {
            "employeeId": "RUMEGB",
            "employeeName": "",
            "positionName": ""
        },
        "marketplace": {
            "marketplaceId": "0200648704",
            "marketplaceSD": "",
            "marketplaceCity": "",
            "marketplaceName": "ООО \"Агроторг\"",
            "marketplaceType": "",
            "marketplaceAddress": "ул.Вертолётчиков, д.4, стр.10, г.Москва, г. Москва",
            "marketplaceClientId": "0200648704",
            "marketplaceDivision": "",
            "marketplaceChainName": "PYATEROCHKA|L7"
        }
    }
}

response = requests.post(url, json=data)
print(response.text)
