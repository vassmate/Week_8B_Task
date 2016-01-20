import mysql
import mysql.connector

connector = mysql.connector.connect(user='root', password='vassmate1991', host='localhost')
my_cursor = connector.cursor()
test_file_path = "data_csvs\dump_data.csv"


def parse(file_path):

	my_cursor.execute("USE meetup_registration_database")

	with open(file_path, "r") as csv_file:
		data = []
		for row in csv_file:
			data.append(row.split(';'))

		return data


def test_def():
	c = 0

	for n in range(5):
		print(parse(test_file_path)[0][c])
		c += 1


test_def()
