import random, getpass, json, sys, os


class Scramblr:
    """
        The Scramblr class will contain necessary
        functions to scramble phrases.
    """
    def __init__(self, use_special_chars):
        self.phrase = None
        self.security_indexes = []
        self.use_special_chars = use_special_chars
        self.pwd = '.pwd'

    def _get_random_character(self):
        alphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' + ['!@#$%&_' if self.use_special_chars else ''][0] 
        return alphanum[random.randint(0, len(alphanum) - 1)]

    def in_use(self,  index):
        for i in self.security_indexes:
            if i == index:
                return True
        return False

    def _get_indexes(self, phrase):
        for index in range(len(phrase)):
            if not self.in_use(index):
                random_replace_character = self._get_random_character()
                self.security_indexes.append((index, random_replace_character))
        if len(self.security_indexes) != len(phrase):
            self._get_indexes(phrase)

    @staticmethod
    def _deserialize_validation_indexes(indexes, phrase):
        container = []
        count = 0
        for _, value in indexes.items():
            if value[0] != phrase[count]:
                print('Invalid phrase')
                sys.exit(0)
            container.append(value[1])
            count += 1
        return ''.join(container)

    @staticmethod
    def _deserialize_validation_indexes_reverse(indexes, phrase):
        container = []
        count = 0
        for _, value in indexes.items():
            if value[1] != phrase[count]:
                print('Invalid phrase')
                sys.exit(0)
            container.append(value[0])
            count += 1
        return ''.join(container)

    @staticmethod
    def _validate(phrase_in_db, scrambled):
        user = phrase_in_db[0:phrase_in_db.index(':')]
        pwd = phrase_in_db[phrase_in_db.index(':') + 1:]
        if user != getpass.getuser() and pwd != scrambled:
            raise ValueError('Username or Password invalid.')
        else:
            return True

    def _save_to_db(self):
        try:
            with open(self.pwd, 'w') as pwd:
                user = getpass.getuser()
                phrase = self.phrase
                obj = self._build_json(self.security_indexes, self.original)
                alt = json.dumps(obj)
                query = user + ':' + phrase + '-' + alt
                pwd.write(query)
        except Exception:
            if os.path.exists(self.pwd):
                os.remove(self.pwd)

    @staticmethod
    def _build_json(indexes, phrase):
        obj = {}
        for index in indexes:
            count = index[0]
            obj[index[0]] = (index[1], phrase[count])
        return obj

    @staticmethod
    def _db_conn():
        with open('.pwd', 'r') as pwd:
            return pwd.read()

    def scramble(self, phrase):
        self.original = phrase
        self._get_indexes(phrase)
        updated_phrase = None
        for indexes in self.security_indexes:
            if updated_phrase is None:
                updated_phrase = phrase[:indexes[0]] + \
                                 indexes[1] + \
                                 phrase[indexes[0] + 1:]
            else:
                updated_phrase = updated_phrase[:indexes[0]] + \
                                 indexes[1] + \
                                 updated_phrase[indexes[0] + 1:]
        self.phrase = updated_phrase
        self._save_to_db()
        return updated_phrase

    def unscramble(self, phrase, reverse=False):
        phrase_in_db = self._db_conn()
        obj = json.loads(phrase_in_db[phrase_in_db.index('-') + 1:])
        unscrambled = None
        if reverse:
            unscrambled = self._deserialize_validation_indexes_reverse(obj, phrase)
        else:
            unscrambled = self._deserialize_validation_indexes(obj, phrase)
        if self._validate(phrase_in_db, phrase):
            return unscrambled

