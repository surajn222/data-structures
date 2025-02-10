import re

import pandas as pd
import requests

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def main():
	df = pd.DataFrame(columns=['name', 'category', 'complexity', 'link', 'name_lower'])
	for i in range(1, 19):
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		# r = requests.get(url=urlLogin, params=params, headers=headers)
		response = requests.get("https://www.techiedelight.com/Category/Binary-Tree/page/" + str(i) + "/",
								headers=headers)
		# print(response.content)

		# class="entry-title"(.*?)<header class="entry-header"
		# print("here")
		# list_regex = re.findall('class="entry-title"(.*?)<header class="entry-header"', str(response.content.decode("utf-8")))
		list_regex = re.findall('class="entry-title"(.*?)<header class="entry-header"',
								str(response.content))

		for string in list_regex:
			print(string)
			list_name = re.findall('"bookmark">(.*?)</a>', str(string))
			list_category = re.findall('Category/(.*?)/', str(string))
			list_complexity = re.findall('Tags/(.*?)"', str(string))
			list_link = re.findall('href="(.*?)" rel="bookmark', str(string))

			print(list_name)
			print(list_category)
			print(list_complexity)
			print(list_link)

			str_name = list_name[0]
			# str_complexity = list_complexity[0]
			str_complexity = ",".join(list_complexity)
			str_category = ",".join(list_category)
			str_link = list_link[0]
			str_name_lowercase = str_name.lower().replace(" ", "_")

			to_append = [str(str_name), str(str_category), str(str_complexity), str(str_link), str(str_name_lowercase)]
			df_length = len(df)
			df.loc[df_length] = to_append
			print(df)

	# df.to_csv("arrays.csv", delimiter = ";")
	# df.to_csv("arrays.csv", sep=';', index=True)
	df.to_csv("binarytrees.csv", sep=';', index=True)


# np.savetxt('arrays.csv', df, delimiter=';')
# "bookmark">(.*?)</a>
# Category/(.*?)/
# Tags/(.*?)"


if __name__ == "__main__":
	main()
