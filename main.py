def encode(message):
    encoded_message =""
    i=0
    while(i<=len(message)-1):
        count = 1
        char = message[i]
    encoded_messageage= encoded_message+char+str(count)
    i = i+1 #i=+1
    return encoded_messageage
encoded_message= encode("AAAAAABBBBBB")
print(encoded_message)


