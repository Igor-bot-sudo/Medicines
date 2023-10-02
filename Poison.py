class Poison:
    # def __init__(self, name, cost, subjects) -> None:
    def __init__(self) -> None: 
      self.medicals = {
            'Medicinal decoctions': 'Подорожник-3 шт.',
            'Fellow': 'Петрушка-1 шт., Подоржник-2 шт.',
            'Robust': 'Черемуха-3шт., Петрушка-2шт., Подорожник-1 шт.'
        }

    #   self.name = name
    #   self.cost = cost
    #   self.subjects = subjects

    def check_description(self, name: str) -> str | None:
       if name in self.medicals.keys():
          return self.medicals[name]
       else:
          return None
          
