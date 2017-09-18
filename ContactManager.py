class Contact:
	def __init__(self, name, phone_number, email, website, birthday, picture):

		self.name=name
		self.phone_number=phone_number
		self.email=email
		self.website=website
		self.birthday=birthday
		self.picture=picture

	def __repr__(self):
		return """
		name= {}
		phone_number={}
		email={}
		website={}
		birthday={}
		picture={}
		""".format(self.name,self.phone_number, self.email, self.website, self.birthday, self.picture)

d_name=input("Enter name:")
d_phone_number=input("Phone number:")
d_email=input("email:")
d_website=input("website:")
d_birthday=input("DOB(DD/MM/YY):")
d_picture=input("Add a photo")

new_contact=Contact(d_name, d_phone_number, d_email, d_website, d_birthday, d_picture)
print(new_contact)
