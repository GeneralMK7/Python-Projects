import requests,datetime
from API import creds
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "madhukirangolla24"
GRAPH_ID = "graph1"
user_parameters = {
    "token" : creds.PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#----------------------------------------CREATE_USER-------------------------------------------#
create_user = requests.post(url=PIXELA_ENDPOINT,json=user_parameters)
print(create_user.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN" : creds.PIXELA_TOKEN
}
graph_parameters = {
    "id": GRAPH_ID,
    "name" : "Cycling-Graph",
    "unit": "Km",
    "type" : "float",
    "color" : "ajisai"
}

#----------------------------------------CREATE_GRAPH-------------------------------------------#
create_graph = requests.post(url=graph_endpoint, json=graph_parameters,headers=headers)
print(create_graph.text)



#----------------------------------------POST_PIXEL---------------------------------------------#
today = datetime.datetime.now()
post_pixel_parameters = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "1.43"
}
post_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
post_pixel = requests.post(url=post_pixel_endpoint,json=post_pixel_parameters,headers=headers)
print(post_pixel.text)

#-----------------------------------------PUT_PIXEL---------------------------------------------#
put_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
put_pixel_parameters = {
    "quantity" : "2.42"
}

put_pixel = requests.put(url=put_pixel_endpoint,json=put_pixel_parameters,headers=headers)
print(put_pixel.text)

#-----------------------------------------DELETE_PIXEL--------------------------------------------#

delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
delete_pixel = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(delete_pixel.text)
