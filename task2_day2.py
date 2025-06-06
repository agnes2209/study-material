f = open("output.txt", "w")
print("Hello, file!", file=f)
f.close()

print("Task Done", flush=True)
