# CLASS: Website, User
class Website(object):
  
  def __init__(self, name):
    self.name = name
    self.status = 'ON'
    self.db_users = []
    # w.users = [w.sign_up() for i in range(5)]
    
    self.users_logged_in = []

  def get_info(self):
    return 'NAME: {}\nSERVER STATUS: {}'.format(self.name, self.status)

  def set_users_logged_in(self):
    for user in self.db_users: 
      if user.status == True:
        self.users_logged_in.append(user)

  def turn_on(self):
    self.status = 'ON'

  def turn_off(self):
    self.status = 'OFF'

  def create_user(self, name, password):
    user = User(name)
    user.set_password(password)
    self.db_users.append(user)
    print 'Welcome to the platform!'
    return user

  def sign_up(self):
    '''
    Method that add user in list of website
    '''  
    print 'enter your name and your password..'
    return self.create_user(raw_input(),raw_input())
     

  def login(self):
    print 'digit your name and your password to enter in website..'
    if self.status == 'ON':
      request_name = raw_input()
      request_password = raw_input()
      for elem in self.db_users:
        print elem.name, elem.password
        if elem.name == request_name and elem.password == request_password:  
          return 'Login success!'
      return 'Please try again!'


class User(object):

  def __init__(self, name):
    self.name = name
    self.password = ''
    self.status = False

  def __str__(self):
    return '{}'.format(self.name)

  def __repr__(self):
    return self.__str__()

  def get_name(self):
    return 'User: {}'.format(self.name)

  def set_password(self, password):
    self.password = password

  def get_all_info(self):
    return 'NAME: {} PASSWORD: {}'.format(self.name, self.password)
