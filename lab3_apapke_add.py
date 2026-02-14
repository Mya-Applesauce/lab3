"""
Lab3_apapke_add
Ari Papke
List addition
02/09/26
"""

from lab3_apapke_list import sonic_characters


sonic_characters.extend(('espio', 'vector', 'charmy', 'tangle', 'whisper'))
sonic_characters.sort(reverse=True)

if __name__ == "__main__":
    print(sonic_characters)