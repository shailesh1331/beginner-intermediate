# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
import pandas
data=pandas.read_csv('nato_phonetic_alphabet.csv')
content=pandas.DataFrame(data)
list={row.letter:row.code for _,row in content.iterrows()}
print(list)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_word():
    phonetic_code = []
    user=input("Enter your word")
    try:
        words=[letter.capitalize() for letter in user]
        for word in words:
            for (key,value) in list.items():
                if key==word:
                    phonetic_code.append(f'{key}:{value}')
        if phonetic_code==[]:
            raise TypeError
    except TypeError:
        print('Type error: Only letters allowed!')
    else:
        print(phonetic_code)

generate_word()