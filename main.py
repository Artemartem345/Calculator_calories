class User:
    def __init__(
        self, 
        first_name: str, 
        middle_name: str, 
        last_name: str,
        ):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

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

    
    def add_weight(self, weight: float = 0):
        self.weight = weight or input('Enter your weight: ')
    
    def add_growth(self, growth: float = 0):
        self.growth = growth or input('Enter your growth: ')

    def add_age(self, age: int = 0):
        self.age = age or input('Enter your age: ')
    
    def _sex(self, sex:str =''):
        self.sex = sex or input('enter your sex: ')

    def input_sex(self, sex:str = ''):
        self.sex = sex
        while not self.sex in ['male', 'female']:
            self._sex()
        
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
        
        from math import fabs
        delta_weight_in_collories = fabs(delta_weight * 7700)
        deltas = (
            delta_weight_in_collories/(12*30), 
            delta_weight_in_collories/(6*30), 
            delta_weight_in_collories/(3*30)
            )

        if delta_weight > 0:
            result = f'you need to out some callories in day!: \n'
        else:
            result = f'you need to add some callories! in day: \n'
            
        result += f' plan for 3 months : {deltas[0]} callories!\n'
        result += f' plan for 6 months : {deltas[1]} callories!\n'
        result += f' plan for 12 months : {deltas[2]} callories!\n'

        print(result)

        

    def input_user_callories_day():
        user = input('how many callories do you eat everyday?: ')
        


def user_init(name: str = '', middle_name: str = '', last_name: str = '') -> User:
    name = name or input('Enter your name: ')
    middle_name = middle_name or input('Enter your middle name: ')
    last_name = last_name or input('Enter your last name: ')
    user0 = User(name, middle_name, last_name)
    return user0





    





user = user_init('Artem', 'Vasilyevich', 'Popov')
user.add_weight(80.0)
user.add_growth(180)
user.add_age(20)
user.input_sex('male')
user.base_metabolism()
user.coeficient_activity_mtb(1.4)
user.user_great_goal(70)
print(user)
user.plan_for_callories()
