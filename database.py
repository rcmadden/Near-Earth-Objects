"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""
from datetime import datetime

class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos 
        self._approaches = approaches 

        # Link together the NEOs and their close approaches.
        for x in range(len(self._approaches)):
            for i in range(len(self._neos)):
                if self._neos[i].designation == self._approaches[x]._designation:
                    self._neos[i].approaches.append(self._approaches[x])
                    self._approaches[x].neo = self._neos[i]


    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        # Fetch an NEO by its primary designation.
        neo_by_designation = ''
        
        for i in range(len(self._neos)):
            if self._neos[i].designation == designation:
                neo_by_designation = self._neos[i]

        if neo_by_designation=='' or neo_by_designation == None:
           return None

        return neo_by_designation
        

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """

        
        # Fetch an NEO by its name.
        neo_by_name = ''
        for i in range(len(self._neos)):
            if self._neos[i].name == name:
                neo_by_name = self._neos[i]
       
        if neo_by_name=='' or neo_by_name == None:
           return None
            
        return neo_by_name    

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaningfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        # ELABORATE: Generate `CloseApproach` objects that match all of the filters 
        self.filters = filters

        for approach in self._approaches:
            if self.filters['date'] and self.filters['date'] != datetime.date(approach.time):
                continue
            if self.filters['start_date'] and not (self.filters['start_date'] <= datetime.date(approach.time)):
                continue            
            if self.filters['end_date'] and not (self.filters['end_date'] >= datetime.date(approach.time)):
                continue 
            if self.filters['distance_min'] and not self.filters['distance_min'] <= float(approach.distance):
                continue
            if self.filters['distance_max'] and not self.filters['distance_max'] >= float(approach.distance):
                continue
            if self.filters['velocity_min'] and not self.filters['velocity_min'] <= float(approach.velocity):
                continue
            if self.filters['velocity_max'] and not self.filters['velocity_max'] >= float(approach.velocity):
                continue 
            if self.filters['diameter_min'] and approach.neo.diameter != '':
                if not (self.filters['diameter_min'] <= float(approach.neo.diameter)):
                    continue  
            if self.filters['diameter_max'] and approach.neo.diameter != '':
                if not (self.filters['diameter_max'] >= float(approach.neo.diameter)):
                    continue  
            if self.filters.get('hazardous')==True and not approach.neo.hazardous == True:
                continue  
            if self.filters.get('hazardous')==False and not approach.neo.hazardous == False:
                continue   
            
            yield approach
