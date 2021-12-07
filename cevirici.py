import requests
from PIL import Image
from io import BytesIO

url = "https://" + input("Url yazın: ")

endpoint = "https://api.qrserver.com/v1/create-qr-code/"

orn = f"?data={url}&amp;size=500x500"
color = "&color=000000"

response = requests.get(endpoint + orn + color)

img = Image.open(BytesIO(response.content))

img.save("qr.png")
