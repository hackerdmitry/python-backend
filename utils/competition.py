from random import randint


class Competition(object):
    _created = 0

    def __init__(self, competitors, weather):
        self.competitors = competitors
        self.weather = weather

    def __new__(cls, *args, **kwargs):
        Competition._created += 1
        if Competition._created < 2:
            return super(Competition, cls).__new__(cls)

    def start(self, distance):
        for competitor in self.competitors:
            competitor_time = 0

            for distance in range(distance):
                _wind_speed = randint(0, self.weather.wind_speed)

                if competitor_time == 0:
                    _speed = 1
                else:
                    _speed = (competitor_time / competitor.time_to_max) * competitor.max_speed
                    if _speed > _wind_speed:
                        _speed -= (competitor.drag_coef * _wind_speed)

                competitor_time += float(1) / _speed

            print("Car <%s> result: %f" % (competitor.model, competitor_time))
