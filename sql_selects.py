def select_all_columns_and_rows():
# should return all of the data featured in the planets table

    return "SELECT * FROM planets"

def select_name_and_color_of_all_planets():
# should return the name and color of each planet
    return "SELECT name,color FROM planets"

def select_all_planets_with_mass_greater_than_one():
# should return all columns for each planet whose mass is greater than 1.00
    return "SELECT * FROM planets WHERE mass > 1.00"

def select_name_and_mass_of_planets_with_mass_less_than_equal_to_one():
# should return the name
#and mass of each planet whose mass is less than or equal to 1.00
    return "SELECT name,mass FROM planets WHERE mass <= 1.00"

def select_name_and_color_of_planets_with_more_than_10_moons():
# should return the name and color of each planets that has more than 10 moons
    return "SELECT name,color FROM planets WHERE num_of_moons > 10"

def select_all_planets_with_moons_and_mass_less_than_one():
# should return the planet that has at least one moon and a mass less than 1.00
    return "SELECT * FROM planets WHERE num_of_moons >= 1 AND mass < 1.00"

def select_name_and_color_of_all_blue_planets():
# should return the name and color of planets that have a
#color of blue, light blue, or dark blue
    return "SELECT name,color FROM planets WHERE color = 'blue'OR color = 'light blue' OR color = 'dark blue'"
