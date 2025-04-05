import binascii 
image_order_number = 0 
image_content = '' 
image_headers_locations_list = [] 

def getHeadersLocations(): 
	global image_content 
	global image_headers_locations_list 
	image = open(r"/home/bruce/Desktop/autopsy.jpg", "rb") 
	image_content = image.read().hex().strip() 
	
	for image_header_index in range(len(image_content)): 
		if image_content.startswith('ffd8ffe0', image_header_index): 
			image_headers_locations_list.append(image_header_index) 

def getImageHexa(header_location): 
	last_header = image_headers_locations_list[-1] 
	current_header = image_headers_locations_list[header_location] 
	
	if current_header == last_header: 
		image_content_string = image_content[current_header:] 
	else:
		next_header = image_headers_locations_list[header_location + 1]
		image_content_string = image_content[current_header:next_header] 
	
	return binascii.a2b_hex(image_content_string) 

def createImage(hexa_of_image_content): 
	global image_order_number 
	image_order_number += 1 
	
	with open(f"./image_{image_order_number}.jpg", 'wb') as image_file: 
			image_file.write(hexa_of_image_content) 

def main(): 
	getHeadersLocations() 
	for header_location in range(len(image_headers_locations_list)): 
		hexa_of_image_content = getImageHexa(header_location) 
		createImage(hexa_of_image_content) 
		
if __name__ == '__main__': 
	main()