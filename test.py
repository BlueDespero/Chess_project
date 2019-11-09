import multiprocessing as mp

output = mp.Queue()

def prime_test(number, output):
    czy = 1
    for i in range(2,number):
        if number%i == 0:
            czy = 0

    if czy == 1:
        output.put("TAK")
    else:
        output.put("NIE")

processes = [mp.Process(target = prime_test, args = (179426549, output)) for x in range(4)]
for p in processes:
    p.start()

for p in processes:
    p.join()

results = [output.get() for p in processes]
print(results)
