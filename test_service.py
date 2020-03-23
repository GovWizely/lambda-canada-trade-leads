import vcr

from service import get_entries


@vcr.use_cassette()
def test_get_entries():
    """Reads from the `test_get_entries` cassette and processes the entries.
    """
    entries = get_entries()
    assert len(entries) == 633
    print(entries[0])
    expected_entry = {
        "language": "English",
        "title": "Social Media Monitoring (EN578-141760/B)",
        "reference_number": "PW-$$CY-007-64441",
        "solicitation_number": "EN578-141760/B",
        "amendment_number": "002",
        "publication_date": "2014-01-20",
        "date_closing": "2021-01-29 14:00 Eastern Standard Time (EST)",
        "amendment_date": "2019-12-02",
        "publishing_status": "Active",
        "gsin": "T004KA - Social Media Monitoring",
        "region_opportunity": "",
        "region_delivery": "Alberta, British Columbia, Manitoba, National Capital Region, "
        "New Brunswick, Newfoundland and Labrador, Northwest Territories, "
        "Nova Scotia, Nunavut, Ontario, Prince Edward Island, Quebec, "
        "Saskatchewan, Yukon",
        "notice_type": "APM-NPP",
        "trade_agreement": "Canadian Free Trade Agreement (CFTA)",
        "tendering_procedure": "The bidder must supply Canadian goods and/or services",
        "competitive_procurement_strategy": "Subsequent/Follow-on Contracts",
        "non_competitive_procurement_strategy": "",
        "procurement_entity": "Public Works and Government Services Canada",
        "end_user_entity": "Public Works and Government Services Canada",
        "description": "Trade Agreement: Canadian Free Trade Agreement (CFTA) Tendering "
        "Procedures: The bidder must supply Canadian goods and/or services "
        "Competitive Procurement Strategy: Subsequent/Follow-on Contracts "
        "Comprehensive Land Claim Agreement: No Nature of Requirements:        "
        "Delivery Date: Above-mentioned  The Crown retains the right to negotiate "
        "with suppliers on any procurement.  Documents may be submitted in either "
        "official language of Canada.",
        "access_terms_of_use": 'Procurement data carries an "Open Government Licence - Canada" '
        "that governs its use. Please refer to the section about "
        'Commercial Reproduction in the Buyandsell.gc.ca "Terms and '
        'Conditions" for more information.',
        "contact": "Richard, Josette, josette.richard@tpsgc-pwgsc.gc.ca, (613) 990-5858 ( ), "
        "360 Albert St./ 360, rue Albert 12th Floor / 12ième étage Ottawa Ontario K1A "
        "0S5, 360 Albert St./ 360, rue Albert 12th Floor / 12ième étage Ottawa Ontario "
        "K1A 0S5",
        "document": "https://buyandsell.gc.ca/cds/public/2014/01/17"
        "/e7a31ca7070b9aa566f700a119af2564/ABES.PROD.PW__CY.B007.E64441.EBSU000.PDF, "
        "https://buyandsell.gc.ca/cds/public/2014/01/17"
        "/26e2138a386a491d75701a9f9c29af8f/ABES.PROD.PW__CY.B007.F64441.EBSU000.PDF, "
        "https://buyandsell.gc.ca/cds/public/2019/01/31"
        "/0de45f938d13bfa165fc78980e01b6fe/ABES.PROD.PW__CY.B007.E64441.EBSU001.PDF, "
        "https://buyandsell.gc.ca/cds/public/2019/01/31"
        "/7f4b16c8e7733f78bc92fb9b3cc20e5e/ABES.PROD.PW__CY.B007.F64441.EBSU001.PDF, "
        "https://buyandsell.gc.ca/cds/public/2019/11/29"
        "/8310ce0aa690eea9983c35232b46133c/ABES.PROD.PW__CY.B007.E64441.EBSU002.PDF, "
        "https://buyandsell.gc.ca/cds/public/2019/11/29"
        "/5b02fa84f5d2c320b5e65511a19b91b6/ABES.PROD.PW__CY.B007.F64441.EBSU002.PDF",
        "attachment": "",
    }
    assert entries[0] == expected_entry
