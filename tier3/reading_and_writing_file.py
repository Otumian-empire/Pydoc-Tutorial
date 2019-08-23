# reading and writing to file

# # create a new file
# file_obj = open("tier3/new_file.txt", 'w+')

# content = """
# Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quod excepturi neque quos fugit at veritatis modi ad provident. Delectus expedita quibusdam, nisi inventore nam repudiandae possimus tempore nobis autem quo.
# Quos harum id accusantium cumque distinctio autem hic explicabo quae sunt. Numquam ea, ex illo repudiandae alias quam sapiente fugit, facere inventore laborum ducimus tenetur animi? Iste magni facere voluptas?
# Sint, eveniet? Mollitia architecto commodi voluptatem voluptatibus, aperiam, officia quisquam vel enim quas, possimus tempore ab animi eligendi repellat dignissimos perferendis eius asperiores repellendus voluptatum natus. Non expedita saepe incidunt.
# Hic aliquid optio maiores, ex incidunt debitis natus sit impedit possimus vero doloribus aspernatur, laudantium, obcaecati quas quos molestiae sapiente modi blanditiis! Adipisci odit itaque doloremque officiis. Nostrum, deleniti quae!
# Magni nam, optio impedit provident nisi commodi. Aut quia laborum debitis modi voluptas maiores sint, reprehenderit harum voluptatum rem corrupti deleniti excepturi nobis ducimus tempora doloribus repellat. Dolorum, illo porro. """

# file_obj.write(content)
# file_obj.close()

# print("file created")

# # append to the new file
# file_obj = open('tier3/new_file.txt', 'a+')

# new_content = """
# I am a newline
# """

# file_obj.write(new_content)
# file_obj.close()

# print("file closed after appending")

# # read from new file
# file_obj = open('tier3/new_file.txt', 'r+')

# old_content = file_obj.readlines()

# print(old_content)
# file_obj.close()
# print("file closed after reading")


# creating files using with


# create a new file
with open("tier3/new_with_file.txt", 'w+') as file_obj:

    content = """
    Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quod excepturi neque quos fugit at veritatis modi ad provident. Delectus expedita quibusdam, nisi inventore nam repudiandae possimus tempore nobis autem quo.
    Quos harum id accusantium cumque distinctio autem hic explicabo quae sunt. Numquam ea, ex illo repudiandae alias quam sapiente fugit, facere inventore laborum ducimus tenetur animi? Iste magni facere voluptas?
    Sint, eveniet? Mollitia architecto commodi voluptatem voluptatibus, aperiam, officia quisquam vel enim quas, possimus tempore ab animi eligendi repellat dignissimos perferendis eius asperiores repellendus voluptatum natus. Non expedita saepe incidunt.
    Hic aliquid optio maiores, ex incidunt debitis natus sit impedit possimus vero doloribus aspernatur, laudantium, obcaecati quas quos molestiae sapiente modi blanditiis! Adipisci odit itaque doloremque officiis. Nostrum, deleniti quae!
    Magni nam, optio impedit provident nisi commodi. Aut quia laborum debitis modi voluptas maiores sint, reprehenderit harum voluptatum rem corrupti deleniti excepturi nobis ducimus tempora doloribus repellat. Dolorum, illo porro. """

    file_obj.write(content)

    print("file created")


# append to the new file
with open("tier3/new_with_file.txt", 'a+') as file_obj:

    new_content = """I am a newline"""

    file_obj.write(new_content)

    print("file closed after appending")


# read from new file
with open("tier3/new_with_file.txt", 'r+') as file_obj:

    old_content = file_obj.readlines()

    print(old_content)

    print("file closed after reading")
