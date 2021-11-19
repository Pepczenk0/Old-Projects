class Write:
    def write(self,pw):
        file = open("CONTENTS\RANDOMPW.txt", 'w')
        file.write("RANDOM PASSWORD: " + pw)
        file.close()