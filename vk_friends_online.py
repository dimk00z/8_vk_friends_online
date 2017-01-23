import vk
from getpass import getpass


APP_ID = 5836646


def get_user_login():
    return input("Введите логин (email или номер телефона): ")


def get_user_password():
    return getpass("Введите пароль: ")


def get_online_friends(login, password):
    try:
        session = vk.AuthSession(
            scope='friends',
            app_id=APP_ID,
            user_login=login,
            user_password=password,)
        api = vk.API(session)
        onlne_friends_ids = api.friends.getOnline()
        return api.users.get(user_ids=onlne_friends_ids)
    except vk.exceptions.VkAuthError:
        print(vk.exceptions.VkAuthError)
        return None


def output_friends_to_console(friends_online):
    if not friends_online:
        exit()
    print('Следующие друзья в сети:')
    for friend in friends_online:
        print("{} {} id:{}".format(friend['first_name'],
                                   friend['last_name'], friend['uid']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
