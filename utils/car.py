class Car(object):
    model = ''
    max_speed = 0
    drag_coef = 0.
    time_to_max = 0

    def __init__(self, model, max_speed, drag_coef, time_to_max):
        self.model = model
        self.max_speed = max_speed
        self.drag_coef = drag_coef
        self.time_to_max = time_to_max
