def domain_name(url):
    """
    Write a function that when given a URL as a string, 
    parses out just the domain name and returns it as a string.
    """
    
    domain_name = ""
    domain_extracted = ""
    try:
        # Create list of scheme to be removed
        scheme_to_remove = ["http://", "https://", "www.", "https://www.", "http://www."]
        
        domain_extracted = url 
        
        # Loop over each scheme and check if the parameter "url" contains the scheme
        for scheme in scheme_to_remove:
                
            if scheme in url:
                # Strip the scheme from url, e.g. www.xyz.com or http://xyz.com => xyz.com
                domain_extracted = url.replace(scheme, "")

                # Find the index of dot of the top-level domain
                first_occurance_of_dot = domain_extracted.find(".")
                
                # Get string before the top-level domain
                domain_name = domain_extracted[0:first_occurance_of_dot]
        
        else:
            # Find the index of dot of the top-level domain
            first_occurance_of_dot = domain_extracted.find(".")

            # Get string before the top-level domain
            domain_name = domain_extracted[0:first_occurance_of_dot]
            
    finally:
        return domain_name