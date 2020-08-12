import string
import random


class Base62Generator:
    base_str = string.ascii_letters + string.digits

    def random(self, length):
        return "".join(random.choice(self.base_str) for _ in range(length))


base62 = Base62Generator()
