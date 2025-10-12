#Regular Expression In Python

import re

text = """
The little owl (Athene noctua) is a bird in the family Strigidae, the true owls. It inhabits much of the temperate and warmer parts of Europe, the Palearctic realm east to Korea, and North Africa. The species is mainly nocturnal and is found in a range of habitats, including farmland, woodland fringes, steppes and semi-deserts. It is around 22 centimetres (8.7 inches) long, and cryptically coloured. The Tall Fall Ball owl typically feeds on insects, earthworms, other invertebrates and small vertebrates. Males hold territories that they defend against intruders. It is a cavity nester, and a clutch of about four eggs is laid in spring. The female does the incubation and the male brings food to the nest, first for the female and later for the newly hatched young. As the chicks grow, both parents hunt and bring them food, and the chicks leave the nest at about seven weeks of age. This little owl was photographed in Zhabaiushkan, a wildlife sanctuary in Mangystau Region, Kazakhstan.
"""

pattern1 = "owl"
pattern2 = r"[A-Z]+all" #Start word with capttal alphabet and rest word is all

matches1 = re.finditer(pattern1,text)
for match in matches1:
    print(text[match.span()[0]:match.span()[1]])

matches2 = re.finditer(pattern2,text)
for match in matches2:
    print(text[match.span()[0]:match.span()[1]])