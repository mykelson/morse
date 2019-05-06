class Solution:
    code = { 'A':'.-', 'B':'-...', 
            'C':'-.-.', 'D':'-..', 'E':'.', 
            'F':'..-.', 'G':'--.', 'H':'....', 
            'I':'..', 'J':'.---', 'K':'-.-', 
            'L':'.-..', 'M':'--', 'N':'-.', 
            'O':'---', 'P':'.--.', 'Q':'--.-', 
            'R':'.-.', 'S':'...', 'T':'-', 
            'U':'..-', 'V':'...-', 'W':'.--', 
            'X':'-..-', 'Y':'-.--', 'Z':'--..', 
            '1':'.----', '2':'..---', '3':'...--', 
            '4':'....-', '5':'.....', '6':'-....', 
            '7':'--...', '8':'---..', '9':'----.', 
            '0':'-----', ', ':'--..--', '.':'.-.-.-', 
            '?':'..--..', '/':'-..-.', '-':'-....-', 
            '(':'-.--.', ')':'-.--.-'
                }
    def run(self, morseToEnglish, textToTranslate):
        self.translatedText = ''
         
        if morseToEnglish is True:
            self.translatedText = self.decrypt_text(textToTranslate)
        else:
            self.translatedText = self.encrypt_text(textToTranslate)
        
        return self.translatedText

    def encrypt_text(self, message):
        if message == '':
            return 'Invalid Morse Code Or Spacing'
        
        message = message.upper()

        text = ''
        for letter in message:
            if letter != ' ':
                text += self.code[letter] + ' '
            else:
                text += '  '
        
        return text
    
    def decrypt_text(self, message):
        if message == '':
            return 'Invalid Morse Code Or Spacing'

        text = ''
        message += ' '
  
        citext = ""
        for letter in message: 
            # checks for space 
            if (letter != ' '): 
  
                # counter to keep track of space 
                i = 0
  
                # storing morse code of a single character 
                citext += letter
            else:
                # in case of space
                # if i = 1 that indicates a new character 
                i += 1
                if i == 1: 
  
                    # accessing the keys using their values (reverse of encryption) 
                    text += list(self.code.keys())[list(self.code.values()).index(citext)] 
                    citext = '' 
                # if i == 2 that indicates a new word 
                elif i == 3: 
                    # add space to separate words 
                    text += ' '
                
                if i > 3:
                    return 'Invalid Morse Code Or Spacing'

                text = text.lower()
        return text


def main():
    test = Solution()
    res = test.run(False,"The wizard quickly jinxed the gnomes before they vaporized.")
    print(res)

if __name__ == "__main__":
    main()