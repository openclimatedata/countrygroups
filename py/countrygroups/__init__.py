"""
countrygroups
-------------

"""

from shortcountrynames import to_name

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions


class Group(list):

    def _add_dict_items(self, d):
        for k, v in d.items():
            v = Group(v)
            setattr(self, k, v)
            self += v

    def __init__(self, group):
        if isinstance(group, dict):
            self._add_dict_items(group)
        else:
            for v in group:
                if isinstance(v, dict):
                    self._add_dict_items(v)
                else:
                    self.append(v)

    @property
    def names(self):
        return sorted([to_name(item) for item in self])


ANNEX_ONE = Group([
    'AUS', 'AUT', 'BEL', 'BGR', 'BLR', 'CAN', 'CHE', 'CYP', 'CZE', 'DEU',
    'DNK', 'ESP', 'EST', 'EUU', 'FIN', 'FRA', 'GBR', 'GRC', 'HRV', 'HUN',
    'IRL', 'ISL', 'ITA', 'JPN', 'LIE', 'LTU', 'LUX', 'LVA', 'MCO', 'MLT',
    'NLD', 'NOR', 'NZL', 'POL', 'PRT', 'ROU', 'RUS', 'SVK', 'SVN', 'SWE',
    'TUR', 'UKR', 'USA'
])

ANNEX_ONE_KAZ = Group([
    'AUS', 'AUT', 'BEL', 'BGR', 'BLR', 'CAN', 'CHE', 'CYP', 'CZE', 'DEU',
    'DNK', 'ESP', 'EST', 'EUU', 'FIN', 'FRA', 'GBR', 'GRC', 'HRV', 'HUN',
    'IRL', 'ISL', 'ITA', 'JPN', 'KAZ', 'LIE', 'LTU', 'LUX', 'LVA', 'MCO',
    'MLT', 'NLD', 'NOR', 'NZL', 'POL', 'PRT', 'ROU', 'RUS', 'SVK', 'SVN',
    'SWE', 'TUR', 'UKR', 'USA'
])

AOSIS = Group([
    'ATG', 'BHS', 'BLZ', 'BRB', 'COK', 'COM', 'CPV', 'CUB', 'DMA', 'DOM',
    'FJI', 'FSM', 'GNB', 'GRD', 'GUY', 'HTI', 'JAM', 'KIR', 'KNA', 'LCA',
    'MDV', 'MHL', 'MUS', 'NIU', 'NRU', 'PLW', 'PNG', 'SGP', 'SLB', 'STP',
    'SUR', 'SYC', 'TLS', 'TON', 'TTO', 'TUV', 'VCT', 'VUT', 'WSM'
])

AR5 = Group({
    'ASIA': [
        'AFG', 'ASM', 'BGD', 'BRN', 'BTN', 'CCK', 'CHN', 'COK', 'CXR', 'FJI',
        'FSM', 'HMD', 'IDN', 'IND', 'IOT', 'KHM', 'KIR', 'KOR', 'LAO', 'LKA',
        'MDV', 'MHL', 'MMR', 'MNG', 'MNP', 'MYS', 'NCL', 'NFK', 'NIU', 'NPL',
        'NRU', 'PAK', 'PCN', 'PHL', 'PLW', 'PNG', 'PRK', 'PYF', 'SGP', 'SLB',
        'THA', 'TKL', 'TLS', 'TON', 'TUV', 'UMI', 'VNM', 'VUT', 'WLF', 'WSM'
    ],
    'EIT': [
        'ALB', 'ARM', 'AZE', 'BGR', 'BIH', 'BLR', 'CYP', 'CZE', 'EST', 'GEO',
        'HRV', 'HUN', 'KAZ', 'KGZ', 'LTU', 'LVA', 'MDA', 'MKD', 'MLT', 'MNE',
        'POL', 'ROU', 'RUS', 'SRB', 'SVK', 'SVN', 'TJK', 'TKM', 'UKR', 'UZB'
    ],
    'LAM': [
        'ABW', 'AIA', 'ANHH', 'ARG', 'ATA', 'ATF', 'ATG', 'BHS', 'BLZ', 'BMU',
        'BOL', 'BRA', 'BRB', 'BVT', 'CHL', 'COL', 'CRI', 'CUB', 'CUW', 'CYM',
        'DMA', 'DOM', 'ECU', 'FLK', 'GLP', 'GRD', 'GTM', 'GUF', 'GUY', 'HND',
        'HTI', 'JAM', 'KNA', 'LCA', 'MEX', 'MSR', 'MTQ', 'NIC', 'PAN', 'PER',
        'PRI', 'PRY', 'SGS', 'SLV', 'SUR', 'SXM', 'TCA', 'TTO', 'URY', 'VCT',
        'VEN', 'VGB', 'VIR'
    ],
    'MAF': [
        'AGO', 'ARE', 'BDI', 'BEN', 'BFA', 'BHR', 'BWA', 'CAF', 'CIV', 'CMR',
        'COD', 'COG', 'COM', 'CPV', 'DJI', 'DZA', 'EGY', 'ERI', 'ESH', 'ETH',
        'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'IRN', 'IRQ', 'ISR', 'JOR',
        'KEN', 'KWT', 'LBN', 'LBR', 'LBY', 'LSO', 'MAR', 'MDG', 'MLI', 'MOZ',
        'MRT', 'MUS', 'MWI', 'MYT', 'NAM', 'NER', 'NGA', 'OMN', 'PSE', 'QAT',
        'REU', 'RWA', 'SAU', 'SDN', 'SEN', 'SHN', 'SLE', 'SOM', 'SSD', 'STP',
        'SWZ', 'SYC', 'SYR', 'TCD', 'TGO', 'TUN', 'TZA', 'UGA', 'YEM', 'ZAF',
        'ZMB', 'ZWE'
    ],
    'OECD1990': [
        'ALA', 'AND', 'AUS', 'AUT', 'BEL', 'CAN', 'CHE', 'DEU', 'DNK', 'ESP',
        'FIN', 'FRA', 'FRO', 'GBR', 'GGY', 'GIB', 'GRC', 'GRL', 'GUM', 'IMN',
        'IRL', 'ISL', 'ITA', 'JEY', 'JPN', 'LIE', 'LUX', 'MCO', 'NLD', 'NOR',
        'NZL', 'PRT', 'SJM', 'SMR', 'SPM', 'SWE', 'TUR', 'USA', 'VAT'
    ]
})

AR32 = Group({
    'ANUZ': [
        'AUS', 'NZL'
    ],
    'BRA': [
        'BRA'
    ],
    'CAN': [
        'CAN'
    ],
    'CAS': [
        'ARM', 'AZE', 'GEO', 'KAZ', 'KGZ', 'TJK', 'TKM', 'UZB'
    ],
    'CHN': [
        'CHN'
    ],
    'EEU': [
        'ALB', 'BIH', 'HRV', 'MNE', 'MKD', 'SRB'
    ],
    'EEU_FSU': [
        'BLR', 'MDA', 'UKR'
    ],
    'EFTA': [
        'ISL', 'NOR', 'CHE'
    ],
    'EU12_H': [
        'CYP', 'CZE', 'EST', 'HUN', 'MLT', 'POL', 'SVK', 'SVN'
    ],
    'EU12_M': [
        'BGR', 'LVA', 'LTU', 'ROU'
    ],
    'EU15': [
        'AUT', 'BEL', 'DNK', 'FIN', 'FRA', 'DEU', 'GRC', 'IRL', 'ITA', 'LUX',
        'NLD', 'PRT', 'ESP', 'SWE', 'GBR'
    ],
    'IDN': [
        'IDN'
    ],
    'IND': [
        'IND'
    ],
    'JPN': [
        'JPN'
    ],
    'KOR': [
        'KOR'
    ],
    'LAM_L': [
        'BLZ', 'GTM', 'HTI', 'HND', 'NIC'
    ],
    'LAM_M': [
        'ATG', 'ARG', 'BHS', 'BRB', 'BMU', 'BOL', 'CHL', 'COL', 'CRI', 'CUB',
        'DMA', 'DOM', 'ECU', 'SLV', 'GUF', 'GRD', 'GLP', 'GUY', 'JAM', 'MTQ',
        'ANT', 'PAN', 'PRY', 'PER', 'KNA', 'LCA', 'VCT', 'SUR', 'TTO', 'URY',
        'VEN'
    ],
    'MAF': [
        'SHN'
    ],
    'MEA_H': [
        'BHR', 'ISR', 'KWT', 'OMN', 'QAT', 'SAU', 'ARE'
    ],
    'MEA_M': [
        'IRN', 'IRQ', 'JOR', 'LBN', 'PSE', 'SYR', 'YEM'
    ],
    'MEX': [
        'MEX'
    ],
    'NAF': [
        'DZA', 'EGY', 'LBY', 'MAR', 'TUN', 'ESH'
    ],
    'OAS_CPA': [
        'KHM', 'LAO', 'MNG', 'VNM'
    ],
    'OAS_L': [
        'ASM', 'BGD', 'FJI', 'FSM', 'MMR', 'NPL', 'PRK', 'PNG', 'PHL', 'WSM',
        'SLB', 'TLS', 'TON', 'VUT'
    ]
        ,
    'OAS_M': [
        'BTN', 'BRN', 'PYF', 'MYS', 'MDV', 'NCL', 'SGP', 'LKA', 'THA', 'GUM'
    ]
    ,
    'PAK': [
        'AFG', 'PAK'
    ]
        ,
    'RUS': [
        'RUS'
    ]
        ,
    'SAF': [
        'ZAF'
    ]
        ,
    'SSA_L': [
        'BEN', 'BFA', 'BDI', 'CPV', 'CMR', 'CAF', 'TCD', 'COM', 'CIV', 'COD',
        'DJI', 'GNQ', 'ERI', 'ETH', 'GMB', 'GHA', 'GIN', 'GNB', 'KEN', 'LSO',
        'LBR', 'MDG', 'MWI', 'MLI', 'MRT', 'MOZ', 'NER', 'NGA', 'COG', 'RWA',
        'SEN', 'SLE', 'SOM', 'SSD', 'SDN', 'STP', 'TZA', 'TGO', 'UGA', 'ZMB',
        'ZWE'
    ],
    'SSA_M': [
        'AGO', 'BWA', 'GAB', 'MUS', 'MYT', 'NAM', 'REU', 'SYC'
    ]
        ,
    'TUR': [
        'TUR'
    ]
        ,
    'TWN': [
        'TWN'
    ]
        ,
    'USA': [
        'PRI', 'VIR', 'USA'
        ]
 })

ARAB_GROUP = Group([
    'ARE', 'BHR', 'COM', 'DJI', 'DZA', 'EGY', 'IRQ', 'JOR', 'KWT', 'LBN',
    'LBY', 'MAR', 'MRT', 'OMN', 'PSE', 'QAT', 'SAU', 'SDN', 'SOM', 'SYR',
    'TUN', 'YEM'
])

BRICS = Group(['BRA', 'CHN', 'IND', 'RUS', 'ZAF'])

EIG = Group(['CHE', 'KOR', 'LIE', 'MCO', 'MEX'])

EUROPEAN_UNION = Group([
    'AUT', 'BEL', 'BGR', 'CYP', 'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN',
    'FRA', 'GRC', 'HRV', 'HUN', 'IRL', 'ITA', 'LTU', 'LUX', 'LVA', 'MLT',
    'NLD', 'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'SWE'
])

G20 = Group([
    'ARG', 'AUS', 'BRA', 'CAN', 'CHN', 'DEU', 'EUU', 'FRA', 'GBR', 'IDN',
    'IND', 'ITA', 'JPN', 'KOR', 'MEX', 'RUS', 'SAU', 'TUR', 'USA', 'ZAF'
])

G7 = Group(['CAN', 'DEU', 'EUU', 'FRA', 'GBR', 'ITA', 'JPN', 'USA'])

G77 = Group([
    'AFG', 'AGO', 'ARE', 'ARG', 'ATG', 'AZE', 'BDI', 'BEN', 'BFA', 'BGD',
    'BHR', 'BHS', 'BLZ', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BWA', 'CAF',
    'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COL', 'COM', 'CPV', 'CRI',
    'CUB', 'DJI', 'DMA', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ETH', 'FJI',
    'FSM', 'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'GRD', 'GTM', 'GUY',
    'HND', 'HTI', 'IDN', 'IND', 'IRN', 'IRQ', 'JAM', 'JOR', 'KEN', 'KHM',
    'KIR', 'KNA', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LKA', 'LSO',
    'MAR', 'MDG', 'MDV', 'MHL', 'MLI', 'MMR', 'MNG', 'MOZ', 'MRT', 'MUS',
    'MWI', 'MYS', 'NAM', 'NER', 'NGA', 'NIC', 'NPL', 'NRU', 'OMN', 'PAK',
    'PAN', 'PER', 'PHL', 'PNG', 'PRK', 'PRY', 'PSE', 'QAT', 'RWA', 'SAU',
    'SDN', 'SEN', 'SGP', 'SLB', 'SLE', 'SLV', 'SOM', 'SSD', 'STP', 'SUR',
    'SWZ', 'SYC', 'SYR', 'TCD', 'TGO', 'THA', 'TJK', 'TKM', 'TLS', 'TON',
    'TTO', 'TUN', 'TZA', 'UGA', 'URY', 'VCT', 'VEN', 'VNM', 'VUT', 'WSM',
    'YEM', 'ZAF', 'ZMB', 'ZWE'
])

GRADUATED_LDCS = Group(['BWA', 'CPV', 'GNQ', 'MDV', 'VUT', 'WSM'])

IMO = Group([
    'AGO', 'ALB', 'ARE', 'ARG', 'ARM', 'ATG', 'AUS', 'AUT', 'AZE', 'BEL',
    'BEN', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BOL', 'BRA',
    'BRB', 'BRN', 'BWA', 'CAN', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD',
    'COG', 'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CYP', 'CZE', 'DEU',
    'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESP', 'EST',
    'ETH', 'FIN', 'FJI', 'FRA', 'GAB', 'GBR', 'GEO', 'GHA', 'GIN', 'GMB',
    'GNB', 'GNQ', 'GRC', 'GRD', 'GTM', 'GUY', 'HND', 'HRV', 'HTI', 'HUN',
    'IDN', 'IND', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR',
    'JPN', 'KAZ', 'KEN', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LBN', 'LBR',
    'LBY', 'LCA', 'LKA', 'LTU', 'LUX', 'LVA', 'MAR', 'MCO', 'MDA', 'MDG',
    'MDV', 'MEX', 'MHL', 'MKD', 'MLT', 'MMR', 'MNE', 'MNG', 'MOZ', 'MRT',
    'MUS', 'MWI', 'MYS', 'NAM', 'NGA', 'NIC', 'NLD', 'NOR', 'NPL', 'NRU',
    'NZL', 'OMN', 'PAK', 'PAN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRK',
    'PRT', 'PRY', 'QAT', 'ROU', 'RUS', 'SAU', 'SDN', 'SEN', 'SGP', 'SLB',
    'SLE', 'SLV', 'SMR', 'SOM', 'SRB', 'STP', 'SUR', 'SVK', 'SVN', 'SWE',
    'SYC', 'SYR', 'TGO', 'THA', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR',
    'TUV', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'VCT', 'VEN', 'VNM', 'VUT',
    'WSM', 'YEM', 'ZAF', 'ZMB', 'ZWE'
])

LDC = Group([
    'AFG', 'AGO', 'BDI', 'BEN', 'BFA', 'BGD', 'BTN', 'CAF', 'COD', 'COM',
    'DJI', 'ERI', 'ETH', 'GIN', 'GMB', 'GNB', 'HTI', 'KHM', 'KIR', 'LAO',
    'LBR', 'LSO', 'MDG', 'MLI', 'MMR', 'MOZ', 'MRT', 'MWI', 'NER', 'NPL',
    'RWA', 'SDN', 'SEN', 'SLB', 'SLE', 'SOM', 'SSD', 'STP', 'TCD', 'TGO',
    'TLS', 'TUV', 'TZA', 'UGA', 'YEM', 'ZMB'
])

LLDC = Group([
    'AFG', 'ARM', 'AZE', 'BDI', 'BFA', 'BOL', 'BTN', 'BWA', 'CAF', 'ETH',
    'KAZ', 'KGZ', 'LAO', 'LSO', 'MDA', 'MKD', 'MLI', 'MNG', 'MWI', 'NER',
    'NPL', 'PRY', 'RWA', 'SSD', 'SWZ', 'TCD', 'TJK', 'TKM', 'UGA', 'UZB',
    'ZMB', 'ZWE'
])

MONTREAL_PROTOCOL_HIGH_AMBIENT_TEMP = Group([
    'ARE', 'BEN', 'BFA', 'BHR', 'CAF', 'CIV', 'DJI', 'DZA', 'EGY', 'ERI',
    'GHA', 'GIN', 'GMB', 'GNB', 'IRN', 'IRQ', 'JOR', 'KWT', 'LBY', 'MLI',
    'MRT', 'NER', 'NGA', 'OMN', 'PAK', 'QAT', 'SAU', 'SDN', 'SEN', 'SYR',
    'TCD', 'TGO', 'TKM', 'TUN'
])

NON_ANNEX_ONE = Group([
    'AFG', 'AGO', 'ALB', 'AND', 'ARE', 'ARG', 'ARM', 'ATG', 'AZE', 'BDI',
    'BEN', 'BFA', 'BGD', 'BHR', 'BHS', 'BIH', 'BLZ', 'BOL', 'BRA', 'BRB',
    'BRN', 'BTN', 'BWA', 'CAF', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG',
    'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'DJI', 'DMA', 'DOM', 'DZA',
    'ECU', 'EGY', 'ERI', 'ETH', 'FJI', 'FSM', 'GAB', 'GEO', 'GHA', 'GIN',
    'GMB', 'GNB', 'GNQ', 'GRD', 'GTM', 'GUY', 'HND', 'HTI', 'IDN', 'IND',
    'IRN', 'IRQ', 'ISR', 'JAM', 'JOR', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KIR',
    'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LKA', 'LSO',
    'MAR', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MKD', 'MLI', 'MMR', 'MNE',
    'MNG', 'MOZ', 'MRT', 'MUS', 'MWI', 'MYS', 'NAM', 'NER', 'NGA', 'NIC',
    'NIU', 'NPL', 'NRU', 'OMN', 'PAK', 'PAN', 'PER', 'PHL', 'PLW', 'PNG',
    'PRK', 'PRY', 'PSE', 'QAT', 'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SLB',
    'SLE', 'SLV', 'SMR', 'SOM', 'SRB', 'SSD', 'STP', 'SUR', 'SWZ', 'SYC',
    'SYR', 'TCD', 'TGO', 'THA', 'TJK', 'TKM', 'TLS', 'TON', 'TTO', 'TUN',
    'TUV', 'TZA', 'UGA', 'URY', 'UZB', 'VCT', 'VEN', 'VNM', 'VUT', 'WSM',
    'YEM', 'ZAF', 'ZMB', 'ZWE'
])

OECD = Group([
    'AUS', 'AUT', 'BEL', 'CAN', 'CHE', 'CHL', 'COL', 'CRI', 'CZE', 'DEU',
    'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HUN', 'IRL', 'ISL',
    'ISR', 'ITA', 'JPN', 'KOR', 'LTU', 'LUX', 'LVA', 'MEX', 'NLD', 'NOR',
    'NZL', 'POL', 'PRT', 'SVK', 'SVN', 'SWE', 'TUR', 'USA'
])

OPEC = Group([
    'AGO', 'ARE', 'DZA', 'ECU', 'GAB', 'GNQ', 'IRN', 'IRQ', 'KWT', 'LBY',
    'NGA', 'QAT', 'SAU', 'VEN'
])

SIDS = Group([
    'ATG', 'BHS', 'BLZ', 'BRB', 'COM', 'CPV', 'CUB', 'DMA', 'DOM', 'FJI',
    'FSM', 'GNB', 'GRD', 'GUY', 'HTI', 'JAM', 'KIR', 'KNA', 'LCA', 'MDV',
    'MHL', 'MUS', 'NRU', 'PLW', 'PNG', 'SGP', 'SLB', 'STP', 'SUR', 'SYC',
    'TLS', 'TON', 'TTO', 'TUV', 'VCT', 'VUT', 'WSM'
])

SIDS_NON_UN_OR_REGIONAL_COMMISSIONS_ASSOCIATES = Group([
    'ABW', 'AIA', 'ASM', 'BMU', 'COK', 'CUW', 'CYM', 'GLP', 'GUM', 'MNP',
    'MSR', 'MTQ', 'NCL', 'NIU', 'PRI', 'PYF', 'SXM', 'TCA', 'VGB', 'VIR'
])

SSP = Group({
    'ASIA': [
        'AFG', 'BGD', 'BRN', 'BTN', 'CHN', 'FJI', 'FSM', 'HKG', 'IDN', 'IND',
        'KHM', 'KOR', 'LAO', 'LKA', 'MAC', 'MDV', 'MMR', 'MNG', 'MYS', 'NCL',
        'NPL', 'PAK', 'PHL', 'PNG', 'PRK', 'PYF', 'SGP', 'SLB', 'THA', 'TLS',
        'TWN', 'VNM', 'VUT', 'WSM'
    ],
    'LAM': [
        'ABW', 'ARG', 'BHS', 'BLZ', 'BOL', 'BRA', 'BRB', 'CHL', 'COL', 'CRI',
        'CUB', 'DOM', 'ECU', 'GLP', 'GRD', 'GTM', 'GUF', 'GUY', 'HND', 'HTI',
        'JAM', 'MEX', 'MTQ', 'NIC', 'PAN', 'PER', 'PRY', 'SLV', 'SUR', 'TTO',
        'URY', 'VEN', 'VIR'
    ],
    'MAF': [
        'AGO', 'ARE', 'BDI', 'BEN', 'BFA', 'BHR', 'BWA', 'CAF', 'CIV', 'CMR',
        'COD', 'COG', 'COM', 'CPV', 'DJI', 'DZA', 'EGY', 'ERI', 'ESH', 'ETH',
        'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'IRN', 'IRQ', 'ISR', 'JOR',
        'KEN', 'KWT', 'LBN', 'LBR', 'LBY', 'LSO', 'MAR', 'MDG', 'MLI', 'MOZ',
        'MRT', 'MUS', 'MWI', 'MYT', 'NAM', 'NER', 'NGA', 'OMN', 'PSE', 'QAT',
        'REU', 'RWA', 'SAU', 'SDN', 'SEN', 'SLE', 'SOM', 'SSD', 'SWZ', 'SYR',
        'TCD', 'TGO', 'TUN', 'TZA', 'UGA', 'YEM', 'ZAF', 'ZMB', 'ZWE'
    ],
    'OECD': [
        'ALB', 'AUS', 'AUT', 'BEL', 'BGR', 'BIH', 'CAN', 'CHE', 'CYP', 'CZE',
        'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'GUM', 'HRV',
        'HUN', 'IRL', 'ISL', 'ITA', 'JPN', 'LTU', 'LUX', 'LVA', 'MKD', 'MLT',
        'MNE', 'NLD', 'NOR', 'NZL', 'POL', 'PRI', 'PRT', 'ROU', 'SRB', 'SVK',
        'SVN', 'SWE', 'TUR', 'USA'
    ],
    'REF': [
        'ARM', 'AZE', 'BLR', 'GEO', 'KAZ', 'KGZ', 'MDA', 'RUS', 'TJK', 'TKM',
        'UKR', 'UZB'
    ]
})

UMBRELLA = Group(
    ['AUS', 'CAN', 'JPN', 'KAZ', 'NOR', 'NZL', 'RUS', 'UKR', 'USA'])

UN_REGIONAL_GROUPS = Group({
    'AFRICAN_GROUP': [
        'AGO', 'BDI', 'BEN', 'BFA', 'BWA', 'CAF', 'CIV', 'CMR', 'COD', 'COG',
        'COM', 'CPV', 'DJI', 'DZA', 'EGY', 'ERI', 'ETH', 'GAB', 'GHA', 'GIN',
        'GMB', 'GNB', 'GNQ', 'KEN', 'LBR', 'LBY', 'LSO', 'MAR', 'MDG', 'MLI',
        'MOZ', 'MRT', 'MUS', 'MWI', 'NAM', 'NER', 'NGA', 'RWA', 'SDN', 'SEN',
        'SLE', 'SOM', 'SSD', 'STP', 'SWZ', 'SYC', 'TCD', 'TGO', 'TUN', 'TZA',
        'UGA', 'ZAF', 'ZMB', 'ZWE'
    ],
    'ASIA_PACIFIC_GROUP': [
        'AFG', 'ARE', 'BGD', 'BHR', 'BRN', 'BTN', 'CHN', 'CYP', 'FJI', 'FSM',
        'IDN', 'IND', 'IRN', 'IRQ', 'JOR', 'JPN', 'KAZ', 'KGZ', 'KHM', 'KIR',
        'KOR', 'KWT', 'LAO', 'LBN', 'LKA', 'MDV', 'MHL', 'MMR', 'MNG', 'MYS',
        'NPL', 'NRU', 'OMN', 'PAK', 'PHL', 'PLW', 'PNG', 'PRK', 'QAT', 'SAU',
        'SGP', 'SLB', 'SYR', 'THA', 'TJK', 'TKM', 'TLS', 'TON', 'TUR', 'TUV',
        'UZB', 'VNM', 'VUT', 'WSM', 'YEM'
    ],
    'EASTERN_EUROPEAN_GROUP': [
        'ALB', 'ARM', 'AZE', 'BGR', 'BIH', 'BLR', 'CZE', 'EST', 'GEO', 'HRV',
        'HUN', 'LTU', 'LVA', 'MDA', 'MKD', 'MNE', 'POL', 'ROU', 'RUS', 'SRB',
        'SVK', 'SVN', 'UKR'
    ],
    'GRULAC': [
        'ARG', 'ATG', 'BHS', 'BLZ', 'BOL', 'BRA', 'BRB', 'CHL', 'COL', 'CRI',
        'CUB', 'DMA', 'DOM', 'ECU', 'GRD', 'GTM', 'GUY', 'HND', 'HTI', 'JAM',
        'KNA', 'LCA', 'MEX', 'NIC', 'PAN', 'PER', 'PRY', 'SLV', 'SUR', 'TTO',
        'URY', 'VCT', 'VEN'
    ],
    'WEOG': [
        'AND', 'AUS', 'AUT', 'BEL', 'CAN', 'CHE', 'DEU', 'DNK', 'ESP', 'FIN',
        'FRA', 'GBR', 'GRC', 'IRL', 'ISL', 'ISR', 'ITA', 'LIE', 'LUX', 'MCO',
        'MLT', 'NLD', 'NOR', 'NZL', 'PRT', 'SMR', 'SWE', 'TUR', 'USA'
    ]
})

UNFCCC = Group([
    'AFG', 'AGO', 'ALB', 'AND', 'ARE', 'ARG', 'ARM', 'ATG', 'AUS', 'AUT',
    'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH',
    'BLR', 'BLZ', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BWA', 'CAF', 'CAN',
    'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK', 'COL', 'COM',
    'CPV', 'CRI', 'CUB', 'CYP', 'CZE', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM',
    'DZA', 'ECU', 'EGY', 'ERI', 'ESP', 'EST', 'ETH', 'EUU', 'FIN', 'FJI',
    'FRA', 'FSM', 'GAB', 'GBR', 'GEO', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ',
    'GRC', 'GRD', 'GTM', 'GUY', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IND',
    'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ',
    'KEN', 'KGZ', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR',
    'LBY', 'LCA', 'LIE', 'LKA', 'LSO', 'LTU', 'LUX', 'LVA', 'MAR', 'MCO',
    'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE',
    'MNG', 'MOZ', 'MRT', 'MUS', 'MWI', 'MYS', 'NAM', 'NER', 'NGA', 'NIC',
    'NIU', 'NLD', 'NOR', 'NPL', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PER',
    'PHL', 'PLW', 'PNG', 'POL', 'PRK', 'PRT', 'PRY', 'PSE', 'QAT', 'ROU',
    'RUS', 'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SLB', 'SLE', 'SLV', 'SMR',
    'SOM', 'SRB', 'SSD', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SYC',
    'SYR', 'TCD', 'TGO', 'THA', 'TJK', 'TKM', 'TLS', 'TON', 'TTO', 'TUN',
    'TUR', 'TUV', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VAT', 'VCT',
    'VEN', 'VNM', 'VUT', 'WSM', 'YEM', 'ZAF', 'ZMB', 'ZWE'
])

UNSTATS_GEOGRAPHICAL_REGIONS = Group({
    "AFRICA": {
        "NORTHERN_AFRICA": ["DZA", "EGY", "ESH", "LBY", "MAR", "SDN", "TUN"],
        "SUB_SAHARAN_AFRICA": {
            "EASTERN_AFRICA": [
                "ATF", "BDI", "COM", "DJI", "ERI", "ETH", "IOT", "KEN", "MDG",
                "MOZ", "MUS", "MWI", "MYT", "REU", "RWA", "SOM", "SSD", "SYC",
                "TZA", "UGA", "ZMB", "ZWE"
            ],
            "MIDDLE_AFRICA":
            ["AGO", "CAF", "CMR", "COD", "COG", "GAB", "GNQ", "STP", "TCD"],
            "SOUTHERN_AFRICA": ["BWA", "LSO", "NAM", "SWZ", "ZAF"],
            "WESTERN_AFRICA": [
                "BEN", "BFA", "CIV", "CPV", "GHA", "GIN", "GMB", "GNB", "LBR",
                "MLI", "MRT", "NER", "NGA", "SEN", "SHN", "SLE", "TGO"
            ]
        }
    },
    "AMERICAS": {
        "LATIN_AMERICA_AND_THE_CARIBBEAN": {
            "CARIBBEAN": [
                "ABW", "AIA", "ATG", "BES", "BHS", "BLM", "BRB", "CUB", "CUW",
                "CYM", "DMA", "DOM", "GLP", "GRD", "HTI", "JAM", "KNA", "LCA",
                "MAF", "MSR", "MTQ", "PRI", "SXM", "TCA", "TTO", "VCT", "VGB",
                "VIR"
            ],
            "CENTRAL_AMERICA":
            ["BLZ", "CRI", "GTM", "HND", "MEX", "NIC", "PAN", "SLV"],
            "SOUTH_AMERICA": [
                "ARG", "BOL", "BRA", "BVT", "CHL", "COL", "ECU", "FLK", "GUF",
                "GUY", "PER", "PRY", "SGS", "SUR", "URY", "VEN"
            ]
        },
        "NORTHERN_AMERICA": ["BMU", "CAN", "GRL", "SPM", "USA"]
    },
    "ANTARCTICA": ["ATA"],
    "ASIA": {
        "CENTRAL_ASIA": ["KAZ", "KGZ", "TJK", "TKM", "UZB"],
        "EASTERN_ASIA": ["CHN", "HKG", "JPN", "KOR", "MAC", "MNG", "PRK"],
        "SOUTHERN_ASIA":
        ["AFG", "BGD", "BTN", "IND", "IRN", "LKA", "MDV", "NPL", "PAK"],
        "SOUTH_EASTERN_ASIA": [
            "BRN", "IDN", "KHM", "LAO", "MMR", "MYS", "PHL", "SGP", "THA",
            "TLS", "VNM"
        ],
        "WESTERN_ASIA": [
            "ARE", "ARM", "AZE", "BHR", "CYP", "GEO", "IRQ", "ISR", "JOR",
            "KWT", "LBN", "OMN", "PSE", "QAT", "SAU", "SYR", "TUR", "YEM"
        ]
    },
    "EUROPE": {
        "EASTERN_EUROPE":
        ["BGR", "BLR", "CZE", "HUN", "MDA", "POL", "ROU", "RUS", "SVK", "UKR"],
        "NORTHERN_EUROPE": [
            "ALA", {
                "CHANNEL_ISLANDS": ["GGY", "JEY"]
            }, "DNK", "EST", "FIN", "FRO", "GBR", "IMN", "IRL", "ISL", "LTU",
            "LVA", "NOR", "SJM", "SWE"
        ],
        "SOUTHERN_EUROPE": [
            "ALB", "AND", "BIH", "ESP", "GIB", "GRC", "HRV", "ITA", "MKD",
            "MLT", "MNE", "PRT", "SMR", "SRB", "SVN", "VAT"
        ],
        "WESTERN_EUROPE":
        ["AUT", "BEL", "CHE", "DEU", "FRA", "LIE", "LUX", "MCO", "NLD"]
    },
    "OCEANIA": {
        "AUSTRALIA_AND_NEW_ZEALAND":
        ["AUS", "CCK", "CXR", "HMD", "NFK", "NZL"],
        "MELANESIA": ["FJI", "NCL", "PNG", "SLB", "VUT"],
        "MICRONESIA": ["FSM", "GUM", "KIR", "MHL", "MNP", "NRU", "PLW", "UMI"],
        "POLYNESIA":
        ["ASM", "COK", "NIU", "PCN", "PYF", "TKL", "TON", "TUV", "WLF", "WSM"]
    }
})
MONTREAL_PROTOCOL_COUNTRIES = Group({
    "ARTICLE_5": {
        "GROUP_1": [
            "AFG", "AGO", "ALB", "ARG", "ARM", "ATG", "BDI", "BEN", "BFA",
            "BGD", "BHS", "BIH", "BLZ", "BOL", "BRA", "BRB", "BRN", "BTN",
            "BWA", "CAF", "CHL", "CHN", "CIV", "CMR", "COD", "COG", "COK",
            "COL", "COM", "CPV", "CRI", "CUB", "DJI", "DMA", "DOM", "DZA",
            "ECU", "EGY", "ERI", "ETH", "FJI", "FSM", "GAB", "GEO", "GHA",
            "GIN", "GMB", "GNB", "GNQ", "GRD", "GTM", "GUY", "HND", "HTI",
            "IDN", "JAM", "JOR", "KEN", "KGZ", "KHM", "KIR", "KNA", "KOR",
            "LAO", "LBN", "LBR", "LBY", "LCA", "LKA", "LSO", "MAR", "MDA",
            "MDG", "MDV", "MEX", "MHL", "MKD", "MLI", "MMR", "MNE", "MNG",
            "MOZ", "MRT", "MUS", "MWI", "MYS", "NAM", "NER", "NGA", "NIC",
            "NIU", "NPL", "NRU", "PAN", "PER", "PHL", "PLW", "PNG", "PRK",
            "PRY", "PSE", "RWA", "SDN", "SEN", "SGP", "SLB", "SLE", "SLV",
            "SOM", "SRB", "SSD", "STP", "SUR", "SWZ", "SYC", "SYR", "TCD",
            "TGO", "THA", "TKM", "TLS", "TON", "TTO", "TUN", "TUR", "TUV",
            "TZA", "UGA", "URY", "VCT", "VEN", "VNM", "VUT", "WSM", "YEM",
            "ZAF", "ZMB", "ZWE"
        ],
        "GROUP_2":
        ["ARE", "BHR", "IND", "IRN", "IRQ", "KWT", "OMN", "PAK", "QAT", "SAU"]
    },
    "NON_ARTICLE_5": {
        "NON_ARTICLE_5_EXCEPTIONS": ["BLR", "KAZ", "RUS", "TJK", "UZB"],
        "NON_ARTICLE_5_MAIN_GROUP": [
            "AND", "AUS", "AUT", "AZE", "BEL", "BGR", "CAN", "CHE", "CYP",
            "CZE", "DEU", "DNK", "ESP", "EST", "EUU", "FIN", "FRA", "GBR",
            "GRC", "HRV", "HUN", "IRL", "ISL", "ISR", "ITA", "JPN", "LIE",
            "LTU", "LUX", "LVA", "MCO", "MLT", "NLD", "NOR", "NZL", "POL",
            "PRT", "ROU", "SMR", "SVK", "SVN", "SWE", "UKR", "USA", "VAT"
        ]
    }
})
