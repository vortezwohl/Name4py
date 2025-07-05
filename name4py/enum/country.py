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

    HUN = ('Hungary', 'Hungary', '348', 'HU')
    DZA = ("People's Democratic Republic of Algeria", 'Algeria', '012', 'DZ')
    NLD = ('Kingdom of the Netherlands', 'Netherlands', '528', 'NL')
    FIN = ('Republic of Finland', 'Finland', '246', 'FI')
    BGD = ("People's Republic of Bangladesh", 'Bangladesh', '050', 'BD')
    BWA = ('Republic of Botswana', 'Botswana', '072', 'BW')
    HTI = ('Republic of Haiti', 'Haiti', '332', 'HT')
    FRA = ('French Republic', 'France', '250', 'FR')
    SAU = ('Kingdom of Saudi Arabia', 'Saudi Arabia', '682', 'SA')
    MAC = ('Macao Special Administrative Region of China', 'Macao', '446', 'MO')
    PRT = ('Portuguese Republic', 'Portugal', '620', 'PT')
    SLV = ('Republic of El Salvador', 'El Salvador', '222', 'SV')
    IRN = ('Islamic Republic of Iran', 'Iran', '364', 'IR')
    MDV = ('Republic of Maldives', 'Maldives', '462', 'MV')
    SWE = ('Kingdom of Sweden', 'Sweden', '752', 'SE')
    KHM = ('Kingdom of Cambodia', 'Cambodia', '116', 'KH')
    ETH = ('Federal Democratic Republic of Ethiopia', 'Ethiopia', '231', 'ET')
    ECU = ('Republic of Ecuador', 'Ecuador', '218', 'EC')
    GEO = ('Georgia', 'Georgia', '268', 'GE')
    MEX = ('United Mexican States', 'Mexico', '484', 'MX')
    QAT = ('State of Qatar', 'Qatar', '634', 'QA')
    SYR = ('Syrian Arab Republic', 'Syria', '760', 'SY')
    ITA = ('Italian Republic', 'Italy', '380', 'IT')
    SVN = ('Republic of Slovenia', 'Slovenia', '705', 'SI')
    HND = ('Republic of Honduras', 'Honduras', '340', 'HN')
    BHR = ('Kingdom of Bahrain', 'Bahrain', '048', 'BH')
    ISL = ('Republic of Iceland', 'Iceland', '352', 'IS')
    AZE = ('Republic of Azerbaijan', 'Azerbaijan', '031', 'AZ')
    HKG = ('Hong Kong Special Administrative Region of China', 'Hong Kong', '344', 'HK')
    LBN = ('Lebanese Republic', 'Lebanon', '422', 'LB')
    EGY = ('Arab Republic of Egypt', 'Egypt', '818', 'EG')
    GRC = ('Hellenic Republic', 'Greece', '300', 'GR')
    BDI = ('Republic of Burundi', 'Burundi', '108', 'BI')
    AFG = ('Islamic Republic of Afghanistan', 'Afghanistan', '004', 'AF')
    USA = ('United States of America', 'United States', '840', 'US')
    BOL = ('Plurinational State of Bolivia', 'Bolivia', '068', 'BO')
    TUN = ('Republic of Tunisia', 'Tunisia', '788', 'TN')
    URY = ('Eastern Republic of Uruguay', 'Uruguay', '858', 'UY')
    BGR = ('Republic of Bulgaria', 'Bulgaria', '100', 'BG')
    JOR = ('Hashemite Kingdom of Jordan', 'Jordan', '400', 'JO')
    NGA = ('Federal Republic of Nigeria', 'Nigeria', '566', 'NG')
    MYS = ('Malaysia', 'Malaysia', '458', 'MY')
    HRV = ('Republic of Croatia', 'Croatia', '191', 'HR')
    CHL = ('Republic of Chile', 'Chile', '152', 'CL')
    SGP = ('Republic of Singapore', 'Singapore', '702', 'SG')
    IDN = ('Republic of Indonesia', 'Indonesia', '360', 'ID')
    PER = ('Republic of Peru', 'Peru', '604', 'PE')
    OMN = ('Sultanate of Oman', 'Oman', '512', 'OM')
    GTM = ('Republic of Guatemala', 'Guatemala', '320', 'GT')
    TUR = ('Republic of Türkiye', 'Türkiye', '792', 'TR')
    CAN = ('Canada', 'Canada', '124', 'CA')
    BRA = ('Federative Republic of Brazil', 'Brazil', '076', 'BR')
    FJI = ('Republic of Fiji', 'Fiji', '242', 'FJ')
    JAM = ('Jamaica', 'Jamaica', '388', 'JM')
    IRQ = ('Republic of Iraq', 'Iraq', '368', 'IQ')
    ALB = ('Republic of Albania', 'Albania', '008', 'AL')
    DJI = ('Republic of Djibouti', 'Djibouti', '262', 'DJ')
    LUX = ('Grand Duchy of Luxembourg', 'Luxembourg', '442', 'LU')
    IRL = ('Ireland', 'Ireland', '372', 'IE')
    SRB = ('Republic of Serbia', 'Serbia', '688', 'RS')
    CHE = ('Swiss Confederation', 'Switzerland', '756', 'CH')
    LBY = ('Libya', 'Libya', '434', 'LY')
    BEL = ('Kingdom of Belgium', 'Belgium', '056', 'BE')
    TKM = ('Turkmenistan', 'Turkmenistan', '795', 'TM')
    CMR = ('Republic of Cameroon', 'Cameroon', '120', 'CM')
    CZE = ('Czech Republic', 'Czechia', '203', 'CZ')
    ARG = ('Argentine Republic', 'Argentina', '032', 'AR')
    PAN = ('Republic of Panama', 'Panama', '591', 'PA')
    POL = ('Republic of Poland', 'Poland', '616', 'PL')
    BRN = ('Brunei Darussalam', 'Brunei Darussalam', '096', 'BN')
    KAZ = ('Republic of Kazakhstan', 'Kazakhstan', '398', 'KZ')
    DEU = ('Federal Republic of Germany', 'Germany', '276', 'DE')
    PSE = ('the State of Palestine', 'Palestine, State of', '275', 'PS')
    CYP = ('Republic of Cyprus', 'Cyprus', '196', 'CY')
    ESP = ('Kingdom of Spain', 'Spain', '724', 'ES')
    UAE = ('United Arab Emirates', 'United Arab Emirates', '784', 'AE')
    JPN = ('Japan', 'Japan', '392', 'JP')
    MDA = ('Republic of Moldova', 'Moldova', '498', 'MD')
    GBR = ('United Kingdom of Great Britain and Northern Ireland', 'United Kingdom', '826', 'GB')
    YEM = ('Republic of Yemen', 'Yemen', '887', 'YE')
    NOR = ('Kingdom of Norway', 'Norway', '578', 'NO')
    KOR = ('Republic of Korea', 'South Korea', '410', 'KR')
    ISR = ('State of Israel', 'Israel', '376', 'IL')
    DNK = ('Kingdom of Denmark', 'Denmark', '208', 'DK')
    PRI = ('Puerto Rico', 'Puerto Rico', '630', 'PR')
    NAM = ('Republic of Namibia', 'Namibia', '516', 'NA')
    MAR = ('Kingdom of Morocco', 'Morocco', '504', 'MA')
    ZAF = ('Republic of South Africa', 'South Africa', '710', 'ZA')
    COL = ('Republic of Colombia', 'Colombia', '170', 'CO')
    LTU = ('Republic of Lithuania', 'Lithuania', '440', 'LT')
    MUS = ('Republic of Mauritius', 'Mauritius', '480', 'MU')
    KWT = ('State of Kuwait', 'Kuwait', '414', 'KW')
    EST = ('Republic of Estonia', 'Estonia', '233', 'EE')
    TWN = ('Taiwan, Province of China', 'Taiwan', '158', 'TW')
    THA = ('Kingdom of Thailand', 'Thailand', '764', 'TH')
    VNM = ('Socialist Republic of Vietnam', 'Vietnam', '704', 'VN')
    MLT = ('Republic of Malta', 'Malta', '470', 'MT')
    GHA = ('Republic of Ghana', 'Ghana', '288', 'GH')
    CRI = ('Republic of Costa Rica', 'Costa Rica', '188', 'CR')
    RUS = ('Russian Federation', 'Russian', '643', 'RU')
    IND = ('Republic of India', 'India', '356', 'IN')
    CHN = ("People's Republic of China", 'China', '156', 'CN')
    BFA = ('Burkina Faso', 'Burkina Faso', '854', 'BF')
    AGO = ('Republic of Angola', 'Angola', '024', 'AO')
    AUT = ('Republic of Austria', 'Austria', '040', 'AT')
    SDN = ('Republic of the Sudan', 'Sudan', '729', 'SD')
    PHL = ('Republic of the Philippines', 'Philippines', '608', 'PH')
