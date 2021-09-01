def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result = result + word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Douglas Carvalho Pereira")) # Should be: OS