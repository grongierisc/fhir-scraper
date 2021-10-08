
#!/usr/bin/env python

from fhirpy import SyncFHIRClient
import requests
import logging

def main():
    """
    A little command line tool to crawl/scrap a FHIR repository to a new one.
    You must specify the url of the source repository and the target repository.
    """

    ### Source Repository
    urlClient = "http://localhost:52773/fhir/r4/"
    ### Source authorization key
    source_authorization=None

    ### Destination Repository
    urlServer = "http://localhost:32783/fhir/r4/"
    ### Destination authorization
    target_authorization=None

    ### List of resource to fetch
    p_resources=None

    ### Limit the number of resource
    p_limit=100

    # Create the source instance
    client = SyncFHIRClient(
        urlClient,source_authorization,extra_headers={'Content-Type':'application/fhir+json'}
    )

    server = SyncFHIRClient(
        urlServer,target_authorization,extra_headers={'Content-Type':'application/fhir+json'}
    )

    types = getResourceType(urlClient) if p_resources is None else p_resources

    for type in types:
        logging.info(type)
        try:
            resources = client.resources(type)
            # limit of resources 
            limit = 10 if p_limit is None else p_limit
            for resource in resources.limit(limit):
                print(resource.resource_type+'/'+resource.id)
                serverResource = server.resource(resource.resource_type)
                # map source to destination
                for key, value in resource.items():
                    # transform it
                    key, value = transform(key,value)
                    if key is not None:
                        setattr(serverResource,key,value)
                logging.info(serverResource.serialize())
                # save it to the destination
                serverResource.save()
        except Exception as e:
            logging.error(e)
            pass

## Get Resource all Resource type from a FHIR endpoint
def getResourceType(url):
    response = requests.get(url+"metadata")
    metadata  = response.json()
    resourcesType = list()
    for value in metadata["rest"][0]["resource"]:
        resourcesType.append(value["type"])
    return resourcesType

## Transfom source to destination if needed
def transform(key,value):
    ## replace id with _ to -
    if key == 'id':
        return key,value.replace("_","-")
    ## remove endpoint
    if key == 'endpoint':
        return None,None
    ## untouch
    else:
        return key,value

if __name__ == '__main__':
    main()

