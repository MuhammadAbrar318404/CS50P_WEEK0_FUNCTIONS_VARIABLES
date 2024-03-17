# Defining the main function
def main():
    string_input = input("Please Provide any text: ")
 # Calling the function convert 
    string_input = convert(string_input)
    print(string_input)

# Defining the convert function
def convert(string_input):
#Replacing the emoticon with emojis   
    string_input = string_input.replace(":)", "🙂")
    string_input = string_input.replace(":(", "🙁")
    return string_input

main()