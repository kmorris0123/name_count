def name_counter():

	counter_dict = {}

	with open('nameslist.txt') as open_file:

		all_text = open_file.readline()

		while all_text:

			all_text = all_text.strip()
			if all_text in counter_dict:
				counter_dict[all_text] += 1

			else:

				counter_dict[all_text] = 1

			all_text = open_file.readline()
	print(counter_dict)

def main():

	name_counter()


if __name__ == "__main__":
	main()