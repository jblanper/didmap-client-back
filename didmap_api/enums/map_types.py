from .name_enum import NameEnum

class MapTypes(str, NameEnum):
    """
    Enum with the ids of the different map types used in Didactalia
    """
    # physical maps
    relief = "gnoss:B07B35CD-FBDA-4CD4-ACF3-5AF1C9B34547"
    rivers = "gnoss:9139A58D-E943-4D40-B5FB-2B7DEE8784A8"
    costs = "gnoss:F6266149-80EF-4F43-B369-3D9C3281E981"
    lakes = "gnoss:95AFC0F8-8917-4CCD-BB41-DDBDD1519E3C"
    oceans = "gnoss:6DF17D1F-D3E8-42BD-B86A-06EC5F2A33E9"
    peninsulas = "gnoss:7BD1C70E-7822-4DB7-958C-817761556B65"
    islands = "gnoss:5F8F6964-E0F3-433B-AB47-83A05E4B88C4"
    volcanoes = "gnoss:B36AAC12-310E-48C2-BA0B-D27BA3C7D3E5"
    deserts = "gnoss:50886369-5584-4E83-8889-A2958BB77885"

    # political maps
    countries = "gnoss:8436956D-44B4-477A-9102-F7CEBB1E2824"
    autonomous_communities = "gnoss:9474AD03-EB00-4855-91D0-26B0FD07D09A"
    provinces = "gnoss:1BB7EBCB-BED4-4CDE-A0B3-012D5DA54DFD"
    continents = "gnoss:EB446A75-F0D8-4BB3-947F-71C26A1A31F9"
    european_union = "gnoss:804FAB12-13F7-4D38-857E-B848805C278F"
    capitals = "gnoss:1D78659A-3FCD-4816-A1B3-8D37DE40EE38"
    comarcas = "gnoss:29894969-BBE7-46D7-8EB2-A9F253F7454C"
    states = "gnoss:99C36976-61F5-4A3B-ACFF-44E269B6C4A7"
    departments = "gnoss:5C996514-F2F6-4AAF-A749-0C5C1F28541C"
    regions = "gnoss:34B98298-6D1D-4708-9C1E-66E19DD2B084"
    districts = "gnoss:EF722A07-0E9E-48B2-ACB0-B37D371CE08C"
    territories = "gnoss:3EC81EF3-764C-45A2-9718-5B25C1B8B807"
    prefectures = "gnoss:42389F3E-00FF-4CE7-92AC-126A249A914D"
    cities = "gnoss:5DE1D009-737C-44A3-B7E9-344903BCEA1D"
    olympic_games = "gnoss:6C0204FC-BD3A-48FE-BF37-3FBCF1A1A961"

    # other maps
    maps_of_demonyms = "gnoss:D79E8E35-3B9A-4CFC-8077-DD421FA37B4E"
    environmental_maps = "gnoss:B159DAB0-CCA5-4DE2-80E6-2780E4B5AEDC"
    natural_areas = "gnoss:2427C3CF-F3E9-4FD2-852C-EE507D4F8151"
    climate = "gnoss:F63E6DCC-FFC5-45B0-9C28-BFBC1A942BA2"
    historical_maps = "gnoss:8E5F4C50-615F-470B-A181-1F96BB423F25"
    ancient_maps = "gnoss:91B8D66C-DDF5-494E-A7C3-A5C9EFC68058"
    archaeological_maps = "gnoss:E0182134-E67C-4DEF-B19E-63A115580C51"
    historical_milestones = "gnoss:C456B2DC-DABD-4E33-ADBA-85D87EFB1B3C"
    battles = "gnoss:D170CE2D-5CEF-4196-AB09-D36FDFB1A36C"
    gastronomic_maps = "gnoss:56DA7AC0-9A6B-43AC-8C7F-E93D0435A3E4"
    tourist_maps = "gnoss:6F3E60BE-194A-4022-B6E4-EDA53AE954CC"
    traditions = "gnoss:45D2B5A1-A1E4-4461-A41C-AE116CE4FB25"
    cultural_heritage = "gnoss:DECEC7E7-AE55-4C7D-961B-8F674100F7CD"
    entertainment = "gnoss:ED183271-C0BD-4C83-A18A-EF3DCE06D176"