class NationalPark:
    all= []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name

        # if hasattr(self, name):
        #     raise AttributeError('Cannot change name once set')
        # if not isinstance(name, str):
        #     raise TypeError('Name must be string')
        # if len(name) < 3:
        #     raise ValueError('Name must be 3 or more characters')
        # self._name = name
        
    def trips(self):
        # trip_list = []
        # for trip in Trip.all:
        #     if self == trip.national_park:
        #         trip_list.append(trip)
        # return len(trip_list)
        return [trip for trip in Trip.all if self == trip.national_park]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        return len(self.trips()) 

    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key=visitors.count)
        

        # visitor_list = {}
        # for park in self.all:
        #     for visitor in Visitor.all:
        #         visitor_list[visitor] = visitor.total_visits_at_park(park)
        #         # visitor_list.append(visitor.total_visits_at_park(park))
        # top_visitor = max(zip(visitor_list.values(), visitor_list.keys()))
        # if top_visitor[0] == 0:
        #     return top_visitor[0]
        # else:
        #     return top_visitor[1]


class Trip:
    all= []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date

    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
    

class Visitor:
    all= []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def trips(self):
        # Returns a list of all trips for that visitor
        # visitor_trips = []
        # for trip in Trip.all:
        #     if self == trip.visitor:
        #         visitor_trips.append(trip)
        # return visitor_trips
        return [trip for trip in Trip.all if self == trip.visitor]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        count = 0
        for trip in self.trips():
            if park == trip.national_park:
                count+= 1
        return count