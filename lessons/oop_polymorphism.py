# Полиморфизм - это механизм, позволяющий выполнить один и тот же код по-разному,
# (в джаве исходя из поданных типов данных, в питоне не совсем так)
# напоминание: новые классы это новый тип данных
# Ducktyping (утиная типизация) - наличие поведения для использования в полиморфизме
# В ЯП со статической типизацией для полиморфизма важно кто ты (какой тип), для питона важно что ты умеешь(поведение)

class Animal:
    def make_noise(self):
        print('shhh')


class Cat(Animal):
    def make_noise(self):
        print('meow')


class Dog(Animal):
    def make_noise(self):
        print('gav')


class Car:
    def make_noise(self):
        print('bi-bi')


def noise(animal: Animal):
    animal.make_noise()


# -------------Example 2------------------
class SQLiteDatabase:
    def connect(self):
        print('Connecting to SQLitedatabase')

    def get_users(self):
        print('get users with SQL')


class MongoDatabase:
    def connect(self):
        print('Connecting to MongoDatabase')

    def get_users(self):
        print('get users with NoSQL')


class Server:
    def get_users(self, db):
        db.connect()
        users = db.get_users()
        return users

def get_db_from_conbfing():
    print('read config')
    return SQLiteDatabase()

if __name__ == '__main__':
    noise(Cat())
    noise(Car())

    print('-------------Example 2------------------')
    server = Server()
    server.get_users(get_db_from_conbfing())
