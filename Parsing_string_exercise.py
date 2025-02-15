# Use find and string slicing to extract the portion of
# the string after the colon character and
# then use the float function to convert
# the extracted string into a floating point number.
#
# custom_string = 'X-MAPDS-Confidence:0.8475'


custom_string = 'X-MAPDS-Confidence:0.8475'
index = custom_string.find(':')
print(index)

domain = custom_string[index + 1 : ]
print(domain)
convert = float(domain)
print(convert)
