Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> CSE=["girls","boys","students"]
>>> CSEC=[]
>>> CSEC=CSE.copy()
>>> print(CSEC)
['girls', 'boys', 'students']
>>> list=[1,2,4,5,9,10]
>>> print(min(list))
1
>>> print(max(list))
10
>>> #List Comprehension:
>>> given_list=[X for X in range(5)]
>>> print(given_list)
[0, 1, 2, 3, 4]
>>> new_list=[var+3 for var in given_list]
>>> print(new_list)
[3, 4, 5, 6, 7]
>>> #Dictionary comprehension:
>>> given_list=[X for X in range(5)]
>>> print(given_list)
[0, 1, 2, 3, 4]
>>> new_list={var:var+3 for var in given_list}
print(new_list)
{0: 3, 1: 4, 2: 5, 3: 6, 4: 7}
#Set comprehension:
given_list={X for X in range(5)}
print(given_list)
{0, 1, 2, 3, 4}
new_list={var+3 for var in given_list}
print(new_list)
{3, 4, 5, 6, 7}
#Generator comprehension:
