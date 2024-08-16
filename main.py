from rembg import remove

input_photo = 'Fotoğraf - 12.05.2022 14.24 #3.jpg'
output_photo = 'netix.png'

with open(input_photo,'rb') as i:
    with open(output_photo,'wb') as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)
