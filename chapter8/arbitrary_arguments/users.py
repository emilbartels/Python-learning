import profilebuilder as pb
from profilebuilder import build_profile as bp

user_profile = pb.build_profile(
    'emil',
    'Sørensen',
    hobby='Running',
    girlfriend='Liv'
)

print(f'\nHere is information about Emil: \n')
for key, value in user_profile.items():
    print(f'{key.capitalize()}: {value.capitalize()}')



user_profile = bp(
    'emil',
    'Sørensen',
    hobby='Running',
    girlfriend='Liv'
)

print(f'\nHere is information about Emil: \n')
for key, value in user_profile.items():
    print(f'{key.capitalize()}: {value.capitalize()}')

