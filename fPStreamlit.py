import streamlit as st

def allPrimesUpTo(num):
    num = int(num)
    primesFound = [2]
    for number in range(3, num + 1):
        for items in primesFound:
            if number % items == 0:
                break
        else:
            primesFound.append(number)
    noDuplicateList = list(dict.fromkeys(primesFound))
    return st.code((noDuplicateList), wrap_lines=True)

with st.sidebar:
    st.subheader("About App:")
    st.text("This app was created by Cecilia F. as an extension of the Python Essentials LinkedIn Learning Course.")
    st.text("")
    st.markdown("*Important note: This calculator is not the most efficient, so please use ranges under 1 million.*")

st.subheader("Welcome!", divider='grey')
st.text("")
st.text("I am going to show you my method of finding all primes in a range of numbers, used in the calculator below. Lets get started!")
st.markdown("")
try:
    allPrimesUpTo(int(st.text_input("Find all the primes from 1 to ...")))
except TypeError:
    st.text("Ah oh! You tried to type in something that does not belong in the calculator (aka letters or a decimal value). Please try again.")
except ValueError:
    st.text("")
st.text("")
st.text("")


st.subheader("Background", divider='grey')
st.text("")
st.markdown("A common way to find primes is to take a number, say 6, and find what the square root equals. We through math logic that we only need to check 6 by numbers less than the square root. Since the square of 6 equals 2.44 repeating, we only need to divide against 2 to learn whether or not 6 is prime. Since we know that 6 divided 2 equals 3, we learn that 6 is not prime.")
st.markdown("")
st.markdown("**Don't get me wrong,** this is a great way to find primes, however when the numbers get super large, it becomes super inefficient. That is why I decide to approach the problem a differen way. Lets break it down my solution!")
st.markdown("")
st.text("")
st.text("")
st.subheader("Solution", divider='grey')
st.text("")
st.markdown("**1.** My program starts of with knowing that 2 is a prime number. Since the end goal is to produce a list of all primes within a range of numbers, we will store this in the list 'primesFound'.")
st.markdown("")
st.markdown("")
st.code('''
def all PrimesUpTo(num):
    primesFound = [2]

# Remember the user determines the range by inputing the end value
# User types in 1000, the range is 1 to 1000
''')
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("**2.** We have a for loop for all numbers in the range of 3 to num + 1. Notice the distinction betweem **numbers** and **num**. Remember **num** is what the **user types in**, we want all **number in the range** the user chooses to be cycled through. We start the range at 3 because we already know the 2 is a prime number. We add 1 to whatever the user input is because without it, the program will stop one number early.")
st.markdown("")
st.markdown("")
st.code('''
def allPrimesUpTo(num):
    primesFound = [2]
    for number in range(2, num + 1):''')
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("**3.** We have another for loop, this time for the items in primesFound. This for loop goes through all items in our list primesFound. This is important because (spolier alert) our list is going to grow. I will explain everything fully in a second.")
st.markdown("")
st.markdown("")
st.code('''
def allPrimesUpTo(num):
    primesFound = [2]
    for number in range(2, num + 1):
        for items in primesFound:''')
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("**4.** Now the magic happens. Our next line is if the reminder of number divided by items equals zero, then the break activates. In plain terms, if our number was 6 and the primes collect in our list are 2 and 3, we exit out of the current for loop (since 6 is divisible by both 2 and 3) and try the next number in the range.")
st.markdown("")
st.markdown("")
st.code('''
def allPrimesUpTo(num):
    primesFound = [2]
    for number in range(2, num + 1):
        for items in primesFound:
            if number % items == 0:
                break''')
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown('''**5.** 
Notice the identation of the else statement. This is important because if the **else statement** was inside the **for items loop**, **the program would never run** because of the **break statement in the if statement**. 

If the number is not divisible with any of the **items in the primesFound list**, then **the number is added to the primesFound list**. Say the number was 7 and the primesFound list had 2, 3, and 5 in it. We know since 7 is not divisible by 2, 3, and 5 **and** that the square root of 7 is less than 5, 7 must be a prime number. 

Since we know that if any number is not divisible by 2, 3, 5, and 7 is a prime number up to 121 and that the primesFound list will eventually have all of these values, we can ensure that all numbers up to 121 will be correctly sorted. Since more primes will be add to the list before 122, including 11, we can also infer that this algorthim will correctly sort prime numbers from non-prime numbers for all numbers.''')
st.markdown("")
st.markdown("")
st.code('''
def allPrimesUpTo(num):
    for number in range(3, num + 1):
        for items in primesFound:
            if number % items == 0:
                break
        else:
            primesFound.append(number)''')
st.text("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("**6.** The last piece to this puzzle is the storaging the list of **primesFound after dict.formkeys is performed**. This is important since the algorthim produces lots of duplicate values. The **dict.fromkeys removes any duplicate values** from the list primesFound and **storages it in noDuplicateList**. The return noDuplicateList **returns the noDuplicateList as the final result** of the function. This is the result that the user sees.")
st.markdown("")
st.markdown("")
st.code('''
def allPrimesUpTo(num):
    for number in range(2, num + 1):
        for items in primesFound:
            if number % items == 0:
                break
        else:
            primesfound.append(number)
    unique_list = list(dict.fromkeys(primesFound))
    return noDuplicateList''')
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
