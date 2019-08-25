# Brief Tour of the Standard Library
# os
import os

print(f"The current working directory: {os.getcwd()}")
os.chdir('tier5')
print(f"Changed directory into directory: {os.getcwd()}")
os.chdir('../')
print(f"Now the current working directory: {os.getcwd()}")

# ls, create a file with touch, add text and echo the text from the file
# ls again
os.system('ls')  # execute cmds in a subshell
os.system("touch ossystem")
os.system("echo 'haha' >> ossystem")
os.system("cat ossystem")
os.system('ls')

# os as open() which there is open also one for opening of files
# avoid `import os *`