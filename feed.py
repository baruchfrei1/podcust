import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml','r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss',{
        'version':'2.0'
    })
channel_element = xml_tree.SubElement(rss_element,'channel')
link_prefix = yaml_data['link']
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'link').text = link_prefix

output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml',encoding='UTF-8',xml_declaration=True)