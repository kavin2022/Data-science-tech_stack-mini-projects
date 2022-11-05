import pymongo as py

class Telephone_Directory:
    def __init__(self):
        '''
        initializing the necessary connections, database, collection to a variable
        '''
        print('welcome to Telephone Directory')
        self.connection_uri = input('Enter the mongodb connection uri : ')
        self.client = py.MongoClient(self.connection_uri)
        self.db = self.client['Telephone_directory']
        self.collection = self.db['chennai_contact_details']
        

    def start(self):
        '''
        start method - gets a choice from a user
        :return: calls another method based on user's input
        '''
        print('Available options \n1. Create a contact\n2. Search a contact\n3. Update a contact\n4. Delete a contact\n0. to exit the directory')
        self.choice = input('Enter the one of the above choice in number( eg: for create enter 1) : ')
        if self.choice == '1':
            self.create()
        elif self.choice == '2':
            self.search()
        elif self.choice == '3':
            self.update()
        elif self.choice == '4':
            self.delete()
        elif self.choice == '0':
            self.exit()
        else:
            print(f'No option exists for that input ({self.choice}) please enter again')
            self.start()
    def create(self):
        '''
        :input: gets the name,phone no,place of the contact
        :working:  it create a document in the collection with above details
        :return: start method to show available options again
        '''
        self.name = input('Enter the name of the contact or enter 0 for options menu : ').casefold()
        if self.name == '0':
            self.start()
        else:
            self.phone_no = input('Enter the Phone no. of the contact: ')
            self.place = input('Enter the place of the contact : ')
            self.collection.insert_one({'Name': self.name, 'Phone no': self.phone_no, 'Place': self.place})
            self.start()

    def search(self):
        '''
        :input: get the name of the contact
        :working: based on the name it searches the collection and prints the contact
        :return: start method to show available options again
        '''
        self.name = input('Enter the name of the contact or enter 0 for options menu : ').casefold()
        if self.name == '0':
            self.start()
        else:
            self.output = list(self.collection.find({'Name': self.name},{'_id':0}))
            if self.output == []:
                print('----ENTERED CONTACT NOT AVAILABLE----')
            else:
                for self.i in self.output:
                    print(self.i)
            self.start()
    def update(self):
        '''
        :input: gets the details to update and get the name of the contact
        :working: based on the name it searches the collection and asks the new details and updates the information
        :return: start method to show available options again
        '''
        print('Details to change\n1. Name\n2. Phone no\n3. Place\n0. go back to options menu ')
        print('Instruction :\nenter input as number \neg:\n 1. to change name - enter: 1 \n 2. to change name,phonenumber -enter : 1,2 ')

        self.inp = input('Enter the detail to change as per the instructions: ').split(',')
        if '0' in self.inp:
            self.start()
        else:
            self.name_2_query = input('Enter the name to be updated : ').casefold()
            for self.i in self.inp:
                if self.i == '1':
                    print('changing name of the contact')
                    self.new_name = input('Enter new name : ').casefold()
                    self.collection.update_one({'Name': self.name_2_query},
                                                {'$set': {'Name': self.new_name}})
                    self.name_2_query = self.new_name
                elif self.i == '2':
                    print('changing phone number of the contact')
                    self.new_phno = input('Enter new Phone number : ')
                    self.collection.update_one({'Name': self.name_2_query},
                                                        {'$set': {'Phone no': self.new_phno}})
                elif self.i == '3':
                    print('changing place of the contact')
                    self.new_place = input('Enter new Place : ')
                    self.collection.update_one({'Name': self.name_2_query},
                                                           {'$set': {'Place': self.new_place}})
                else:
                    print('not a valid option')
            self.start()
    def delete(self):
        '''
        :input: get the name of the contact to delete
        :working: based on the name it searches the collection and deletes the document from the collection
        :return: start method to show available options again
        '''
        self.name_2_query = input('Enter the name to be deleted or press 0 to go back to options : ').casefold()
        if self.name_2_query == '0':
            self.start()
        else:
            self.collection.delete_one({'Name': self.name_2_query})
            self.start()
    def exit(self):
        '''
        prints the thk you line and ends the program
        '''
        print('Thank you for using this telephone directory')
