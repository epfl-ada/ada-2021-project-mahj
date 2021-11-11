from urllib.parse import urlparse
from tld import get_tld

def extract_domain(url):
    """
    Extract domain of an url
    """
    url_pruned = urlparse(url).netloc
    tld = get_tld(url, as_object=True).tld
    url_no_tld = url_pruned.replace('.'+tld,"")
    domain = url_no_tld.split('.')[-1]

    return domain