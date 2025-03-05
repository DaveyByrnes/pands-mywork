# test while
# part of week 04 lecture
# author: it is me

count = 0
while count < 10:
    print("count is", count)
    count += 1

print("The final count is ", count)

count = 10
while count >= 0:
    print("Countdown", count)
    count -= 1
print("Blast off!")

# sentinel controlled loop

val = input("type something(q to quit): ")
while val != 'q':
    print("Hi mom")
    val = input("q to quit: ")

print("all done")