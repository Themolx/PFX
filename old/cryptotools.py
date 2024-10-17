import nuke
import re

def detect_crypto_layer(node):
    expression = node['expression'].value()
    match = re.search(r'VRayCryptomatte(\w+)00\.red', expression)
    if match:
        return f"VRayCryptomatte{match.group(1)}"
    return node['cryptoLayer'].value()

def process_cryptomattes():
    processed_nodes = 0
    mismatched_nodes = 0
    for node in nuke.allNodes('Cryptomatte'):
        current_layer = node['cryptoLayer'].value()
        detected_layer = detect_crypto_layer(node)
        
        if current_layer != detected_layer:
            mismatched_nodes += 1
        
        node['cryptoLayer'].setValue(detected_layer)
        node['cryptoLayerLock'].setValue(True)
        
        if detected_layer.startswith('VRayCryptomatte'):
            label = detected_layer[len('VRayCryptomatte'):]
        else:
            label = detected_layer
        
        node['label'].setValue(label)
        processed_nodes += 1

    nuke.message(f"Processed {processed_nodes} Cryptomatte nodes.\n"
                 f"- All Cryptos are locked!\n"
                 f"- All Labels and Layers updated based on keyer expressions!\n"
                 f"- Found {mismatched_nodes} nodes with mismatched layers.")

if __name__ == "__main__":
    process_cryptomattes()
