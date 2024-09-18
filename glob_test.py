import glob
Results = glob.glob("*.py")

print(f"There are {len(Results)} of python files in the practice folder.\n")
for index, file in enumerate(Results):
    print(f"{index+1}-{file}")