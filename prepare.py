import os
import MeCab

mecab = MeCab.Tagger("-Ochasen")

def split(text):
	node = mecab.parseToNode(text)
	keywords = []

	# mecab-python3パッケージのバグ対応(2019/4/22時点で必要)
	# See https://github.com/SamuraiT/mecab-python3/issues/19
	current = ""
	previous = ""

	while node:
		current = node.surface.strip("\n")
		diff = previous[:len(previous) - len(current)]
		if len(diff): keywords.append(diff)
		previous = current
		node = node.next
	return " ".join(keywords);

def main():
	result_file_path = "./corpus.txt"
	if os.path.exists(result_file_path): os.remove(result_file_path)
	result_file = open(result_file_path, "a")
	with open("./original.txt", "r") as file:
		for line in file:
			result_file.write(split(line) + "\n")
	result_file.close()

main()
