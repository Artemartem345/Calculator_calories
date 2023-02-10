from random import choice
from math import fabs
# import PyQt5 as PQ5


list_of_motivated = [
    "You can do this! dont give up!",
    "i believe in you!",
    "remember, lazy is your worst enemy now!",
]

class User:
    def __init__(
        self, 
        first_name: str, 
        middle_name: str, 
        last_name: str,
        weight:float = None,
        growth:str = None,
        sex:str = None,
        age:str = None,
        ):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.weight = weight or input('Enter your weight: ')
        self.growth = growth or input('Enter your growth: ')
        self.sex = self._input_sex(sex)
        self.age = age or input('Enter your age: ')

    def _input_sex(self, sex:str = ''):
        while not self.sex in ['male', 'female']:
            self.sex = input('Enter your sex: ')
        

    def __repr__(self) -> str:
        result = f'{self.first_name} {self.middle_name} {self.last_name}'
        result += f'\n   Weight: {self.weight} kg' #if 'weight' in self.__dict__.items() else ''
        result += f'\n   Growth: {self.growth} cm' #if 'growth' in self.__dict__.items() else ''
        result += f'\n   Age: {self.age} age '
        result += f'\n   Sex: {self.sex} '
        result += f'\n   Metabolism: {self.base_mtb} '
        result += f'\n   Coefficient_activity_mtb {self.user_activity_coeficient}'
        result += f'\n   Real_mtb {self.real_mtb}'
        result += f'\n   Goal {self.goal}\n'
        result += '-'*30
        return result

    def base_metabolism(self):    
        '''
        Для мужчин:
        Базовый метаболизм = 9,99×(вес в кг) + 6,25×(рост в см) – 4,92×(возраст в годах) + 5.
        Для женщин:
        Базовый метаболизм = 9,99×(вес в кг) + 6,25×(рост в см) – 4,92×(возраст в годах) – 161.
        '''
        base_mtb = 9.99 * self.weight + 6.25 * self.growth - 4.92 * self.age
        if self.sex == 'male':
            # 9,99×(вес в кг) + 6,25×(рост в см) – 4,92×(возраст в годах) + 5
            base_mtb += 5
        elif self.sex == 'female':
            # 9,99×(вес в кг) + 6,25×(рост в см) – 4,92×(возраст в годах) – 161
            base_mtb -= 161
        self.base_mtb = base_mtb

    def coeficient_activity_mtb(self, coeficient_mtb: float = 0):
        '''
        Этап #2: умножаем полученную цифру базового метаболизма на коэффициент активности.
        Коэффициент активности варьирует от 1.2 (сидячий 
        образ жизни, практически никакой физической активности) до 1.9 
        (Очень тяжелый физический труд / 2 интенсивные тренировки в день).
        '''
                  
        self.user_activity_coeficient = coeficient_mtb
        if not coeficient_mtb:
            doc_str = (f'   Коэффициент активности варьирует от 1.2 (сидячий \n'
                    f'    образ жизни, практически никакой физической активности) до 1.9\n' 
                    f'    (Очень тяжелый физический труд / 2 интенсивные тренировки в день).\n')
            print(f'\n {doc_str}')
        
        while not coeficient_mtb and True:
            try:
                self.user_activity_coeficient = float(input(f'Enter your activity coeficient (from 1.2 to 2) Enter: '))
            except ValueError:
                print('you cannot write any symbols not a numbers')
                continue
            else:
                if 1.2 <= self.user_activity_coeficient <= 2:
                    break
                else:
                    print('you cannot write nums less than 1.2')

        self.find_real_mtb()

    def find_real_mtb(self):
        self.real_mtb = self.base_mtb * self.user_activity_coeficient

    def user_great_goal(self, goal: float = 0):
        self.goal = goal or input('how many KG you want to have ?: ')    
      
    """
    Рассчитать кол-во потребляемых коллорий для достижения целевого веса за 3 мес, 6 мес и 12 мес 
    """
    def plan_for_callories(self):
        '''
        1. рассчитать разницу в весе, сколько он хочет
           потерять или набрать
        2. перевести вес в каллории (1 кг жира — это 7700 калорий)
        3. рассчитать сколько каллорий в день пользователь может потреблять в сроки 3, 6, 12 месяцев
        '''
        delta_weight = self.weight - self.goal        
        delta_goal = 'out' if delta_weight > 0 else 'add'
        result = f'you need to {delta_goal} some callories! in day: \n'
        
        months_len = [3, 6, 12]
        delta_weight_in_collories = fabs(delta_weight * 7700)
        get_delta = lambda months: int(delta_weight_in_collories/(months*30))
        deltas = zip(months_len, map(get_delta, months_len))        
        for item in deltas:
            result += f' plan for {item[0]} months : {item[1]} callories!\n'

        print(result)

        

    def input_user_callories_day():
        user = input('how many callories do you eat everyday?: ')
        
    def get_new_motivation(self):
        return choice(list_of_motivated)

def user_init(name: str = '', middle_name: str = '', last_name: str = '') -> User:
    name = name or input('Enter your name: ')
    middle_name = middle_name or input('Enter your middle name: ')
    last_name = last_name or input('Enter your last name: ')
    user0 = User(name, middle_name, last_name)
    return user0


if __name__ == '__main__':

    user = user_init('Artem', 'Vasilyevich', 'Popov')
    user.base_metabolism()
    user.coeficient_activity_mtb(1.4)
    user.user_great_goal(70)
    print(user)
    user.plan_for_callories()
    print(user.get_new_motivation())


