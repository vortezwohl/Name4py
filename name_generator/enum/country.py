from enum import Enum


class Country(Enum):
    def __init__(self, official_name: str, name: str, numeric: str, abbr: str):
        self._official_name = official_name
        self._name = name
        self._numeric = numeric
        self._abbr = abbr

    @property
    def official_name(self) -> str:
        return self._official_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def numeric(self) -> str:
        return self._numeric

    @property
    def abbr(self) -> str:
        return self._abbr

    HUN = ('Hungary', 'Hungary', '348')
    DZA = ("People's Democratic Republic of Algeria", 'Algeria', '012')
    NLD = ('Kingdom of the Netherlands', 'Netherlands', '528')
    FIN = ('Republic of Finland', 'Finland', '246')
    BGD = ("People's Republic of Bangladesh", 'Bangladesh', '050')
    BWA = ('Republic of Botswana', 'Botswana', '072')
    HTI = ('Republic of Haiti', 'Haiti', '332')
    FRA = ('French Republic', 'France', '250')
    SAU = ('Kingdom of Saudi Arabia', 'Saudi Arabia', '682')
    MAC = ('Macao Special Administrative Region of China', 'Macao', '446')
    PRT = ('Portuguese Republic', 'Portugal', '620')
    SLV = ('Republic of El Salvador', 'El Salvador', '222')
    IRN = ('Islamic Republic of Iran', 'Iran', '364')
    MDV = ('Republic of Maldives', 'Maldives', '462')
    SWE = ('Kingdom of Sweden', 'Sweden', '752')
    KHM = ('Kingdom of Cambodia', 'Cambodia', '116')
    ETH = ('Federal Democratic Republic of Ethiopia', 'Ethiopia', '231')
    ECU = ('Republic of Ecuador', 'Ecuador', '218')
    GEO = ('Georgia', 'Georgia', '268')
    MEX = ('United Mexican States', 'Mexico', '484')
    QAT = ('State of Qatar', 'Qatar', '634')
    SYR = ('Syrian Arab Republic', 'Syrian', '760')
    ITA = ('Italian Republic', 'Italy', '380')
    SVN = ('Republic of Slovenia', 'Slovenia', '705')
    HND = ('Republic of Honduras', 'Honduras', '340')
    BHR = ('Kingdom of Bahrain', 'Bahrain', '048')
    ISL = ('Republic of Iceland', 'Iceland', '352')
    AZE = ('Republic of Azerbaijan', 'Azerbaijan', '031')
    HKG = ('Hong Kong Special Administrative Region of China', 'Hong Kong', '344')
    LBN = ('Lebanese Republic', 'Lebanon', '422')
    EGY = ('Arab Republic of Egypt', 'Egypt', '818')
    GRC = ('Hellenic Republic', 'Greece', '300')
    BDI = ('Republic of Burundi', 'Burundi', '108')
    AFG = ('Islamic Republic of Afghanistan', 'Afghanistan', '004')
    USA = ('United States of America', 'United States', '840')
    BOL = ('Plurinational State of Bolivia', 'Bolivia', '068')
    TUN = ('Republic of Tunisia', 'Tunisia', '788')
    URY = ('Eastern Republic of Uruguay', 'Uruguay', '858')
    BGR = ('Republic of Bulgaria', 'Bulgaria', '100')
    JOR = ('Hashemite Kingdom of Jordan', 'Jordan', '400')
    NGA = ('Federal Republic of Nigeria', 'Nigeria', '566')
    MYS = ('Malaysia', 'Malaysia', '458')
    HRV = ('Republic of Croatia', 'Croatia', '191')
    CHL = ('Republic of Chile', 'Chile', '152')
    SGP = ('Republic of Singapore', 'Singapore', '702')
    IDN = ('Republic of Indonesia', 'Indonesia', '360')
    PER = ('Republic of Peru', 'Peru', '604')
    OMN = ('Sultanate of Oman', 'Oman', '512')
    GTM = ('Republic of Guatemala', 'Guatemala', '320')
    TUR = ('Republic of Türkiye', 'Türkiye', '792')
    CAN = ('Canada', 'Canada', '124')
    BRA = ('Federative Republic of Brazil', 'Brazil', '076')
    FJI = ('Republic of Fiji', 'Fiji', '242')
    JAM = ('Jamaica', 'Jamaica', '388')
    IRQ = ('Republic of Iraq', 'Iraq', '368')
    ALB = ('Republic of Albania', 'Albania', '008')
    DJI = ('Republic of Djibouti', 'Djibouti', '262')
    LUX = ('Grand Duchy of Luxembourg', 'Luxembourg', '442')
    IRL = ('Ireland', 'Ireland', '372')
    SRB = ('Republic of Serbia', 'Serbia', '688')
    CHE = ('Swiss Confederation', 'Switzerland', '756')
    LBY = ('Libya', 'Libya', '434')
    BEL = ('Kingdom of Belgium', 'Belgium', '056')
    TKM = ('Turkmenistan', 'Turkmenistan', '795')
    CMR = ('Republic of Cameroon', 'Cameroon', '120')
    CZE = ('Czech Republic', 'Czechia', '203')
    ARG = ('Argentine Republic', 'Argentina', '032')
    PAN = ('Republic of Panama', 'Panama', '591')
    POL = ('Republic of Poland', 'Poland', '616')
    BRN = ('Brunei Darussalam', 'Brunei', '096')
    KAZ = ('Republic of Kazakhstan', 'Kazakhstan', '398')
    DEU = ('Federal Republic of Germany', 'Germany', '276')
    PSE = ('the State of Palestine', 'Palestine', '275')
    CYP = ('Republic of Cyprus', 'Cyprus', '196')
    ESP = ('Kingdom of Spain', 'Spain', '724')
    UAE = ('United Arab Emirates', 'United Arab Emirates', '784')
    JPN = ('Japan', 'Japan', '392')
    MDA = ('Republic of Moldova', 'Moldova', '498')
    GBR = ('United Kingdom of Great Britain and Northern Ireland', 'United Kingdom', '826')
    YEM = ('Republic of Yemen', 'Yemen', '887')
    NOR = ('Kingdom of Norway', 'Norway', '578')
    KOR = ('Korea, Republic of', 'Korea', '410')
    ISR = ('State of Israel', 'Israel', '376')
    DNK = ('Kingdom of Denmark', 'Denmark', '208')
    PRI = ('Puerto Rico', 'Puerto Rico', '630')
    NAM = ('Republic of Namibia', 'Namibia', '516')
    MAR = ('Kingdom of Morocco', 'Morocco', '504')
    ZAF = ('Republic of South Africa', 'South Africa', '710')
    COL = ('Republic of Colombia', 'Colombia', '170')
    LTU = ('Republic of Lithuania', 'Lithuania', '440')
    MUS = ('Republic of Mauritius', 'Mauritius', '480')
    KWT = ('State of Kuwait', 'Kuwait', '414')
    EST = ('Republic of Estonia', 'Estonia', '233')
    TWN = ('Taiwan, Province of China', 'Taiwan', '158')
    MLT = ('Republic of Malta', 'Malta', '470')
    GHA = ('Republic of Ghana', 'Ghana', '288')
    CRI = ('Republic of Costa Rica', 'Costa Rica', '188')
    RUS = ('Russian Federation', 'Russian', '643')
    IND = ('Republic of India', 'India', '356')
    CHN = ("People's Republic of China", 'China', '156')
    BFA = ('Burkina Faso', 'Burkina Faso', '854')
    AGO = ('Republic of Angola', 'Angola', '024')
    AUT = ('Republic of Austria', 'Austria', '040')
    SDN = ('Republic of the Sudan', 'Sudan', '729')
    PHL = ('Republic of the Philippines', 'Philippines', '608')
