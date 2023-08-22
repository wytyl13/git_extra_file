import os
import xml.etree.ElementTree as ET



def remove_duplicate_labels(xml_in_path):
    tree = ET.parse(xml_in_path)
    root = tree.getroot()
    existing_labels = {}
    total = 0
    count = 0
    for object_elem in root.findall('object'):
        total += 1
        name_elem = object_elem.find('bndbox')
        if name_elem is not None:
            s = ','.join(box.text for box in name_elem)
            if existing_labels.get(s):
                root.remove(object_elem)  # Remove the duplicate entry
                count += 1
            else:
                existing_labels[s] = True
    print(f'total {total} object labels, have found {count} duplicate object lables, removed successfully!!! rest {total - count} object labels')
    tree.write(xml_in_path)

def remove_duplicates_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            xml_path = os.path.join(directory, filename)
            remove_duplicate_labels(xml_path)



if __name__ == "__main__":
    remove_duplicates_in_directory('data/to_train_data/image_voc')