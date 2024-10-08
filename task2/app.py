# 
# Part 1: Implement phone book class
# 

class PhoneBook:
    
    def __init__(self) -> None:
        self.contacts = []

    def add(self, name: str, surname: str, phone: str) -> None:
        """Adds a person to the phone book."""
        for contact in self.contacts:
            if contact['name'] == name and contact['surname'] == surname:
                return
        self.contacts.append({'name': name, 'surname': surname, 'phone': phone})

    def update(self, name: str, surname: str, phone: str) -> bool:
        """Updates information about a person in the phone book."""
        for contact in self.contacts:
            if contact['name'] == name and contact['surname'] == surname:
                contact['phone'] = phone
                return True
        return False

    def remove(self, name: str, surname: str) -> int:
        """Removes a person from the phone book."""
        for index, contact in enumerate(self.contacts):
            if contact['name'] == name and contact['surname'] == surname:
                self.contacts.pop(index)
                return 1
        return 0

    def search(self, name: str = None, surname: str = None) -> list[dict]:
        """Searches for a person in the phone book."""
        if name is None and surname is None:
            return self.contacts
        result = []
        for contact in self.contacts:
            if (contact['name'] == name) or (contact['surname'] == surname):
                result.append(contact)
        return result



# 
# Part 2: Implement console support
# 

def _main():
    pass


if __name__ == "__main__":
    _main()
