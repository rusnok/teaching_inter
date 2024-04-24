from dataclasses import dataclass
import pickle


@dataclass
class User:
    name: str
    surname: str

    @classmethod
    def create_pickle(cls, user):
        with open("data.pickle", "wb") as f:
            return pickle.dump(user, f)

    @classmethod
    def load_pickle(self):
        with open("data.pickle", "rb") as f:
            data_load = pickle.load(f)

        return(data_load)


user_1 = User("Katka", "Klimkova")
user_1.create_pickle()
user_1.load_pickle()
print(user_1)