stocks = {'ICBP': 'Indofood CBP Sukses Makmur Tbk.',
 'CPIN': 'Charoen Pokphand Indonesia Tbk',
 'INDF': 'Indofood Sukses Makmur Tbk.',
 'MYOR': 'Mayora Indah Tbk',
 'CMRY': 'Cisarua Mountain Dairy Tbk.',
 'GOOD': 'Garudafood Putra Putri Jaya Tbk.',
 'MLBI': 'Multi Bintang Indonesia Tbk.',
 'PANI': 'Pratama Abadi Nusa Industri Tbk.',
 'JPFA': 'Japfa Comfeed Indonesia Tbk.',
 'AALI': 'Astra Agro Lestari Tbk.',
 'ULTJ': 'Ultra Jaya Milk Industry & Trading Company Tbk.',
 'FAPA': 'PT FAP Agri Tbk',
 'SMAR': 'Sinar Mas Agro Resources and Technology Tbk',
 'SSMS': 'Sawit Sumbermas Sarana Tbk.',
 'STAA': 'Sumber Tani Agung Resources Tbk.',
 'STTP': 'Siantar Top Tbk.',
 'ROTI': 'Nippon Indosari Corpindo Tbk.',
 'LSIP': 'PP London Sumatra Indonesia Tbk.',
 'TLDN': 'Teladan Prima Agro Tbk.',
 'SIMP': 'Salim Ivomas Pratama Tbk.',
 'PALM': 'Provident Agro Tbk.',
 'CLEO': 'Sariguna Primatirta Tbk',
 'DSNG': 'Dharma Satya Nusantara Tbk.',
 'ADES': 'Akasha Wira International Tbk.',
 'WMPP': 'Widodo Makmur Perkasa Tbk.',
 'TBLA': 'Tunas Baru Lampung Tbk.',
 'CPRO': 'Central Proteina Prima Tbk',
 'SGRO': 'Sampoerna Agro Tbk.',
 'BISI': 'BISI International Tbk.',
 'FISH': 'FKS Multi Agro Tbk.',
 'PSGO': 'Palma Serasih Tbk.',
 'JARR': 'Jhonlin Agro Raya Tbk.',
 'DLTA': 'Delta Djakarta Tbk',
 'MGRO': 'Mahkota Group Tbk.',
 'ANJT': 'Austindo Nusantara Jaya Tbk.',
 'BWPT': 'Eagle High Plantations Tbk.',
 'KEJU': 'Mulia Boga Raya Tbk.',
 'TRGU': 'Cerestar Indonesia Tbk.',
 'CAMP': 'Campina Ice Cream Industry Tbk.',
 'WMUU': 'Widodo Makmur Unggas Tbk',
 'MAIN': 'Malindo Feedmill Tbk.',
 'CEKA': 'Wilmar Cahaya Indonesia Tbk.',
 'CSRA': 'Cisadane Sawit Raya Tbk',
 'AISA': 'FKS Food Sejahtera Tbk.',
 'HOKI': 'Buyung Poetra Sembada Tbk'}

def get_stock_name(query: str):
    """
    reference: https://stackoverflow.com/questions/17106819/accessing-python-dict-values-with-the-key-start-characters
    """
    return {k:v for k, v in stocks.items() if k.startswith(query)}