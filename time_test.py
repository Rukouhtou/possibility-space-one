import time, datetime

t = time.asctime()
t2 = time.localtime()
print(t)
print(t2)

t3 = datetime.datetime.now()
print(t3)

t3 = time.time()
print(t3)

# pull = fetch + merge

# Pull before commit, push
# merge branch will be created by Git if you wont pull other worker's version
# the reason for making merge branch is for keeping data.
