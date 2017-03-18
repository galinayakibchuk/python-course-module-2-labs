"""
create dict with 5 items, where keys will be country name and value -
domain name, i.e. {Ukraine:UA}
"""
country = {'Ukraine': 'UA',
           'Italy': 'IT',
           'Germany': 'GER',
           'Sweden': 'SW',
           'France': 'FR'}

"""
create another dict with 5 items, where values of countries will be keys,
and values will be the capitals
"""
capital = {'UA': 'Kiev',
            'IT': 'Rome',
            'GER': 'Berlin',
            'SW': 'Stokholm',
            'FR': 'Paris'
}
"""
add one more element to each dict above
"""
country.update({'Australian':'AU'})
capital.update({'AU':'Sydney'})

"""
print sentence "Domain for COUNTRY is DOMAIN." for each record in countries
with the replace from
"""
for key, value in country.items():
    print("Domain for {} is {}.".format(key, value))

"""
print sentence "The capital of COUNTRY is CAPITAL"
for each record in capitals with the replace from
"""
for key, value in capital.items():
    print("The capital of {} is {}.".format(key,value))

"""
Merge sentences above together with one cycle
"""
for key, value in country.items():
    print("Domain for {} is {}.The capital is{}".format(key,value,capital[value]))

"""
Add to each value of first dict another two domains: COM and GOV
"""
for key,value in country.items():
    country[key] = [value, 'COM', 'GOV']

for key, value in country.items():
    print("Domain for {} is {}.The capital is {}".
          format(key,value,capital[value[0]]))
