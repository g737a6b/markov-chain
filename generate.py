import markovify

with open("./corpus.txt") as file:
	text = file.read()

text_model = markovify.NewlineText(text)

for i in range(24):
	print(text_model.make_short_sentence(100).replace(" ", ""))
