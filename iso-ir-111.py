""" Python Character Mapping Codec iso-ir-111 by Evgeny BOLK Stepanischev. http://bolknote.ru/

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_table)

    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_table)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input,self.errors,decoding_table)[0]

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name='iso-ir-111',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Table

decoding_table = (
    u'\x00'     #  0x00 -> NULL
    u'\x01'     #  0x01 -> START OF HEADING
    u'\x02'     #  0x02 -> START OF TEXT
    u'\x03'     #  0x03 -> END OF TEXT
    u'\x04'     #  0x04 -> END OF TRANSMISSION
    u'\x05'     #  0x05 -> ENQUIRY
    u'\x06'     #  0x06 -> ACKNOWLEDGE
    u'\x07'     #  0x07 -> BELL
    u'\x08'     #  0x08 -> BACKSPACE
    u'\t'       #  0x09 -> HORIZONTAL TABULATION
    u'\n'       #  0x0A -> LINE FEED
    u'\x0b'     #  0x0B -> VERTICAL TABULATION
    u'\x0c'     #  0x0C -> FORM FEED
    u'\r'       #  0x0D -> CARRIAGE RETURN
    u'\x0e'     #  0x0E -> SHIFT OUT
    u'\x0f'     #  0x0F -> SHIFT IN
    u'\x10'     #  0x10 -> DATA LINK ESCAPE
    u'\x11'     #  0x11 -> DEVICE CONTROL ONE
    u'\x12'     #  0x12 -> DEVICE CONTROL TWO
    u'\x13'     #  0x13 -> DEVICE CONTROL THREE
    u'\x14'     #  0x14 -> DEVICE CONTROL FOUR
    u'\x15'     #  0x15 -> NEGATIVE ACKNOWLEDGE
    u'\x16'     #  0x16 -> SYNCHRONOUS IDLE
    u'\x17'     #  0x17 -> END OF TRANSMISSION BLOCK
    u'\x18'     #  0x18 -> CANCEL
    u'\x19'     #  0x19 -> END OF MEDIUM
    u'\x1a'     #  0x1A -> SUBSTITUTE
    u'\x1b'     #  0x1B -> ESCAPE
    u'\x1c'     #  0x1C -> FILE SEPARATOR
    u'\x1d'     #  0x1D -> GROUP SEPARATOR
    u'\x1e'     #  0x1E -> RECORD SEPARATOR
    u'\x1f'     #  0x1F -> UNIT SEPARATOR
    u' '        #  0x20 -> SPACE
    u'!'        #  0x21 -> EXCLAMATION MARK
    u'"'        #  0x22 -> QUOTATION MARK
    u'#'        #  0x23 -> NUMBER SIGN
    u'$'        #  0x24 -> DOLLAR SIGN
    u'%'        #  0x25 -> PERCENT SIGN
    u'&'        #  0x26 -> AMPERSAND
    u"'"        #  0x27 -> APOSTROPHE
    u'('        #  0x28 -> LEFT PARENTHESIS
    u')'        #  0x29 -> RIGHT PARENTHESIS
    u'*'        #  0x2A -> ASTERISK
    u'+'        #  0x2B -> PLUS SIGN
    u','        #  0x2C -> COMMA
    u'-'        #  0x2D -> HYPHEN-MINUS
    u'.'        #  0x2E -> FULL STOP
    u'/'        #  0x2F -> SOLIDUS
    u'0'        #  0x30 -> DIGIT ZERO
    u'1'        #  0x31 -> DIGIT ONE
    u'2'        #  0x32 -> DIGIT TWO
    u'3'        #  0x33 -> DIGIT THREE
    u'4'        #  0x34 -> DIGIT FOUR
    u'5'        #  0x35 -> DIGIT FIVE
    u'6'        #  0x36 -> DIGIT SIX
    u'7'        #  0x37 -> DIGIT SEVEN
    u'8'        #  0x38 -> DIGIT EIGHT
    u'9'        #  0x39 -> DIGIT NINE
    u':'        #  0x3A -> COLON
    u';'        #  0x3B -> SEMICOLON
    u'<'        #  0x3C -> LESS-THAN SIGN
    u'='        #  0x3D -> EQUALS SIGN
    u'>'        #  0x3E -> GREATER-THAN SIGN
    u'?'        #  0x3F -> QUESTION MARK
    u'@'        #  0x40 -> COMMERCIAL AT
    u'A'        #  0x41 -> LATIN CAPITAL LETTER A
    u'B'        #  0x42 -> LATIN CAPITAL LETTER B
    u'C'        #  0x43 -> LATIN CAPITAL LETTER C
    u'D'        #  0x44 -> LATIN CAPITAL LETTER D
    u'E'        #  0x45 -> LATIN CAPITAL LETTER E
    u'F'        #  0x46 -> LATIN CAPITAL LETTER F
    u'G'        #  0x47 -> LATIN CAPITAL LETTER G
    u'H'        #  0x48 -> LATIN CAPITAL LETTER H
    u'I'        #  0x49 -> LATIN CAPITAL LETTER I
    u'J'        #  0x4A -> LATIN CAPITAL LETTER J
    u'K'        #  0x4B -> LATIN CAPITAL LETTER K
    u'L'        #  0x4C -> LATIN CAPITAL LETTER L
    u'M'        #  0x4D -> LATIN CAPITAL LETTER M
    u'N'        #  0x4E -> LATIN CAPITAL LETTER N
    u'O'        #  0x4F -> LATIN CAPITAL LETTER O
    u'P'        #  0x50 -> LATIN CAPITAL LETTER P
    u'Q'        #  0x51 -> LATIN CAPITAL LETTER Q
    u'R'        #  0x52 -> LATIN CAPITAL LETTER R
    u'S'        #  0x53 -> LATIN CAPITAL LETTER S
    u'T'        #  0x54 -> LATIN CAPITAL LETTER T
    u'U'        #  0x55 -> LATIN CAPITAL LETTER U
    u'V'        #  0x56 -> LATIN CAPITAL LETTER V
    u'W'        #  0x57 -> LATIN CAPITAL LETTER W
    u'X'        #  0x58 -> LATIN CAPITAL LETTER X
    u'Y'        #  0x59 -> LATIN CAPITAL LETTER Y
    u'Z'        #  0x5A -> LATIN CAPITAL LETTER Z
    u'['        #  0x5B -> LEFT SQUARE BRACKET
    u'\\'       #  0x5C -> REVERSE SOLIDUS
    u']'        #  0x5D -> RIGHT SQUARE BRACKET
    u'^'        #  0x5E -> CIRCUMFLEX ACCENT
    u'_'        #  0x5F -> LOW LINE
    u'`'        #  0x60 -> GRAVE ACCENT
    u'a'        #  0x61 -> LATIN SMALL LETTER A
    u'b'        #  0x62 -> LATIN SMALL LETTER B
    u'c'        #  0x63 -> LATIN SMALL LETTER C
    u'd'        #  0x64 -> LATIN SMALL LETTER D
    u'e'        #  0x65 -> LATIN SMALL LETTER E
    u'f'        #  0x66 -> LATIN SMALL LETTER F
    u'g'        #  0x67 -> LATIN SMALL LETTER G
    u'h'        #  0x68 -> LATIN SMALL LETTER H
    u'i'        #  0x69 -> LATIN SMALL LETTER I
    u'j'        #  0x6A -> LATIN SMALL LETTER J
    u'k'        #  0x6B -> LATIN SMALL LETTER K
    u'l'        #  0x6C -> LATIN SMALL LETTER L
    u'm'        #  0x6D -> LATIN SMALL LETTER M
    u'n'        #  0x6E -> LATIN SMALL LETTER N
    u'o'        #  0x6F -> LATIN SMALL LETTER O
    u'p'        #  0x70 -> LATIN SMALL LETTER P
    u'q'        #  0x71 -> LATIN SMALL LETTER Q
    u'r'        #  0x72 -> LATIN SMALL LETTER R
    u's'        #  0x73 -> LATIN SMALL LETTER S
    u't'        #  0x74 -> LATIN SMALL LETTER T
    u'u'        #  0x75 -> LATIN SMALL LETTER U
    u'v'        #  0x76 -> LATIN SMALL LETTER V
    u'w'        #  0x77 -> LATIN SMALL LETTER W
    u'x'        #  0x78 -> LATIN SMALL LETTER X
    u'y'        #  0x79 -> LATIN SMALL LETTER Y
    u'z'        #  0x7A -> LATIN SMALL LETTER Z
    u'{'        #  0x7B -> LEFT CURLY BRACKET
    u'|'        #  0x7C -> VERTICAL LINE
    u'}'        #  0x7D -> RIGHT CURLY BRACKET
    u'~'        #  0x7E -> TILDE
    u'\x7f'     #  0x7F -> DELETE
    u'\ufffe'   #  0x80 -> UNDEFINED 
    u'\ufffe'   #  0x81 -> UNDEFINED 
    u'\ufffe'   #  0x82 -> UNDEFINED 
    u'\ufffe'   #  0x83 -> UNDEFINED 
    u'\ufffe'   #  0x84 -> UNDEFINED 
    u'\ufffe'   #  0x85 -> UNDEFINED 
    u'\ufffe'   #  0x86 -> UNDEFINED 
    u'\ufffe'   #  0x87 -> UNDEFINED 
    u'\ufffe'   #  0x88 -> UNDEFINED 
    u'\ufffe'   #  0x89 -> UNDEFINED 
    u'\ufffe'   #  0x8A -> UNDEFINED 
    u'\ufffe'   #  0x8B -> UNDEFINED 
    u'\ufffe'   #  0x8C -> UNDEFINED 
    u'\ufffe'   #  0x8D -> UNDEFINED 
    u'\ufffe'   #  0x8E -> UNDEFINED 
    u'\ufffe'   #  0x8F -> UNDEFINED 
    u'\ufffe'   #  0x90 -> UNDEFINED
    u'\ufffe'   #  0x91 -> UNDEFINED 
    u'\ufffe'   #  0x92 -> UNDEFINED 
    u'\ufffe'   #  0x93 -> UNDEFINED 
    u'\ufffe'   #  0x94 -> UNDEFINED 
    u'\ufffe'   #  0x95 -> UNDEFINED 
    u'\ufffe'   #  0x96 -> UNDEFINED 
    u'\ufffe'   #  0x97 -> UNDEFINED 
    u'\ufffe'   #  0x98 -> UNDEFINED 
    u'\ufffe'   #  0x99 -> UNDEFINED 
    u'\ufffe'   #  0x9A -> UNDEFINED 
    u'\ufffe'   #  0x9B -> UNDEFINED 
    u'\ufffe'   #  0x9C -> UNDEFINED 
    u'\ufffe'   #  0x9D -> UNDEFINED 
    u'\ufffe'   #  0x9E -> UNDEFINED 
    u'\ufffe'   #  0x9F -> UNDEFINED 
    u'\xa0'     #  0xA0 -> NO-BREAK SPACE
    u'\u0452'   #  0xA1 -> CYRILLIC SMALL LETTER DJE
    u'\u0453'   #  0xA2 -> CYRILLIC SMALL LETTER GJE
    u'\u0451'   #  0xA3 -> CYRILLIC SMALL LETTER IO
    u'\u0454'   #  0xA4 -> CYRILLIC SMALL LETTER UKRAINIAN IE
    u'\u0455'   #  0xA5 -> CYRILLIC SMALL LETTER DZE
    u'\u0456'   #  0xA6 -> CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    u'\u0457'   #  0xA7 -> CYRILLIC SMALL LETTER YI
    u'\u0458'   #  0xA8 -> CYRILLIC SMALL LETTER JE
    u'\u0459'   #  0xA9 -> CYRILLIC SMALL LETTER LJE
    u'\u045a'   #  0xAA -> CYRILLIC SMALL LETTER NJE
    u'\u045b'   #  0xAB -> CYRILLIC SMALL LETTER TSHE
    u'\u045c'   #  0xAC -> CYRILLIC SMALL LETTER KJE
    u'\xad'     #  0xAD -> SHY
    u'\u045e'   #  0xAE -> CYRILLIC SMALL LETTER SHORT U
    u'\u045f'   #  0xAF -> CYRILLIC SMALL LETTER DZHE
    u'\u2116'   #  0xB0 -> NUMERO SIGN
    u'\u0402'   #  0xB1 -> CYRILLIC CAPITAL LETTER DJE
    u'\u0403'   #  0xB2 -> CYRILLIC CAPITAL LETTER GJE
    u'\u0401'   #  0xB3 -> CYRILLIC CAPITAL LETTER IO
    u'\u0404'   #  0xB4 -> CYRILLIC CAPITAL LETTER UKRAINIAN IE
    u'\u0405'   #  0xB5 -> CYRILLIC CAPITAL LETTER DZE
    u'\u0406'   #  0xB6 -> CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
    u'\u0407'   #  0xB7 -> CYRILLIC CAPITAL LETTER YI
    u'\u0408'   #  0xB8 -> CYRILLIC CAPITAL LETTER JE
    u'\u0409'   #  0xB9 -> CYRILLIC CAPITAL LETTER LJE
    u'\u040a'   #  0xBA -> CYRILLIC CAPITAL LETTER NJE
    u'\u040b'   #  0xBB -> CYRILLIC CAPITAL LETTER TSHE
    u'\u040c'   #  0xBC -> CYRILLIC CAPITAL LETTER KJE
    u'\u00a4'   #  0xBD -> CURRENCY SIGN
    u'\u040e'   #  0xBE -> CYRILLIC CAPITAL LETTER SHORT U
    u'\u040f'   #  0xBF -> CYRILLIC CAPITAL LETTER DZHE
    u'\u044e'   #  0xC0 -> CYRILLIC SMALL LETTER YU <- RUSSIAN
    u'\u0430'   #  0xC1 -> CYRILLIC SMALL LETTER A
    u'\u0431'   #  0xC2 -> CYRILLIC SMALL LETTER BE
    u'\u0446'   #  0xC3 -> CYRILLIC SMALL LETTER TSE
    u'\u0434'   #  0xC4 -> CYRILLIC SMALL LETTER DE
    u'\u0435'   #  0xC5 -> CYRILLIC SMALL LETTER IE
    u'\u0444'   #  0xC6 -> CYRILLIC SMALL LETTER EF
    u'\u0433'   #  0xC7 -> CYRILLIC SMALL LETTER GHE
    u'\u0445'   #  0xC8 -> CYRILLIC SMALL LETTER HA
    u'\u0438'   #  0xC9 -> CYRILLIC SMALL LETTER I
    u'\u0439'   #  0xCA -> CYRILLIC SMALL LETTER SHORT I
    u'\u043a'   #  0xCB -> CYRILLIC SMALL LETTER KA
    u'\u043b'   #  0xCC -> CYRILLIC SMALL LETTER EL
    u'\u043c'   #  0xCD -> CYRILLIC SMALL LETTER EM
    u'\u043d'   #  0xCE -> CYRILLIC SMALL LETTER EN
    u'\u043e'   #  0xCF -> CYRILLIC SMALL LETTER O
    u'\u043f'   #  0xD0 -> CYRILLIC SMALL LETTER PE
    u'\u044f'   #  0xD1 -> CYRILLIC SMALL LETTER YA
    u'\u0440'   #  0xD2 -> CYRILLIC SMALL LETTER ER
    u'\u0441'   #  0xD3 -> CYRILLIC SMALL LETTER ES
    u'\u0442'   #  0xD4 -> CYRILLIC SMALL LETTER TE
    u'\u0443'   #  0xD5 -> CYRILLIC SMALL LETTER U
    u'\u0436'   #  0xD6 -> CYRILLIC SMALL LETTER ZHE
    u'\u0432'   #  0xD7 -> CYRILLIC SMALL LETTER VE
    u'\u044c'   #  0xD8 -> CYRILLIC SMALL LETTER SOFT SIGN
    u'\u044b'   #  0xD9 -> CYRILLIC SMALL LETTER YERU
    u'\u0437'   #  0xDA -> CYRILLIC SMALL LETTER ZE
    u'\u0448'   #  0xDB -> CYRILLIC SMALL LETTER SHA
    u'\u044d'   #  0xDC -> CYRILLIC SMALL LETTER E
    u'\u0449'   #  0xDD -> CYRILLIC SMALL LETTER SHCHA
    u'\u0447'   #  0xDE -> CYRILLIC SMALL LETTER CHE
    u'\u044a'   #  0xDF -> CYRILLIC SMALL LETTER HARD SIGN
    u'\u042e'   #  0xE0 -> CYRILLIC CAPITAL LETTER YU
    u'\u0410'   #  0xE1 -> CYRILLIC CAPITAL LETTER A
    u'\u0411'   #  0xE2 -> CYRILLIC CAPITAL LETTER BE
    u'\u0426'   #  0xE3 -> CYRILLIC CAPITAL LETTER TSE
    u'\u0414'   #  0xE4 -> CYRILLIC CAPITAL LETTER DE
    u'\u0415'   #  0xE5 -> CYRILLIC CAPITAL LETTER IE
    u'\u0424'   #  0xE6 -> CYRILLIC CAPITAL LETTER EF
    u'\u0413'   #  0xE7 -> CYRILLIC CAPITAL LETTER GHE
    u'\u0425'   #  0xE8 -> CYRILLIC CAPITAL LETTER HA
    u'\u0418'   #  0xE9 -> CYRILLIC CAPITAL LETTER I
    u'\u0419'   #  0xEA -> CYRILLIC CAPITAL LETTER SHORT I
    u'\u041a'   #  0xEB -> CYRILLIC CAPITAL LETTER KA
    u'\u041b'   #  0xEC -> CYRILLIC CAPITAL LETTER EL
    u'\u041c'   #  0xED -> CYRILLIC CAPITAL LETTER EM
    u'\u041d'   #  0xEE -> CYRILLIC CAPITAL LETTER EN
    u'\u041e'   #  0xEF -> CYRILLIC CAPITAL LETTER O
    u'\u041f'   #  0xF0 -> CYRILLIC CAPITAL LETTER PE
    u'\u042f'   #  0xF1 -> CYRILLIC CAPITAL LETTER YA
    u'\u0420'   #  0xF2 -> CYRILLIC CAPITAL LETTER ER
    u'\u0421'   #  0xF3 -> CYRILLIC CAPITAL LETTER ES
    u'\u0422'   #  0xF4 -> CYRILLIC CAPITAL LETTER TE
    u'\u0423'   #  0xF5 -> CYRILLIC CAPITAL LETTER U
    u'\u0416'   #  0xF6 -> CYRILLIC CAPITAL LETTER ZHE
    u'\u0412'   #  0xF7 -> CYRILLIC CAPITAL LETTER VE
    u'\u042c'   #  0xF8 -> CYRILLIC CAPITAL LETTER SOFT SIGN
    u'\u042b'   #  0xF9 -> CYRILLIC CAPITAL LETTER YERU
    u'\u0417'   #  0xFA -> CYRILLIC CAPITAL LETTER ZE
    u'\u0428'   #  0xFB -> CYRILLIC CAPITAL LETTER SHA
    u'\u042d'   #  0xFC -> CYRILLIC CAPITAL LETTER E
    u'\u0429'   #  0xFD -> CYRILLIC CAPITAL LETTER SHCHA
    u'\u0427'   #  0xFE -> CYRILLIC CAPITAL LETTER CHE
    u'\u042a'   #  0xFF -> CYRILLIC CAPITAL LETTER HARD SIGN
)

### Encoding table
encoding_table=codecs.charmap_build(decoding_table)