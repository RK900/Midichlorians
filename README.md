# Midichlorians
[![Python27](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/download/releases/2.7/)
[![Python34](https://img.shields.io/badge/python-3.3+-cecb00.svg)](https://www.python.org/download/releases/3.4.0/)
[![License](https://img.shields.io/cocoapods/l/EasyQL.svg?style=flat)](https://github.com/RK900/Star-Wars/blob/master/LICENSE.txt)
[![Twitter](https://img.shields.io/badge/twitter-@RohanKoodli-blue.svg?style=flat)](http://twitter.com/RohanKoodli)

### Author
Rohan Koodli

### License
MIT

## Rey's Parents: A Data-Driven Approach
### The Problem
As Star Wars Episode VIII: The Last Jedi nears, the one question plaguing Star Wars fans is who the heck are Rey's parents? We only know her by her first name, most likely by design by JJ Abrams, as to not reveal her family. She clearly is strong with the Force, as she is able to overpower Kylo Ren and wedge Anakin's lightsaber out of the ice during their duel on Starkiller Base. Also, we see during her vision in Maz Kanata's castle that she was abandoned on Jakku by a ship. The young Rey screams as the ship flies away and as Unkar Plutt drags her away.

The theories and all are insightful, but I wanted a data-driven approach to this problem. Hence, this repository.

### The Approach
I looked online to find midichlorian counts of various characters. I found [this Quora post](https://www.quora.com/What-is-Luke-Skywalkers-midichlorian-count-How-does-his-count-compare-to-other-Jedis) to be especially useful. To predict Rey's parents, I trained a machine learning model on how midichlorian counts (MC) have changed over generations. For example, Kylo Ren's mother is Leia, and Leia's father is Anakin. 

```
Anakin Skywalker (Darth Vader) -> Leia Organa -> Ben Solo (Kylo Ren)
```

The model learned how the midichlorian counts in the Skywalker family changed over time. To add more data, I did some data augmentation to increase the number of training samples and made my model more robust.

Since Rey's MC is unknown, I varied the counts, using MC that I felt were reasonable. Then, I ran the model using my training samples.

### Results
Most of the time, Rey's parent's MC ranged from 20,000 to about 22,000. These values were obtained using multiple different guesses for Rey's MC. The closest match for 20,000 to 22,000 midichlorians is...Emperor Palpatine! I was surprised by this result, as I was expecting either Luke or Han. Regardless, this was a fun personal project to undertake. Comments, questions and suggestions are welcome. The code is available in this [GitHub repository](https://github.com/RK900/Star-Wars). If you know of any more MCs for characters, feel free to open a pull request or issue. I look forward to seeing if this is confirmed in Episode VIII.

### Update - Jan 2, 2018
In _The Last Jedi_, Kylo Ren reveals that Rey's parents were "nobodys", they sold off Rey. I'm still unsure of whether he was telling the truth (why would Rey's parents sell her off when in her vision in _The Force Awakens_ they flew off in their own ship?). This model cannot compensate for the fact that Rey's parents are nobodys; the underlying assumption is that she is somewhat related to previous characters.

### Update 2 - 2020
Well, whaddaya know? In _The Rise of Skywalker_, Palpatine is indeed revealed to be an ancestor of Rey (her grandfather) - my model's prediction was confirmed!

![](midichlorians_meme.png)
