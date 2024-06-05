class Student:
    def hello(self):
        return print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        return print("Pick me!")

class ChattyStudent(Student):

    def hello(self):
        super().hello()
        return print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        for x in range(0, 10):
            super().raise_hand()



