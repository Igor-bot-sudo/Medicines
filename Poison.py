class Poison:
    def __init__(self) -> None:      
        self.medicals = {
            'Целебный отвар': ('Подорожник-3 шт.', '10 коп.'),
            'Приятель': ('Петрушка-1 шт., Подоржник-2 шт.', '15 коп.'),
            'Прилив сил': ('Черемуха-3шт., Петрушка-2шт., Подорожник-1 шт.', '20 коп.')
        }

    def check_description(self, name: str) -> str | None:
       if name in self.medicals.keys():
          return self.medicals[name]
       else:
          return None
