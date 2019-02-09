class Dog():
    """This docstring will discuss how to interact with our Dog class.

    Our Dog class will have two attributes - a name and happiness_level.
    It's one method, wag_tail, will simulate the dog wagging it's tail
    some number of times, and increasing it's happiness level.

    Parameters:
    -----------
        name: str
        happiness_level: int
    """

    def __init__(self, name, happiness_level=5):
        self.name = name
        self.happiness_level = happiness_level

    def wag_tail(self, n):
        """Wags the dogs tail n times, and each time increase
        happiness level by 5.

        Args:
            n: int
        """
        self.happiness_level += n * 5


def pizza_func(sizes, costs):
	areas = []
	for size in sizes:
		areas.append(3.14*(size/2)**2)
	cpi = []
	for i in range(len(areas)):
		cpi.append(areas[i]/costs[i])
	min_cpi = min(cpi)
	min_ind = cpi.index(min_cpi)
	return sizes[min_ind]


class Pizza():

	def __init__(self, restaurant):
		self.name = restaurant
		self.sizes = []
		self.costs = []
		self.areas = []

	def add_pie(self, size, cost):
		self.sizes.append(size)
		self.costs.append(cost)
		self.areas.append(self.calc_area(size))

	def calc_area(self, size):
		return 3.14 * (size/2)**2

	def best_price(self):
		cpis = [self.costs[i] * self.areas[i] for i in range(len(sizes)-1)]
		min_cpi = min(cpis)
		min_ind = cpis.index(min_cpi)
		return self.sizes[min_ind]


class Cat():
    """This docstring will discuss how to interact with our Cat class.

    Our Cat class will have three attributes - a name, laziness level,
    and a location. It's one method, sense_earthquake, will change
    the cats location based on whether or not there is an earthquake.

    Parameters
    ----------
        name: str
        laziness_level: int
            This holds how lazy the cat is on a scale of 1 to 10.
        location: str
            This holds where the cat is currently located at.
    """

    def __init__(self, name, laziness_level=5, location='home'):
        self.name = name
        self.laziness_level = laziness_level
        self.location = location

    def sense_earthquake(self, earthquake):
        """Checks if the cat senses an earthquake, and if so changes the cat's
        location to 'gone dark'.

        Args:
            earthquake: boolean
                Holds a True or False as to whether there was an earthquake.
        """
        if earthquake:
            self.location = 'gone dark'
            print('{} has {}!'.format(self.name, self.location))
        else:
            print('{} is at {}.'.format(self.name, self.location))

class Car():

    def __init__(self, model, color, tank_size):
        self.model = model
        self.color = color
        self.tank_size = tank_size
        self.gallons_of_gas = self.tank_size

    def drive(self, miles_driven):
        self.gallons_of_gas -= miles_driven/10

class Plane():

    def __init__(self, destination, departure_city, trip_distance):
        self.destination = destination
        self.departure_city = departure_city
        self.trip_distance = trip_distance

    def fly(self):
        self.departure_city, self.destination = self.destination, self.departure_city

class Company():

    def __init__(self, name, industry_type, num_employees=0, total_revenue=0):
        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue

    def serve_customer(self, cost):
        self.total_revenue += cost

    def gain_employees(self, employees):
        self.num_employees += len(employees)

class TV():

    def __init__(self):
        self.on = False
        self.channel = 0
        self.life_perc = 1

    def hit_power(self):
        if self.on:
            self.on = False
            self.life_perc -= 0.01
            self.channel = 0
            print('Power Off')
        else:
            self.on = True
            print('Power On')

    def change_channel(self, int):
        if self.on:
            self.channel = int
        else:
            print('Television is not on!')

class OurClass():

    def __init__(self, name, location, size=0, members=None, instructors=None):
        self.name = name
        self.location = location
        self.at_capacity = False
        if members==None:
            self.members = []
        else:
            self.members = members
        if instructors==None:
            self.instructors = []
        else:
            self.instructors = instructors
        self.size = len(self.members)
        self.check_if_at_capacity()

    def add_class_members(self, name, hair_color, birthdate):
        self.members.append(Members(name, hair_color, birthdate))
        self.check_if_at_capacity()

    def add_instructor(self, name):
        self.isntructors.append(Instructor(name))

    def check_if_at_capacity(self):
        if self.size >= 31:
            self.at_capacity = True
            print('Capacity Reached!')
        else:
            self.at_capacity = False
            print('{} more spots available'.format(31-self.size))

    def get_member_names(self):
        return [mem.name for mem in self.members]

    def get_instructor_names(self):
        return [ins.name for ins in self.instructors]

    def get_num_questions_asked(self):
        total_questions_asked = 0
        for mem in self.members:
            total_questions_asked += len(mem.questions_asked)
        return total_questions_asked

    def get_num_lines_coded(self):
        total_lines_coded = 0
        for mem in self.members:
            total_lines_coded += mem.num_lines_coded
        return total_lines_coded

    def get_num_questions_answered(self):
        total_questions_answered = 0
        for ins in self.instructors:
            total_questions_answered += len(ins.questions_answered)
        return total_questions_answered

    def num_outstanding_questions(self):
        return self.get_num_questions_asked() - self.get_num_questions_answered()


class Members():

    def __init__(self, name, hair_color, birthdate):
        self.name = name
        self.hair_color = hair_color
        self.birthdate = birthdate
        self.questions_asked = []
        self.lines_of_code = []
        self.num_lines_coded = 0
        self.coding_level = 'beginner'

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def add_coded_line(self, line_of_code):
        self.lines_of_code.append(line_of_code)
        self.num_lines_coded += 1
        self.get_coding_level()

    def get_coding_level(self):
        if self.num_lines_coded <= 100:
            self.coding_level = 'beginner'
        elif self.num_lines_coded <= 1000:
            self.coding_level = 'novice'
        elif self.num_lines_coded <= 10000:
            self.coding_level = 'intermediate'
        else:
            self.coding_level = 'master'
        return self.coding_level

class Instructor():

    def __init__(self, name):
        self.name = name
        self.questions_answered = []

    def add_question_answered(self, question):
        self.questions_answered.append(question)

if __name__ == '__main__':
    # Students
    # stacy = Members('Stacy', 'brown', '09/31/1978')
    # sean = Members('Sean', 'brown', '05/31/1987')
    # kevin = Members('Kevin', 'blond', '07/24/1986')
    # erin = Members('Erin', 'red', '02/05/1990')
    # claire = Members('Claire', 'black', '03/23/1984')

    # # Instructors
    # marshall = Instructor('Marshall')
    # taylor = Instructor('Taylor')

    # # Add questions asked
    # stacy.add_question_asked('Whats an object?')
    # sean.add_question_asked('why self again?')
    # kevin.add_question_asked('Init what?')
    # erin.add_question_asked('Why is this so hard?')
    # claire.add_question_asked('Whats python anyway?')

    # # Add coded lines
    # stacy.add_coded_line('if __name__ == __main__:')
    # sean.add_coded_line('if __name__ == __main__:')
    # kevin.add_coded_line('if __name__ == __main__:')
    # erin.add_coded_line('if __name__ == __main__:')
    # claire.add_coded_line('if __name__ == __main__:')

    # # Add questions answered
    # marshall.add_question_answered('Whats an object?')
    # taylor.add_question_answered('Why self again?')
    # marshall.add_question_answered('Why is this so hard?')

    # # Add all members and instructors to OurClass
    # members = [stacy, sean, kevin, erin, claire]
    # instructors = [marshall, taylor]
    # DSI = OurClass('DSI', 'platte', members=members, instructors=instructors)

    # # Print results
    # print('Class Name: {}'.format(DSI.name))
    # print('Class Location: {}'.format(DSI.location))
    # print('Class Size: {}'.format(DSI.size))
    # print('DSI members: {}'.format(DSI.get_member_names()))
    # print('Num Questions Asked: {}'.format(DSI.get_num_questions_asked()))
    # print('Num Lines Coded: {}'.format(DSI.get_num_lines_coded()))
    # print('Num Questions Answered: {}'.format(DSI.get_num_questions_answered()))
    # print('Num Outstanding Questions: {}'.format(DSI.num_outstanding_questions()))


    # Pizza
	sizes = [8, 12, 14]
	costs = [15, 20, 25]

	print('Best Priced Pie: {} inch'.format(pizza_func(sizes, costs)))
	print('\n')

	blue_pan = Pizza('Blue Pan')
	blue_pan.add_pie(8, 15)
	blue_pan.add_pie(12, 20)
	blue_pan.add_pie(14, 25)

	print('Restaurant: {}\nBest Priced Pie: {} inch'.format(blue_pan.name, blue_pan.best_price()))
	print('\n')
	
	denver_deep_dish = Pizza('Denver Deep Dish')
	denver_deep_dish.add_pie(12, 17)
	denver_deep_dish.add_pie(14, 22)
	denver_deep_dish.add_pie(16, 27)

	print('Restaurant: {}\nBest Priced Pie: {} inch'.format(denver_deep_dish.name, denver_deep_dish.best_price()))