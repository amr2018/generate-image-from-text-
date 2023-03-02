
from PIL import Image
import re, random

# generate image from text
text = "make image 150 x 150 and blackground color is red"

def generate_image():
	colors = ['black', 'red', 'blue', 'yellow', 'white', 'skyblue']
	target_pattren = 'color n n'
	words = re.findall('[a-zA-Z0-9]+', text, re.IGNORECASE)
	generated_pattren = ''
	indexs = []

	random.shuffle(words)

	for i, word in enumerate(words):
		if word.isdigit():
			generated_pattren += ' n'
			indexs.append(i)
		elif word in colors:
			generated_pattren += ' color'
			indexs.append(i)
		else:
			pass

	generated_pattren = generated_pattren.strip()

	if generated_pattren != target_pattren:
		generate_image()
	else:
		print(generated_pattren, indexs)

		new_image = Image.new(
			mode = "RGB",
			size = (int(words[indexs[1]]), int(words[indexs[2]])),
			color = words[indexs[0]]
		)

		

		new_image.save('generated_image.jpg')
		new_image.show()

generate_image()
