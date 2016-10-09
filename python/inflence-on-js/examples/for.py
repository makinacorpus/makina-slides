from listparam import ListParam

params = ListParam("one,two,three")

it = iter(params)
while True:
    try:
        param = next(it)
        print("One of its param is {}.".format(param))
    except StopIteration:
        break
