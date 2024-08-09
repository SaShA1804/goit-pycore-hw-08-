import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class AddressBook:
    def __init__(self, filename="addressbook.pkl"):
        self.filename = filename
        self.contacts = []

    def add_contact(self, person: Person):
        self.contacts.append(person)

    def remove_contact(self, name: str):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return AddressBook(filename)  # Повернення нової адресної книги, якщо файл не знайдено


