import hashlib, time, sys


input_hash = sys.argv[1]
start = time.time()
password_list = [x for x in open(sys.argv[2], "r").readlines()]
salt = "slayer"
count = 1

for x in range(len(password_list)):
    guess = str(password_list[x]).strip('\n')
    hashedGuess = str(hashlib.sha1(guess).hexdigest())


    if input_hash == hashedGuess :
        end = time.time()
        print("The password is " + str(guess))
        print("Guesses: "+ count)
        print("Time elapsed: "+ end-start)
        quit()
    else: count += 1

for x in range(len(password_list)):
    guess = str(password_list[x]).strip('\n')
    saltedguess = salt+guess
    hashedGuess = str(hashlib.sha1(saltedguess).hexdigest())

    # print(saltedguess)

    if input_hash == hashedGuess :
        end = time.time()
        print("The password is ", str(guess))
        print("Guesses: ", count)
        print("Time elapsed: " , end-start)
        quit()
    else: count += 1

print("Password not found\n")
