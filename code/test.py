import fire

mydictionary = {
    'name': 'Emanuel',
    'hobbies': ['play the guitar', 'read', 'The Office'],
    'bday': {
        'day': 1,
        'month': 6
    }
}


def hello(name = 'Allien'):
    """
    Say 'Hello' to user
    """
    return f'Hello, {name}!'


# '_' hidden the command
def _eyes():
    return 42


class Group:
    def eyes(self, number):
        return f'I have {number} eyes'


fire.Fire()