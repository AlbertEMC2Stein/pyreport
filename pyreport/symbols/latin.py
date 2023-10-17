from pyreport.symbols import Symbol, SymbolCollection

__all__ = ["BlackBoardSymbols", "CalligraphicSymbols", "FrakturSymbols"]


class BlackBoardSymbols(SymbolCollection):
    AA = Symbol("AA", r"\mathbb{A}", "\u1D538")
    BB = Symbol("BB", r"\mathbb{B}", "\u1D539")
    CC = Symbol("CC", r"\mathbb{C}", "\u2102")
    DD = Symbol("DD", r"\mathbb{D}", "\u1D53B")
    EE = Symbol("EE", r"\mathbb{E}", "\u1D53C")
    FF = Symbol("FF", r"\mathbb{F}", "\u1D53D")
    GG = Symbol("GG", r"\mathbb{G}", "\u1D53E")
    HH = Symbol("HH", r"\mathbb{H}", "\u210D")
    II = Symbol("II", r"\mathbb{I}", "\u1D540")
    JJ = Symbol("JJ", r"\mathbb{J}", "\u1D541")
    KK = Symbol("KK", r"\mathbb{K}", "\u1D542")
    LL = Symbol("LL", r"\mathbb{L}", "\u1D543")
    MM = Symbol("MM", r"\mathbb{M}", "\u1D544")
    NN = Symbol("NN", r"\mathbb{N}", "\u2115")
    OO = Symbol("OO", r"\mathbb{O}", "\u1D546")
    PP = Symbol("PP", r"\mathbb{P}", "\u2119")
    QQ = Symbol("QQ", r"\mathbb{Q}", "\u211A")
    RR = Symbol("RR", r"\mathbb{R}", "\u211D")
    SS = Symbol("SS", r"\mathbb{S}", "\u1D54A")
    TT = Symbol("TT", r"\mathbb{T}", "\u1D54B")
    UU = Symbol("UU", r"\mathbb{U}", "\u1D54C")
    VV = Symbol("VV", r"\mathbb{V}", "\u1D54D")
    WW = Symbol("WW", r"\mathbb{W}", "\u1D54E")
    XX = Symbol("XX", r"\mathbb{X}", "\u1D54F")
    YY = Symbol("YY", r"\mathbb{Y}", "\u1D550")
    ZZ = Symbol("ZZ", r"\mathbb{Z}", "\u2124")

    @classmethod
    def get_symbols(cls):
        return super(BlackBoardSymbols, cls).get_symbols()
    
    @classmethod
    def list_symbols(cls):
        super(BlackBoardSymbols, cls).list_symbols()


class CalligraphicSymbols(SymbolCollection):
    calA = Symbol("calA", r"\mathcal{A}", "\u1D49C")
    calB = Symbol("calB", r"\mathcal{B}", "\u212C")
    calC = Symbol("calC", r"\mathcal{C}", "\u1D49E")
    calD = Symbol("calD", r"\mathcal{D}", "\u1D49F")
    calE = Symbol("calE", r"\mathcal{E}", "\u2130")
    calF = Symbol("calF", r"\mathcal{F}", "\u2131")
    calG = Symbol("calG", r"\mathcal{G}", "\u1D4A2")
    calH = Symbol("calH", r"\mathcal{H}", "\u210B")
    calI = Symbol("calI", r"\mathcal{I}", "\u2110")
    calJ = Symbol("calJ", r"\mathcal{J}", "\u1D4A5")
    calK = Symbol("calK", r"\mathcal{K}", "\u1D4A6")
    calL = Symbol("calL", r"\mathcal{L}", "\u2112")
    calM = Symbol("calM", r"\mathcal{M}", "\u2133")
    calN = Symbol("calN", r"\mathcal{N}", "\u1D4A9")
    calO = Symbol("calO", r"\mathcal{O}", "\u1D4AA")
    calP = Symbol("calP", r"\mathcal{P}", "\u1D4AB")
    calQ = Symbol("calQ", r"\mathcal{Q}", "\u1D4AC")
    calR = Symbol("calR", r"\mathcal{R}", "\u211B")
    calS = Symbol("calS", r"\mathcal{S}", "\u1D4AE")
    calT = Symbol("calT", r"\mathcal{T}", "\u1D4AF")
    calU = Symbol("calU", r"\mathcal{U}", "\u1D4B0")
    calV = Symbol("calV", r"\mathcal{V}", "\u1D4B1")
    calW = Symbol("calW", r"\mathcal{W}", "\u1D4B2")
    calX = Symbol("calX", r"\mathcal{X}", "\u1D4B3")
    calY = Symbol("calY", r"\mathcal{Y}", "\u1D4B4")
    calZ = Symbol("calZ", r"\mathcal{Z}", "\u1D4B5")

    @classmethod
    def get_symbols(cls):
        return super(CalligraphicSymbols, cls).get_symbols()
    
    @classmethod
    def list_symbols(cls):
        super(CalligraphicSymbols, cls).list_symbols()


class FrakturSymbols(SymbolCollection):
    frakA = Symbol("frakA", r"\mathfrak{A}", "\u1D56C")
    frakB = Symbol("frakB", r"\mathfrak{B}", "\u1D56D")
    frakC = Symbol("frakC", r"\mathfrak{C}", "\u1D56E")
    frakD = Symbol("frakD", r"\mathfrak{D}", "\u1D56F")
    frakE = Symbol("frakE", r"\mathfrak{E}", "\u1D570")
    frakF = Symbol("frakF", r"\mathfrak{F}", "\u1D571")
    frakG = Symbol("frakG", r"\mathfrak{G}", "\u1D572")
    frakH = Symbol("frakH", r"\mathfrak{H}", "\u1D573")
    frakI = Symbol("frakI", r"\mathfrak{I}", "\u1D574")
    frakJ = Symbol("frakJ", r"\mathfrak{J}", "\u1D575")
    frakK = Symbol("frakK", r"\mathfrak{K}", "\u1D576")
    frakL = Symbol("frakL", r"\mathfrak{L}", "\u1D577")
    frakM = Symbol("frakM", r"\mathfrak{M}", "\u1D578")
    frakN = Symbol("frakN", r"\mathfrak{N}", "\u1D579")
    frakO = Symbol("frakO", r"\mathfrak{O}", "\u1D57A")
    frakP = Symbol("frakP", r"\mathfrak{P}", "\u1D57B")
    frakQ = Symbol("frakQ", r"\mathfrak{Q}", "\u1D57C")
    frakR = Symbol("frakR", r"\mathfrak{R}", "\u1D57D")
    frakS = Symbol("frakS", r"\mathfrak{S}", "\u1D57E")
    frakT = Symbol("frakT", r"\mathfrak{T}", "\u1D57F")
    frakU = Symbol("frakU", r"\mathfrak{U}", "\u1D580")
    frakV = Symbol("frakV", r"\mathfrak{V}", "\u1D581")
    frakW = Symbol("frakW", r"\mathfrak{W}", "\u1D582")
    frakX = Symbol("frakX", r"\mathfrak{X}", "\u1D583")
    frakY = Symbol("frakY", r"\mathfrak{Y}", "\u1D584")
    frakZ = Symbol("frakZ", r"\mathfrak{Z}", "\u1D585")

    @classmethod
    def get_symbols(cls):
        return super(FrakturSymbols, cls).get_symbols()
    
    @classmethod
    def list_symbols(cls):
        super(FrakturSymbols, cls).list_symbols()
        