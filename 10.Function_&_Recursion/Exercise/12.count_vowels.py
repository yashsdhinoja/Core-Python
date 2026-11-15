def count_vowels(text):
    vowels = 'aeiouAEIOUS'
    count = 0

    for i in text:
        if i in vowels:
            count =+ 1

    return count

print(count_vowels("Hello World"))