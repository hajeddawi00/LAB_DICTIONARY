#Q1 - Answer
phone_dict:dict = {
    "0568323222":"Amal",
    "0522222232":"Mohammed",
    "0532335983":"Khadijah",
    "0545341144":"Abdullah",
    "0545534556":"Rawan",
    "0560664566":"Faisal",
    "0567917077": "Layla"
}

user_input:str = input('Please Enter The Phone Number :')


def checks_phone (str):
    '''this method cheks if the user entered a valid number or not, then print owner name'''
    special_characters = "!@#$%^&*()_-+={[]}abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSSTUVWXZY"
    if any(char in special_characters for char in str):#Using any()
        print('This is invalid number')
    elif len(str)==10:
        if user_input in phone_dict:
            print('The Owner Is :',phone_dict[user_input])
        else:
            print('Sorry, the number is not found')
    else:
        print('This is invalid number')
    
checks_phone(user_input)
    
#Q2:Write a function that receives a list containing the following numbers :
givin_list:list = [5, 0, 34, 9, 0, 13, 8]

def rearrange_list(list):
    '''This method checks if there is a zero in the list and moves it to the end.'''
    zeros = list.count(0)  # Count the number of zeros in the list
    list = [x for x in list if x != 0]  # Remove zeros from the list (list comprehension.)
    list.extend([0] * zeros)  # Append zeros to the end
    print("The list after rearranging:", list)

rearrange_list(givin_list)

'''
def rearrange_list (list):
    #this method cheks if there a zero in the list and make it in the last
    for i in list:
        if i == 0:
            list_value = list.pop(i)
            print(list_value)
            print(list)
    
    list2 = [list_value,list_value]
    list.extend(list2)

    print("the list after arrange :",list)
'''