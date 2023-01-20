# NERD PRIME REWARDS
Automation for Rewards @ [prime.nerdunited.com](https://www.prime.nerdunited.com)
### DEPENDANCIES
1. **Python 3.10.8**
2. **ChromeDriver** *Matching Version to your OS*
  - [ChromeDriver](https://chromedriver.chromium.org/downloads)
  - Add **ChromeDriver** to the top-level directory *where .git is*.
  - Unzip **ChromeDriver**
### INSTALL
1. Install Dependancies 
`$ pip install requirements.txt`


2. Configure Variables in ***config.json***

```
"credentials": {
    "user": "<EMAIL>",
    "password": "<PASSWORD>"
  },
  "team": [
    "<FIRST> <LAST>",
    "<FIRST> <LAST>"
  ],
```
4. Run `$ python main.py`