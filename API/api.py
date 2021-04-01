import requests

URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

PARAMS = "name=Dark Magician"

r = requests.get(url=URL, params = PARAMS)



data = r.json()

print(data['data'][0]['type'])




class Monster(object):
    def __init__(self, name, effects, attributes, monster_type, atk, _def, description):
        self.name = name
        self.effects = effects
        self.attributes = attributes
        self.type = monster_type
        self.atk = atk
        self._def = _def
        self.description = description

    def effect(self):
        """
        Activate the effect of this monster.
        """
        for effect in self.effects:
            eval(effect)


class Spell(object):
    def __init__(self, name, effects):
        self.name = name
        self.effects = effects

    def activate(self):
        """
        Activate the effect of this spell.
        """
        for effect in self.effects:
            eval(effect)


class Trap(object):
    def __init__(self, name, effects):
        self.name = name
        self.effects = effects

    def activate(self):
        """
        Activate the effect of this spell.
        """
        for effect in self.effects:
            eval(effect)

def create_monster(data):
    name = data['data'][0]['name']
    monster_type = data['data'][0]['type']
    atk = data['data'][0]['atk']
    _def = data['data'][0]['def']
    description = data['data'][0]['desc']
    attribute = data['data'][0]['attribute']
    M = Monster(name, attributes=attribute, monster_type=monster_type, atk=atk, _def=_def, description=description, effects='')
    print(M)
    return M

if __name__ == "__main__":
    i = create_monster(data)
    print(i.name)
    print(i.attributes)
    print(i.type)
    print(i.atk)
    print(i._def)
    print(i.description)
    print(i.effects)