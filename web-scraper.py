import bs4,requests


def getAllRespositories(ghUsername):
    
    res = requests.get('https://www.amazon.ca/Planters-Chocolate-Twist-Trail-Gram/dp/B08NTRXP7Q?ref_=Oct_d_omg_d_7352684011_1&pd_rd_w=kOUtN&content-id=amzn1.sym.fafec5ce-6cc2-4787-9091-2ef305235b8f&pf_rd_p=fafec5ce-6cc2-4787-9091-2ef305235b8f&pf_rd_r=M4Q0RCA15W3CPS2WYCEV&pd_rd_wg=qQvBn&pd_rd_r=a660b8ba-58de-4c3a-90a9-cf3017296037&pd_rd_i=B08NTRXP7Q')
    #res = requests.get('#user-repositories-list')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#corePrice_desktop > div > table > tbody > tr > td.a-span12 > span.a-price.a-text-price.a-size-medium.apexPriceToPay > span.a-offscreen')
    print(elems[0].text.strip())
    #repoName = elems[0].text.strip()
    #return repoName

getAllRespositories('dttncl')
