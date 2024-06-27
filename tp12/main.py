import xml.etree.ElementTree as ET

def main():
    xml_file = "customers.xml"
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # for child in root:
    #     print(child.tag, child[1].text)
    # //*[@id="12"]
    customers = tree.findall('//customer')
    for customer in customers:
        print(customer.find('id').text)
        print(customer.find('last_name').text)
        print(customer.find('first_name').text)
    
    customer = tree.find('.//customer[id="12"]')
    print(customer.find('id').text)
    print(customer.find('last_name').text)
    print(customer.find('first_name').text)

if __name__=='__main__':
    main()
