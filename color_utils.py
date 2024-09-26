from constants import MAJOR_COLORS, MINOR_COLORS

# Helper function to format color pairs as strings
def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'

# Function to validate index boundaries for major/minor colors
def validate_color_indexes(major_index, minor_index):
    if major_index >= len(MAJOR_COLORS):
        raise Exception('Major index out of range')
    if minor_index >= len(MINOR_COLORS):
        raise Exception('Minor index out of range')

# Function to retrieve major and minor color based on pair number
def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    validate_color_indexes(major_index, minor_index)
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

# Helper function to get index of color, or raise an exception
def get_index_or_raise(color, color_list, color_type):
    try:
        return color_list.index(color)
    except ValueError:
        raise Exception(f'{color_type} color "{color}" not found')

# Function to find pair number from major and minor color names
def get_pair_number_from_color(major_color, minor_color):
    major_index = get_index_or_raise(major_color, MAJOR_COLORS, 'Major')
    minor_index = get_index_or_raise(minor_color, MINOR_COLORS, 'Minor')
    return major_index * len(MINOR_COLORS) + minor_index + 1
