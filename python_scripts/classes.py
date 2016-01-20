c_file_path = "data_csvs\customers.csv"
e_file_path = "data_csvs\employees.csv"
o_file_path = "data_csvs\orders.csv"
od_file_path = "data_csvs\order_datails.csv"


def make_rows_from_file(input_file):

	with open(input_file, "r") as csv_file:
		rows = []

		for data in csv_file:
			row = data.split(';')
			rows.append(row)

		return rows


class Employees:

	employee_count = 0

	def __init__(self, EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate, Address,
				City, Region, PostalCode, Country, HomePhone, Extension, Photo, Notes, ReportsTo, PhotoPath, Salary):

		self.EmployeeID = EmployeeID
		self.LastName = LastName
		self.FirstName = FirstName
		self.Title = Title
		self.TitleOfCourtesy = TitleOfCourtesy
		self.BirthDate = BirthDate
		self.HireDate = HireDate
		self.Address = Address
		self.City = City
		self.Region = Region
		self.PostalCode = PostalCode
		self.Country = Country
		self.HomePhone = HomePhone
		self.Extension = Extension
		self.Photo = Photo
		self.Notes = Notes
		self.ReportsTo = ReportsTo
		self.PhotoPath = PhotoPath
		self.Salary = Salary

	@staticmethod
	def check_file(file):
		for row in file:
			s_row = row.split(';')
			if not len(s_row) == 19:
				return False

	@staticmethod
	def parse(csv_row):
		employee = Employees(csv_row[0], csv_row[1], csv_row[2], csv_row[3], csv_row[4], csv_row[5], csv_row[6],
							csv_row[7], csv_row[8], csv_row[9], csv_row[10], csv_row[11], csv_row[12], csv_row[13],
							csv_row[14], csv_row[15], csv_row[16], csv_row[17], csv_row[18])
		return employee

	def persist(self):
		pass


class Customers:

	def __init__(self, CustomerID, CompanyName, ContactName, ContactTitle,
				Address, City, Region, PostalCode, Country, Phone, Fax):

		self.CustomerID = CustomerID
		self.CompanyName = CompanyName
		self.ContactName = ContactName
		self.ContactTitle = ContactTitle
		self.Address = Address
		self.City = City
		self.Region = Region
		self.PostalCode = PostalCode
		self.Country = Country
		self.Phone = Phone
		self.Fax = Fax

	@staticmethod
	def parse():
		pass

	def persist(self):
		pass


class Orders:

	def __init__(self, OrderID, CustomerID, EmployeeID, ContactTitle, OrderDate, RequiredDate, ShippedDate, ShipVia,
				Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry):

		self.OrderID = OrderID
		self.CustomerID = CustomerID
		self.EmployeeID = EmployeeID
		self.ContactTitle = ContactTitle
		self.OrderDate = OrderDate
		self.RequiredDate = RequiredDate
		self.ShippedDate = ShippedDate
		self.ShipVia = ShipVia
		self.Freight = Freight
		self.ShipName = ShipName
		self.ShipAddress = ShipAddress
		self.ShipCity = ShipCity
		self.ShipRegion = ShipRegion
		self.ShipPostalCode = ShipPostalCode
		self.ShipCountry = ShipCountry

	@staticmethod
	def parse():
		pass

	def persist(self):
		pass


class OrderDetails:

	def __init__(self, OrderID, ProductID, UnitPrice, Quantity, Discount):

		self.OrderID = OrderID
		self.ProductID = ProductID
		self.UnitPrice = UnitPrice
		self.Quantity = Quantity
		self.Discount = Discount

	@staticmethod
	def parse():
		pass

	def persist(self):
		pass
