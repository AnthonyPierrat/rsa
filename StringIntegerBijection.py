"""
/**
 * Copyright (c) 2019 Hamza JAFFALI.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
"""

import math

class StringIntegerBijection():

    alphabet = list(".ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    def __init__(self, alphabet=None):
        """
        Set up alphabet.
        """
        self.base = len(self.alphabet)
        
    def compareTo(self,a, b):
        if (a == b):
            return 0
        if (a > b):
            return 1
        if (a < b):
            return -1
        
    def StringToInteger(self, message):
        upperMessage = message.upper()
        number = 0
        for i in range(len(upperMessage)):
            char = upperMessage[i]
            index = self.alphabet.index(char)
            number = number + math.pow(self.base, len(upperMessage)-1-i)*index
        return int(number)
    
    def IntegerToString(self, number):
        message = ""
        quotient = number // self.base
        remainder = number % self.base
        message = self.alphabet[remainder] + message
        
        while (self.compareTo(quotient, self.base) > 0):
            remainder = quotient % self.base
            quotient = quotient // self.base
            message = self.alphabet[remainder] + message;
        
        message = self.alphabet[quotient] + message
        
        return message