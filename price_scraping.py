import screenshot
import multivision
import image_splitter

url = "https://www.amazon.com/s?k=raspberry+pi"

shot = screenshot.take(url, full_page=True)

shots = image_splitter.split(shot, "splits", 1200, offset=300)

response = multivision.look(shots, 'Extract all the products and their prices from these website screenshots and return them in JSON format [{"name": "Name here", "price": 1.23}]')

print(response)
