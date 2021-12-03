class CompressedGene:
    def __init__(self,gene: str) -> None:
        self._compress(gene)

    def _compress(self,gene: str) -> None:
        self.bit_string: int=1 #start with sentinel
        for nucleotide in gene.upper():#Upper consider only uppercase
            self.bit_string <<=2 #shift two bits
            if nucleotide == "A": #change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C": #change last two bits to 00
                self.bit_string |= 0b01
            elif nucleotide == "G":  # change last two bits to 00
                self.bit_string |= 0b10
            elif nucleotide == "T":  # change last two bits to 00
                self.bit_string |= 0b11
            else:
                raise ValueError("!Invalid Nucleotide: {}".format(nucleotide))
        return gene[::-1] #[::-1] reverses string by slicing backward

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1,2): # -1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11  #get just relevant bits
            if bits == 0b00:  #A
                gene +="A"
            elif bits == 0b01:  # C
                gene +="C"
            elif bits == 0b10:  # G
                gene +="G"
            elif bits == 0b11:  #T
                gene +="T"
            else:
                raise ValueError("!Invalid Nucleotide: {}".format(bits))
        return gene[::-1] #[::-1] reverses string by slicing backward

    def __str__(self) -> str: # string representation for pretty printing
        return self.decompress()


if __name__ =="__main__":
    from sys import getsizeof
    original: str = ("TAGGGATTAACCGGTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATAaAGCCATGGATCGATTATA" * 100).upper()#transforma to uppercase
    print("original is {} bytes".format(getsizeof(original)))
    compressed = CompressedGene(original) #compress
    print("Compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(original)
    print(compressed.bit_string)
    print("original and bit string are the same:",original==compressed)
    print("original and decompressed are the same:",(original == compressed.decompress()))
    #print("Compressed Gene: ",(compressed))


