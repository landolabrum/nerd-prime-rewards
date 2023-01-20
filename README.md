# NERD PRIME REWARDS
Automation for Rewards @ [prime.nerdunited.com](https://www.prime.nerdunited.com)
### DEPENDANCIES
1. **Python 3.10 >**
2. **[ChromeDriver](https://chromedriver.chromium.org/downloads)** - *Matching Version to your OS*
  - Add **ChromeDriver** to the top-level directory *where .git is*.
  - Unzip **ChromeDriver**
### INSTALL
1. Install Dependancies 
`$ pip install requirements.txt`


2. Configure Variables in ***config.json***
** credentials['team'] **
*- is Capitalized* **ex.** *Jace Otterson*
```
"credentials": {
    "user": "<EMAIL>",
    "password": "<PASSWORD>"
  },
  "team": [
    "<First> <Last>",
    "<First> <Last>"
  ],
```
4. Run `$ python main.py`