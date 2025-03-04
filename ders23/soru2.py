# "secret.txt" adlı bir dosyayı açmaya çalışan bir Python programı yazın. Eğer dosya mevcut değilse, dosyayı oluşturun ve içine "Top Secret" yazın.
# Ancak, program aşağıdaki durumları da ele almalıdır:

# Eğer dosya mevcut ise, içeriğini okuyun ve yazdırın.

# Eğer dosya mevcut ancak boş ise, "File is empty!" mesajıyla özel bir istisna (exception) fırlatın.

# Bilinmeyen bir hata oluşursa, bu hatayı yakalayın ve "An unexpected error occurred!" mesajını yazdırın.

# -----------------------------------


class EmptyFileError(Exception):
    pass  # Custom exception for empty files


try:
    with open("secret.txt", "r") as file:
        content = file.read()
        if not content:
            raise EmptyFileError("File is empty!")
        print("File Content:", content)
except FileNotFoundError:
    with open("secret.txt", "w") as file:
        file.write("Top Secret")
    print("File did not exist. 'secret.txt' created with content: 'Top Secret'.")
except EmptyFileError as e:
    print(e)
except Exception:
    print("An unexpected error occurred!")
