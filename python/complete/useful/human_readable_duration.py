import warnings
#This is a challenge from codewats, but as long as the stuff i made here
# is useful in other situations i adapted it to be useful.
# aniway a part of this code is commented as any other challenge.  


#Your task in order to complete this Kata is to write a function 
# which formats a duration, given as a number of seconds, in a 
# human-friendly way.

#The function must accept a non-negative integer. If it is zero, 
# it just returns "now". Otherwise, the duration is expressed as a 
# combination of years, days, hours, minutes and seconds.

#It is much easier to understand with an example:
#   format_duration(62)    # returns "1 minute and 2 seconds"
#   format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
#   For the purpose of this Kata, a year is 365 days and a day is 24 hours.
#Note that spaces are important.

class useful1_greedy:
    """Some useful functions"""
    def __init__(self):
        pass
#First and last attempt, essencially because is a huge amount of code and i
# don't wanto to optimize it, aniway, the efficienci is pretty good,
# but i think that's more an achivement of the problem itself than mi own
# coding ability.
#O(Constant) (yeah boy constant big O, i thought)
    def convert_two_lists_into_dict(self, keys, values):
        """ Returns the list merged into a dict 

            Parameters:
                keys (list): the keys of the dict
                values (list): the values of the dict

            returns:
                dict: with keys as keys and values as values
        """
        #Raising a warning if the length of the keys and the length of the 
        # values are not equal, see that it will not raise an error, only 
        # will raise a warning and delete the extra values, or set the 
        # extra keys with 0's.  
        if len(keys) != len(values):
            warnings.warn("the length of keys and values are different")
            if len(keys) > len(values):
                for i in range(len(keys) - len(values)):
                    values.append(0)

        #Merging both list, keys and values into a dict
        new_dict = {}
        for key in keys:
            for value in values:
                new_dict[key] = value
                values.remove(value)
                break
    
        return new_dict


    def find_latest_and_penultimate_values(self, quantities):
        """ Returns the latest and penultimate values of a list bigger than 0
            
            Parameters:
                quantites (list/dict): the list where find the latest and penultimate

            Returns:
                tuple: containing latest and penultimate, in this order.
            """
        
        #Verifying that quantities is a list, turning it into a list if it is
        # a list 
        if type(quantities) == dict:
            quantities = [i for i in quantities.values()]
    
        #Finding the latest value bigger to 0.
        latest = None
        penultimate = None
        for ind, value in enumerate(quantities):
            if value > 0:
                latest = ind
    
        #Finding the penultimate values bigger than 0.
        quantities_minus_last = quantities[:latest]
        for ind,value in enumerate(quantities_minus_last):
            if value > 0:
                penultimate = ind

        return (latest, penultimate)


#In this secondary function we are, printing the data in a human readable way
    def natural_printing_of_multiple_inputs(self, to_print, values = None, lenguage = "en"):
        """ Returns a human readable string, printing each values bigger to 0
        
            Parameters:
                to_print (list / dict): if list, the names to print, if dict both,
                    names and values.
                values (list): the values of every name, only if to_print is 
                    list. (default = None)
                lengauge (str): defines the lengauge, currently only available 
                    in english (en) and spanish (es). (default = en)
            
            Returns:
                string: a human readable string reperesenting the input data.

            Raises:
                ValueError: if lenguage is different of en/es
                AttributeError: if values error is not defined when to_print is a list.
                TypeError: if introduced another type in to_print different of list/dict
        """
        #In this part of the code qe are changing the lenguage between english and
        # spanish by only changing the conector, and raising a ValueError if the
        # specified lenguage is different of suported lengauges.  
        if lenguage == "en":
            conector = "and"
        elif lenguage == "es":
            conector = "y"
        else:
            raise ValueError(f"lenguage should be en or es, you introduced {lenguage}")

        #Changing the mode depending of the type of the input and verifying
        # that every si fine. 
        if type(to_print) == dict:
            mode = "dict"
        elif type(to_print) == list and values != None:
            mode = "lists"
        else:
            if values == None:
                raise AttributeError("if to_print is list yo have to define values")
            else:
                raise TypeError(f"to_print should be list or dict, istead you give a {type(list_0_or_dict)}")
        
        #Defining the functiong using lists. both finctions works 
        # similar so i will explin the functing only in this. 
        if mode == "lists":
            #Using the function find_latest_and_penultimate to search the 
            # latest and penultimate value different to 0
            latest_index, penultimate_index = self.find_latest_and_penultimate_values(values)
            final = ""
            
            for ind, unit, value in zip(range(to_print), to_print, values):
                #If we are in the latest pair value/unit printing the 
                # conector between the penultimate and the latest.
                if ind == latest_index and penultimate_index != None:
                    final += " " + conector 
                
                if value > 0:
                    #Adding to a single string the values and the units 
                    # if the values are bigger than 0
                    final += f" {value} {unit}"
                    
                    if values != 1:
                        final += "s"
                    
                    #If the string  is not the latest or the penultimate 
                    # adding a coma between the courrent pair value/unit 
                    # and the next one
                    if ind != penultimate_index and i != latest_index:
                        final += ","

        #Here the same but using dicts.
        elif mode == "dict":
            latest_index, penultimate_index = self.find_latest_and_penultimate_values(to_print)
            final = ""
            #Instead of using to_print as keys and values as values we iterate
            # over dict.keys() and dict.values(). 
            for ind, key, value in zip(range(len(to_print)), to_print.keys(), to_print.values()):
                if ind == latest_index and penultimate_index != None:
                    final += " " + conector
                if value > 0:
                    final += f" {value} {key}"
                    if value != 1:
                        final += "s"
                    if ind != penultimate_index and ind != latest_index:
                        final += ","

        #Finally we return the final string striping the spaces on the sides.
        return final.strip()   





    def greedy_algorithm(self, units, equivalences, units_names = None, human_readable = False):
        """ Returns the optimal distribution of the given units in the packages, 
            giving the least quantitie of packages possible evaluating her capacity.

            
            Parameters:
            units (int): the units to distribute
            equivalences (dict or list): packages names in keys if dict, and package 
                capacity in values or list
            units_names (list): if equivalence is a dict you include package names 
                here. (default = None)
            human_readable (bool): defines if return the raw data or a human readable
                string. (default = False) 
                
            Returns:
                if human_readable = False return a dict, containing the package
                    names as keys and the quantites as values.
                if human_readable = True return a str, containing a enumeration
                    of the package and their quantities in a human readable way.
            
            Raises:
                ValueError: if the units are smaller than 0.
            """
        
        #Verifying that units is bigger than 0.
        if units < 0:
            raise ValueError ("units must be positive")

        #Changing data types to adjust to the next algorithm.
        if type(equivalences) == dict:
            units_names = list(equivalences.keys())
        elif type(equivalences) == list:
            equivalences = self.convert_two_lists_into_dict(units_names, equivalences)
        
        #Finding the best distribution of units.
        quantitites = []
        units_remaining = units 
        for equivalence in equivalences.values():
            quantitite = units_remaining // equivalence
            units_remaining = units_remaining - equivalence * quantitite
            quantitites.append(quantitite)
        quantitites.append(units_remaining)

        #Transforming the result into a dict, and transforming it into a
        # human readable string if user specefied.
        result = self.convert_two_lists_into_dict(units_names, quantitites)
        if human_readable:
            result = self.natural_printing_of_multiple_inputs(result)
        
        return result

if __name__ == "__main__":
    #print(format_duration(0))
    """ print(format_duration(62))
    print(format_duration(120))
    print(format_duration(3600))
    print(format_duration(3662))
     """