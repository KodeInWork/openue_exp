## API 1 : Relational Triple Extraction

Input: sentence

Output: relational triples

```
GET openue.top:8887/IEDemo?q=Inception is a 2010 science fiction action film written and directed by Christopher Nolan, who also produced the film with his wife, Emma Thomas. 
```

parameters

|parameter|description|is necessary|default|
|:----|:------|:-----|:----|
|q |input sentence | necessary | None|

Examples1:

```
GET /?q=Inception is a 2010 science fiction action film written and directed by Christopher Nolan, who also produced the film with his wife, Emma Thomas. 
```

Results:

```json
{"0": {"text": "Inception is a 2010 science fiction action film written and directed by Christopher Nolan, who also produced the film with his wife, Emma Thomas..", "spo_list": [{"predicate": "P57", "object": " christopher nolan", "subject": " inception"}, {"predicate": "P136", "object": " science fiction", "subject": " inception"}, {"predicate": "P136", "object": " action film", "subject": " inception"}], "rel_time": 214, "ent_time": 625, "total_time": 841, "class_prob": [0.00112232519, 2.4856e-05, 6.97949872e-05, 0.0249631833, 0.986882269, 0.000130208136, 0.000879697094, 0.190037325, 0.00128584856, 0.000393838505, 0.000136892166, 0.000651476148, 0.000280235283, 0.000413141563, 0.00415658345, 0.0186637845, 0.00428134389, 0.00241552806, 0.000191932821, 7.44582503e-05, 4.49884028e-05, 0.00350840297, 0.000483950309, 0.00764138903, 0.000803668459, 0.000682095531, 0.00027463556, 8.34275124e-05, 0.000153202898, 0.00836379454, 0.000969863788, 0.000123517835, 0.00161897822, 0.00122919271, 0.00101010362, 0.000208550933, 0.000235763728, 0.0450608768, 0.00768747646, 2.66087318e-05, 0.00122022443, 0.00114414527, 0.000109865985, 0.617734, 9.99656768e-05, 0.0179543421, 0.027340224, 0.0986918, 2.16867247e-05, 9.74370505e-06, 0.00283915969, 0.00518612238, 0.00757851824, 0.000261425, 0.00272235321, 4.2401356e-05, 3.72452305e-05, 0.0106186029, 6.49549693e-05, 0.000940858677, 0.167479485, 0.908121586, 0.000575952348, 8.30486533e-05, 0.064847, 0.0113750212, 3.76322823e-05, 0.0241856314, 0.0132566178, 0.000127468709, 7.78985195e-05, 0.000964459323, 0.00428855792, 0.00938831, 0.00754940929, 1.06171665e-05, 0.000620784587, 0.000124733619, 3.93251066e-05, 0.00299555482, 0.00214794534, 3.68823057e-05, 0.00811619777, 8.02657669e-05, 0.000137539828, 0.000150308915, 0.000906060566, 0.000253911538, 0.000613037322, 0.000100710742, 0.00120162067, 0.000751681568, 0.00284342491, 0.00846523605, 0.000546438678, 0.00391289406, 0.000133764974, 0.000887748669, 0.000105449581, 5.14393214e-05, 0.00301302806, 4.62121461e-05, 0.00027344859, 6.62134e-06, 0.000285569404, 0.146206692, 2.59205462e-05, 0.0003790583, 0.000451401196, 0.000731941254, 1.93259766e-05, 0.00118862197, 3.43825704e-05, 0.000449988584, 0.000189156752, 0.000338619458, 0.000423043704, 0.000693866576, 0.00933917239, 0.000144736317, 6.3492269e-05, 0.0110616963, 0.130006671, 0.0016186384, 0.00102970924, 0.00243263762, 0.000487385347, 0.00701257214, 0.000395923416, 0.00246482948, 7.00242526e-05, 0.000196811234, 0.00182174845, 0.000409391825, 0.000844975235, 2.63066377e-05, 3.24174434e-05, 0.00313158776, 2.32407419e-05, 5.16798e-05, 5.02284274e-06, 0.000239480374, 0.00100019469, 0.00316977967, 6.82205064e-05, 0.00120566203, 0.000363008061, 0.000163564342, 0.000580702967, 8.72197488e-05, 0.000196972876, 0.000125215069, 0.000132322428, 4.0848e-05, 0.000255590858, 0.000340919447, 0.000229776677, 8.42828813e-05, 0.000962943945, 0.000383722101, 5.19002206e-05, 0.0021156359, 0.000137802112, 0.00017052496, 0.000959898229, 0.000128495158, 0.00490857475, 7.27178776e-05, 0.00979684293, 0.00022459618, 0.000451155385, 0.000374785595, 0.000455711037, 2.42516471e-05, 9.90259286e-05, 3.66387358e-05, 0.00126448821, 0.000676867377, 0.000327227841, 0.000205668854, 8.30579229e-05, 0.000112750597, 0.000459019, 0.0132894358, 0.00558181712, 0.000290840515, 7.8109988e-05, 0.000183862736, 0.00859205518, 0.00604599481, 2.93159555e-05, 9.46339205e-05, 4.55504269e-05, 0.000640067097, 9.09956e-05, 1.88325721e-05, 7.14742e-05, 8.59136e-05, 0.000112276699, 8.32896767e-05, 0.000820702466, 0.000479619688, 0.000355586351, 8.2243685e-05, 3.86454e-05, 5.44399736e-05, 0.000238746477, 1.9200892e-05, 8.46336261e-05, 0.000148406674, 5.40195833e-05, 0.000167175589, 9.04122862e-05, 0.000345843699, 2.40531517e-05, 3.54819349e-05, 5.40262808e-05, 3.41126688e-05, 9.34421842e-05, 0.000171952488, 7.67843449e-06, 7.14604321e-05, 5.32309969e-05, 7.71546474e-05, 1.68505267e-05, 8.16560205e-05, 0.000281624321, 0.000106558444, 8.83595203e-05, 4.44423349e-05, 0.000608328381, 0.000240512352, 8.46554485e-06, 4.39537944e-05, 0.0056119361, 0.000125911538, 7.416671e-05, 0.00080409128, 0.000111950962, 2.93752855e-05, 2.12848645e-05, 3.17938175e-05, 6.46426706e-05, 5.17737717e-05, 0.00107210199, 5.61812667e-05, 0.000100172838, 9.2168535e-05, 5.52493148e-05, 0.000174613087, 0.000434173126, 3.74280316e-05, 2.30441237e-05, 0.000248381839, 0.00060049945, 2.8679231e-05, 9.87689054e-06, 0.00112582347, 5.91664975e-05, 0.000116689116, 0.000180487419, 0.000252734579, 4.38138923e-05, 2.69645698e-05, 4.43594727e-05, 0.000162075943, 5.49082215e-05, 8.7096e-05, 9.36516299e-05, 5.1171728e-06, 0.00108956499, 6.85512e-05, 4.88868172e-05, 0.000100003243, 0.00013204047, 2.35751795e-05, 8.36291947e-05, 0.000103874707, 2.52537266e-05, 1.25451688e-05, 2.60545985e-05, 0.000215595966, 5.37186024e-05, 1.52544226e-05, 8.95579e-05, 6.15221e-05, 7.65884215e-06, 3.39463513e-05, 4.15925351e-05, 0.000108034008, 9.09807641e-05, 8.754173e-06, 0.000107674452, 5.86598617e-05, 6.07088659e-05, 5.74889855e-05, 3.26564877e-05, 0.000346064335, 3.48321628e-05, 4.07039297e-05, 3.44037908e-05, 4.07299085e-05, 6.2809966e-05, 4.08842061e-05, 2.21120845e-05, 4.46244849e-05, 7.71102132e-05, 1.81273808e-05, 1.10638384e-05, 9.9284618e-05, 2.20278525e-05, 6.89504086e-05, 2.20774236e-05, 1.59689189e-05, 0.000119353856, 4.86008184e-06, 1.51280374e-05, 4.79663649e-05, 1.35599958e-05, 2.32098e-05, 4.33131718e-05, 1.25659199e-05, 2.02931224e-05, 4.27897976e-06, 3.73870753e-05, 1.29975433e-05, 2.99099702e-05, 5.50465484e-06, 1.77615893e-05, 1.1334505e-05, 3.22155483e-06, 2.4718167e-05, 1.58237799e-05, 2.27622604e-05, 1.04432593e-05, 2.75187595e-05, 4.47301318e-06, 1.84490309e-05, 4.12591316e-06, 9.04769604e-06, 4.23768579e-05, 5.93886507e-05, 2.77522049e-05, 2.32195634e-05, 2.57331903e-05, 2.67335145e-05, 5.09761448e-05, 8.04250794e-06, 2.50838661e-06, 1.02204194e-05, 4.60166302e-06, 4.76317655e-06], "token_pred": [["[CLS]", "B-SUB", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-OBJ", "I-OBJ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "[SEP]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[SEP]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]"], ["[CLS]", "B-SUB", "O", "O", "O", "B-OBJ", "I-OBJ", "B-OBJ", "I-OBJ", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "[SEP]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[SEP]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]"], ["[CLS]", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-OBJ", "I-OBJ", "O", "O", "O", "O", "O", "O", "O", "O", "[SEP]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[category]", "[SEP]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]", "[Padding]"]]}}
```


