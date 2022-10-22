__author__ = 'Martinskole'
# -*- coding: utf-8 -*-
from sys import exit
from collections import deque

class invalidInput( Exception ):
    """
    Raises an error if the user inputs an invalid entry.
    """

    def __init__( self, message ):
        self.message = message

    def __str__( self ):
        return str( self.message )


class RotorData( object ):
    """
    Contains the information used in the acutal Enigma Machine.
    """

    # set lettercase to uppercase letters
    lettercase = 65

    def __init__( self ):

        # source:
        # http://users.telenet.be/d.rijmenants/en/enigmatech.htm

        # Rotors
        self.rotor1Str = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        self.rotor2Str = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
        self.rotor3Str = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        self.rotor4Str = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
        self.rotor5Str = 'VZBRGITYUPSDNHLXAWMJQOFECK'
        self.rotor6Str = 'JPGVOUMFYQBENHZRDKASXLICTW'
        self.rotor7Str = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'
        self.rotor8Str = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'
        self.BetaStr   = 'LEYJVCNIXWPBQMDRTAKZGFUHOS'
        self.GammaStr  = 'FSOKANUERHMBTIYCWLQPZXVGJD'

        # Reflectors
        self.reflAStr  = 'EJMZALYXVBWFCRQUONTSPIKHGD'
        self.reflBStr  = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        self.reflCStr  = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

        # Convert Strings to deque objects and convert the strings to Numbers
        self.rotor1 = self.convertLettersToNumbers( deque( self.rotor1Str ) )
        self.rotor2 = self.convertLettersToNumbers( deque( self.rotor2Str ) )
        self.rotor3 = self.convertLettersToNumbers( deque( self.rotor3Str ) )
        self.rotor4 = self.convertLettersToNumbers( deque( self.rotor4Str ) )
        self.rotor5 = self.convertLettersToNumbers( deque( self.rotor5Str ) )
        self.rotor6 = self.convertLettersToNumbers( deque( self.rotor6Str ) )
        self.rotor7 = self.convertLettersToNumbers( deque( self.rotor7Str ) )
        self.rotor8 = self.convertLettersToNumbers( deque( self.rotor8Str ) )
        self.Beta   = self.convertLettersToNumbers( deque( self.BetaStr ) )
        self.Gamma  = self.convertLettersToNumbers( deque( self.GammaStr ) )
        self.reflA  = self.convertLettersToNumbers( deque( self.reflAStr ) )
        self.reflB  = self.convertLettersToNumbers( deque( self.reflBStr ) )

        # Define an alphabet
        self.alphaRange  = tuple( range ( 26 ) )
        self.alphabet    = self.convertNumbersToLetters( self.alphaRange )
        self.alphabetNum = self.convertLettersToNumbers( self.alphabet )

    def convertLettersToNumbers( self, letters ):
        """
        Converts a tuple of capital letters to numbers.
        """

        numbers = deque()

        for letter in letters:
            numbers.append( int( ord( letter ) ) - RotorData.lettercase )
        return numbers

    def convertNumbersToLetters( self, numbers ):
        """
        Converts a tuple of numbers to capital letters.
        """

        letters = deque()

        for number in numbers:
            letters.append( chr( number + RotorData.lettercase ) )
        return letters

    def convertLetterToNumber( self, letter ):
        """
        Converts a single uppercase letter to a number. E.g, 'A' --> 65
        """

        return int( ord ( letter.upper() ) ) - RotorData.lettercase

    def convertNumberToLetter( self, number ):
        """
        Converts a tuple of numbers to capital letters.
        """

        return chr( number + RotorData.lettercase )


class Plugboard( RotorData ):

    def __init__( self ):
        RotorData.__init__( self )
        self.board = range( 26 )
        self.connections = []

    def makeConnections( self, fromWhatLetter, toWhatLetter ):
        """
        Connects a plug fromWhatLetter toWhatLetter.
        """

        # Test input to ensure a valid entry else raise an invalidInput error
        if fromWhatLetter.upper() not in self.alphabet or toWhatLetter.upper() not in self.alphabet:
            raise invalidInput( "Letter must be between 'A' and 'Z'" )

        # store the alpha format of the letters
        firstLetter  = fromWhatLetter.upper()
        secondLetter = toWhatLetter.upper()

        # receives two letters and converts then to integers
        fromWhatLetter = self.convertLetterToNumber( fromWhatLetter.upper() )
        toWhatLetter   = self.convertLetterToNumber( toWhatLetter.upper() )

        # check to make sure not trying to put a plug where one already exists
        if self.isPlugEmpty( fromWhatLetter, toWhatLetter ):

            # Plugboard is symmetrical
            self.board[fromWhatLetter] = toWhatLetter
            self.board[toWhatLetter] = fromWhatLetter
            steckerPair = (firstLetter, secondLetter)
            self.connections.append(steckerPair)

    def isPlugEmpty( self, firstNumberToCheck, secondNumberToCheck ):
        """
        Returns True if NumberToCheck is an empty plug otherwise False.
        """

        # syntactic sugar
        indexOfFirstNumber = self.board.index( firstNumberToCheck )
        indexOfSecondNumber = self.board.index( secondNumberToCheck )

        if indexOfFirstNumber == firstNumberToCheck and indexOfSecondNumber == secondNumberToCheck:
            return True
        else:
            return False

    def getPlugBoard( self ):
        """
        Returns the plugboard.
        """

        return self.board


class Rotor( RotorData ):
    """
    Contains attributes and methods that relate to an Enigma rotor.
    """

    def __init__( self, name, wheel ):
        RotorData.__init__( self )
        self.name = name
        self.wheel = wheel
        self.iWheel = self.inverseWheel()
        self.notchSettings = ()
        self.position = deque( range( 26 ) )
        self.outerRing = deque( range( 26 ) )
        self.entryContact = deque( range( 26 ) )
        self.ringSetting = 0

    def encode( self, plainTextNum ):
        """
        Converts plaintext to ciphertext. Returns cipherText.
        -param entryContact: the letter on the inner ring where the signal enters
        -param exitContact: the letter on the inner ring where the signal exits
         this is defined by the rotor. Note these are hard wired to the rotor.
         self.wheel is a list representing the rotor wiring.
        -param contactDifference: the difference between the exit letter and the
         entry letter
        -return cipherText: scrambled representation of plainText
        """

        # determine which contact the signal arrives at
        entryContact = self.entryContact[ plainTextNum ]

        # determine which contact the signal exits
        exitContact = self.wheel[ plainTextNum ]

        # determine the amount to shift the exit contact to determine
        # the exit position
        contactDifference = exitContact - entryContact
        cipherText = self.position[ ( plainTextNum + contactDifference ) % 26 ]

        return cipherText

    def iEncode( self, plainTextNum ):
        """
        Converts plaintext to ciphertext using the inverse of self.wheel.
        Returns cipherText.
        -param entryContact: the letter on the inner ring where the signal enters
        -param exitContact: the letter on the inner ring where the signal exits
         this is defined by the rotor. Note these are hard wired to the rotor.
         self.iWheel is a list representing the inverse of the rotor wiring.
        -param contactDifference: exitContact - entryContact
        -return cipherText: scrambled representation of plainText
        """

        # determine which contact the signal arrives at
        entryContact = self.entryContact[ plainTextNum ]

        # determine which contact the signal exits
        exitContact = self.iWheel[ plainTextNum ]

        # determine the amount to shift the exit contact to determine
        # the exit position
        contactDifference =  exitContact - entryContact
        cipherText = self.position[ ( plainTextNum + contactDifference ) % 26 ]

        return cipherText

    def inverseWheel( self ):
        """
        Returns the inverse of self.wheel.
        -param iWheel: a list containing the inverse of self.wheel
        -return iWheel as a deque object
        """

        wheel  = list( self.wheel )
        iWheel = [ 0 ] * len( wheel )

        # iWheel is the inverse of wheel
        for index, value in enumerate( wheel ):
            iWheel[ value ] = index

        return deque( iWheel )

    def setRingSetting( self, setRingToThisLetter = 'A' ):
        """
        Changes the position of the internal wiring relative to the rotor.
        Binds the outer ring and the inner ring together.
        """

        # Test input to ensure a valid entry else raise an invalidInput error
        if setRingToThisLetter not in self.alphabet:
            raise invalidInput( "RingSetting must be between 'A' and 'Z'" )

        setRingToThisNumber = self.convertLetterToNumber( setRingToThisLetter.upper() )

        self.ringSetting = setRingToThisNumber
        self.entryContact.rotate( setRingToThisNumber )
        self.wheel.rotate( setRingToThisNumber )
        self.iWheel.rotate( setRingToThisNumber )

    def stepRotor( self, numSteps ):
        """
        Steps the rotor numSteps.
        """

        self.outerRing.rotate( numSteps )
        self.entryContact.rotate( numSteps )
        self.iWheel.rotate( numSteps )
        self.wheel.rotate( numSteps )

    def setNotchPositions( self, *positions ):
        """
        Sets the 'physical' notch location on a rotor. This is the point where
        the rotor will turn the rotor to its left one notch. There can be
        more than one notch position on a rotor.
        -param notches: a tuple containing the numerical values of the notch
         settings
        -return self.notchSettings
        """

        # sets a default value if none given
        if not positions:
            positions = ( 'A', )

        notches = ()

        # Test input to ensure a valid entry else raise an invalidInput error
        for letter in positions:
            if letter not in self.alphabet:
                raise invalidInput( "Notch position must be between 'A' and 'Z'" )
            else:
                notches += ( self.convertLetterToNumber( letter.upper() ), )

        self.notchSettings = notches

    def getNotchSettings( self ):
        """
        Returns the current notchSettings.
        """

        return self.notchSettings

    def atTurnOverPosition( self ):
        """
        Returns True if ready to step rotor on the left.
        """

        if self.outerRing[ 0 ] in self.notchSettings:
            return True
        else:
            return False

    def getWheel( self ):
        """
        Returns the wheel.
        """

        return self.wheel

    def setLetterInWindow( self, shiftToThisLetter = 'A' ):
        """
        Sets the letter in the Enigma's window.
        """

        # test input to ensure a valid entry else raise an invalidInput error
        if shiftToThisLetter.upper() not in self.alphabet:
            raise invalidInput( "Letter in Window must be between 'A' and 'Z'" )

        shiftToThisNumber = self.convertLetterToNumber( shiftToThisLetter.upper() )

        # multiply by shiftDirection to make sure this is shifting the same
        # way as the rotor when stepped.
        shiftDirection = -1
        shiftToThisNumber = shiftDirection * shiftToThisNumber % 26
        self.outerRing.rotate( shiftToThisNumber )
        self.entryContact.rotate( shiftToThisNumber )
        self.wheel.rotate( shiftToThisNumber )
        self.iWheel.rotate( shiftToThisNumber )

    def __str__( self ):
        """
        String representation.
        """

        letter = self.convertNumberToLetter( self.outerRing[ 0 ] )
        return "The letter %s is in Rotor %s's window" % ( letter, self.name )


class Reflector( object ):
    """
    The Enigma's relfector.
    """

    def __init__( self, name, wheel ):
        self.name = name
        self.wheel = wheel

    def getReflector( self ):
        """
        Returns the reflector.
        """

        return self.wheel

    def setReflector( self ):
        """
        Sets the wiring of the reconfigurable relfector.
        """

        pass


class EnigmaMachine( object ):
    """
    Contains all the components of the Enigma Machine.
    """

    def __init__( self, reflector, plugboard, *rotors ):
        self.reflector = reflector
        self.plugboard = plugboard
        self.rotors = rotors
        self.numRotors = len( self.rotors )
        self.whichRotorsToShift = [ False ] * self.numRotors
        self.rotorData = RotorData()
        self.interval = 0

    def shiftRotors( self ):
        """
        Shifts rotors based on key strokes and notchSettings.
        """

        # Todo: Need to add the double step sequence

        # a +ive value shifts the rotors to the right, -ive to the left
        # Fact: Enigma shifted to the left (-1)
        numSteps = -1

        # shifts rotors as necessary
        try:
            for i in range( 0, self.howManyRotorsShift()+1 ):
                self.rotors[ i ].stepRotor( numSteps )

        except IndexError:
            pass

    def howManyRotorsShift( self ):
        """
        Determines which rotors should shift.
        -param countNumberOfTrue counts the number of trues in the
         self.whichRotorsToShift list
        -return countNumberOfTrue
        """

        # creates a list that contains whether each rotor is in its
        # turnOverPosition. [True, False, False, False] for 4 rotors.
        # This indicates that Rotor 1 is in its TurnOverPosition.
        for i in range( self.numRotors ):
            self.whichRotorsToShift[ i ] = self.rotors[ i ].atTurnOverPosition()

        # counts how many True's there are in a row from index pos 0.
        # If count= 1 then rotor 1 is in position ==> shift rotor2.
        # If count= 2 then rotor's 1 & 2 are in position ==> shift
        # rotors 2 & 3, etc.
        countNumberOfTrue = 0
        for index, value in enumerate( self.whichRotorsToShift ):
            # if you find a true count it and check the next value
            if self.whichRotorsToShift[ index ] == True:
                countNumberOfTrue += 1
            # if you find a 'False' then break
            else:
                break
        return countNumberOfTrue

    def encrypt( self, text ):
        """
        Encrypts a string of text.
        """

        nums       = ()
        cipherText = ""

        # convert plaintext into upper case
        # convert individual plaintext characters in text into numbers
        for letters in text.upper():
            # only allow valid letters to continue else skip the letter
            if letters in self.rotorData.alphabet:
                nums += ( self.rotorData.convertLetterToNumber( letters ), )

        print ("\nStarting rotor settings in window:",)
        print (self.__str__())
        for num in nums:

            # shift rotors
            self.shiftRotors()
            print (self.__str__())

            # passthrough plugboard
            num = self.plugboard.getPlugBoard()[ num ]

            # passthrough rotors in order
            for rotor in range( self.numRotors ):
                num = self.rotors[ rotor ].encode( num )

            # hit reflector
            num = self.reflector.getReflector()[ num ]

            # passthrough the inverse of the rotors
            for rotor in reversed( range( self.numRotors ) ):
                num = self.rotors[ rotor ].iEncode( num )

            # passthrough plugboard
            num = self.plugboard.getPlugBoard()[ num ]

            # create cipherText
            cipherText +=  self.rotorData.convertNumberToLetter( num )

        # formats the output to add blanks at user defined intervals
        if self.interval != 0:
            cipherText = self.formatOutput( cipherText )

        return cipherText

    def formatOutput( self, cipherText ):
        """
        Adds blanks to the ciphertext at self.intervals
        """

        cipherText = list( cipherText )

        # adds a ' ' into every interval-1 index location
        index, counter = 0, 0
        lengthOfText = len( cipherText )
        while counter <= lengthOfText:
            cipherText.insert( index, ' ' )
            index += self.interval
            counter += 1

        # remove the first element of the list - it's a ' '
        cipherText.pop( 0 )

        # make list into a string
        cipherText = ''.join( cipherText )
        return cipherText

    def setInterval( self, interval = -1 ):
        """
        Adds a space to the output every interval.
        """

        assert interval >= -1, "must be >= -1"

        # if 0 is entered then make it return 0
        if interval == 0:
            interval = -1

        # to add a blank in every 5th spot, interval needs to be 6
        self.interval = interval+1

    def machineSettings( self ):
        """
        Provides the current machine settings.
        """

        walzen = []
        ringstellung = []
        window = []
        stecker = []

        print ("\nCurrent SetUp of the Machine:\n")

        # order of rotors & ring settings
        for index, rotor in enumerate( self.rotors ):
            name = self.rotors[ index ].name
            ringSetting = self.rotorData.convertNumberToLetter( self.rotors[ index ].ringSetting )
            rotorSetting = self.rotorData.convertNumberToLetter( self.rotors[ index ].outerRing[ 0 ] )
            walzen.append( name )
            ringstellung.append( ringSetting )
            window.append( rotorSetting )

        print ("         UKW: %s" % self.reflector.name)
        print ("      Walzen:",)
        for rotor in reversed( walzen ):
            print ("%s\t" % rotor,)

        print ("\nRingstellung:\t",)
        for ring in reversed( ringstellung ):
            print ("%s\t" % ring,)

        print ("\nRotor Window:\t",)
        for letter in reversed( window ):
            print ("%s\t" % letter,)

        print ("\n     Stecker:",)
        for pair in self.plugboard.connections:
            print ("%s%s " % ( pair[ 0 ], pair[ 1 ] ),)
        print ("\n")

    def __str__( self ):
        """
        Displays letters in the rotor's window.
        """

        rotorList = []
        for rotors in self.rotors:
            rotorList.append( rotors.alphabet[ rotors.outerRing[0] ] )

        return '-'.join( map(str, reversed( rotorList ) ) )


class User( RotorData ):
    """
    Future user interface.
    """

    def main( self, plainText ):
        """
        The main program.
        """

        rotorData = RotorData()

        # set the number of rotors
        rotor1 = Rotor( 'I', rotorData.rotor1 )
        rotor2 = Rotor( 'II', rotorData.rotor2 )
        rotor3 = Rotor( 'III', rotorData.rotor3 )
        rotor4 = Rotor( 'IV', rotorData.rotor4 )

        # set the reflector
        reflector = Reflector( 'B', rotorData.reflB )

        # initialize the plugboard
        plugboard = Plugboard()

        # Set Notch Positions
        # Note: n-1 notches are important. The last rotor on the left will
        # not engage a rotor to its left since there is not a rotor there.
        # Enter the letter in the window for the notch position
        rotor1.setNotchPositions( 'Q', ) # Y=notch; Q=window
        rotor2.setNotchPositions( 'E', ) # M=notch; E=window
        rotor3.setNotchPositions( 'V', ) # D=notch; V=window
        rotor4.setNotchPositions( 'J', ) # R=notch; J=window

        # Set Ringsettings
        # valid values are between 'A' - 'Z'
        rotor1.setRingSetting( 'A' )
        rotor2.setRingSetting( 'A' )
        rotor3.setRingSetting( 'A' )
        rotor4.setRingSetting( 'A' )

        # Make Plugboard Connections
        # Each entry must be unique. Can't use any letter more than once
        # in the entire plugboard as only one plug will fit in each letter.
        plugboard.makeConnections( 'a', 'b' )
        plugboard.makeConnections( 'x', 'o' )
        plugboard.makeConnections( 's', 'n' )
        plugboard.makeConnections( 'q', 'd' )
        plugboard.makeConnections( 'g', 'z' )

        # Set Letter in Rotor Window
        # Valid input 'A' - 'Z'
        rotor1.setLetterInWindow( 'A' )
        rotor2.setLetterInWindow( 'A' )
        rotor3.setLetterInWindow( 'A' )
        rotor4.setLetterInWindow( 'A' )

        # Create the machine based on the setup above
        # Note: you can put the rotors in any order (e.g, 3,2,1; 1,2,3; 1,3,4), etc.
        # Note: the rotors in here are reversed so the last rotor in the parens
        # is the left rotor on the enigma.
        machine = EnigmaMachine( reflector, plugboard, rotor1, rotor2, rotor3 )

        # Set formatting of output; leave blank for no blanks to be added
        # Enigma output had an interval of 5.
        #self.machine.setInterval( 5 )
        machine.setInterval(  )

        # print machine settings
        machine.machineSettings()

        # encrypt plaintext to ciphertext
        cipherText = machine.encrypt( plainText )

        print ("\nThe plaintext to encrypt is:\n", plainText)
        print ("\nThe ciphertext is:\n", cipherText)

if __name__ == '__main__':
    user = User()

    plainText = "This is a test."

    exit(user.main(plainText))