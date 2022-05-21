from server.models import add_user
from customers.password import get_new_password, check_strong_password
from customers.users import get_new_user_name

print("Добавление пользователя в систему")
# login = input("Login: ") # для самостоятельного ввода нового пользователя
# pswd = input("Password: ")
# if check_strong_password(pswd):
#    add_user(login, pswd)

for i in range(15):
    login = get_new_user_name()
    pswd = get_new_password()

    if check_strong_password(pswd):
        add_user(login, pswd)
add_user("Inessa", get_new_password())
add_user("Alena", get_new_password())
add_user("Alena", get_new_password())






