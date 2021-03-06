#--------|---------|---------|---------|---------|---------|---------|---------
# Advanced Challenge: Matching Makes & Models

# make_id, make_name
makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)

# model_id, model_name, make_name
models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

#  color_id, color_name
colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

#  model_id, color_id
available_car_colors = (
  (1, 1), (1, 2), (1, 7), 
  (2, 1), (2, 3), (2, 7), 
  (3, 2), (3, 3), (3, 7), 
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8), 
  (6, 2), (6, 6), (6, 7), 
  (7, 1), (7, 3), (7, 7), 
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7), 
  (10, 2), (10, 5), (10, 7), 
  (11, 3), (11, 6), (11, 8), 
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8), 
  (14, 2), (14, 5), (14, 8), 
  (15, 1), (15, 4), (15, 7)
)

## Overview

# This is an advanced challenge because it requires multiple layers of iteration. It is also an introduction to database relationships because there are four unique collections that are all related to each other.

# In the `makes` and `colors` collections, each item has a numeric identifier, and then a string representation.

# In the `models` collection, each item also has a numeric identifier, but also stores the numeric identifier of a model

##### Example

# Finally, the `available_car_colors` collection is storing the relationships between items in two foreign collections. The first number represents the corresponding model, and the second number represents the corresponding color.

## Instructions

### Part I: Reporting Object

report_dict = dict()

for make in makes:
    report_dict[make[1]] = dict()
    for model in models:
        color_list = []
        if make[0] == model[2]:
            for color in colors:
                for c in available_car_colors:
                    if c[1] == color[0] and c[0] == model[0]:
                        color_list.append(color[1])
            report_dict[make[1]][model[1]] = color_list

# print("car report 1")
# print(report_dict)
report_dict2 = {make[1]: {
    model[1]: [
        color[1] for color in colors
        for c in available_car_colors if c[1] == color[0] and c[0] == model[0]
    ] for model in models if model[2] == make[0]
} for make in makes}

# print("car report 2")
# print(report_dict2)

# You must first build a new dictionary that follows the format below. 

# 1. Each key in the dictionary should be the name of a make, and its value will be a dictionary.
# 1. The keys in the make dictionary will be the models, and the value will be a list of colors in which that the model is available.

# {
#     'Toyota': {
#       'Prius': ['Charcoal', 'Brick', 'Ivory'],
#       'Camry': ['Black', 'Red', 'White']
#     },
#     'Nissan': {
#       'Sentra': ['Charcoal', 'Blue', 'Ivory'], 
#       'Altima': ['Black', 'Charcoal', 'White'], 
#       'Xterra': ['Charcoal', 'Navy', 'Ivory']
#     },
#     'Mini': {
#       'Countryman': ['Charcoal', 'Navy', 'White'],
#       'Cooper': ['Red', 'Navy', 'Ivory']
#     }, 
#     'Ford': {
#       'F150': ['Black', 'Blue', 'Ivory'],
#       'Thunderbird': ['Black', 'Red', 'White']
#     }, 
#     'Honda': {
#       'Civic': ['Black', 'Navy', 'White'], 
#       'Pilot': ['Black', 'Brick', 'White'], 
#       'Accord': ['Red', 'Blue', 'Ivory']
#     }, 
#     'Dodge': {
#       'Ram': ['Charcoal', 'Blue', 'White'], 
#       'Charger': ['Black', 'Brick', 'White'], 
#       'Dart': ['Charcoal', 'Red', 'White']
#     }
# }

### Part II - Command Line Report
# print('Final Report 1 -- Using For loops')
# for make_name, model in report_dict.items():
#     print('{0}\n--------------------'.format(make_name))
#     for model_name, colors in model.items():
#         print('{0} available in: {1}, {2}, and {3}'.format(
#           model_name, colors[0], colors[1], colors[2]))
#     print('')

print('Final Report 2 -- Using Comprehension')
for make_name, model in report_dict2.items():
    print('{0}\n--------------------'.format(make_name))
    for model_name, colors in model.items():
        print('{0} available in: {1}, {2}, and {3}'.format(
          model_name, colors[0], colors[1], colors[2]))
    print('')

# Output a report on the command line that looks like this.

# Ford
# ------------------
# F150 available in Black, Blue, Ivory
# Thunderbird available in Black, Red, White

# etc...

# Black Hat Hacker Challenge

# Rewrite your nested `for` loops as nested comprehensions.

[print('\n' + make_name + '\n-----------------------------\n' + "{0} available in {1}, {2}, and {3}".format(model, *model_name[model]) for model in model_name for make_name, model_name in report_dict2.items())]
  # print('\n' + k + '\n-----------------------------')
  # for model in v:
    # print("{0} available in {1}".format(model, ', '.join(v[model])))