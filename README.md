# NERD PRIME REWARDS
Automation for Rewards @ [prime.nerdunited.com](https://www.prime.nerdunited.com)
### INSTALL
1. Install Dependancies 
`$ pip install requirements.txt`
2. Download **ChromeDriver**
  - [ChromeDriver](https://chromedriver.chromium.org/downloads)
  - Add **ChromeDriver** to the top-level directory *where .git is*.
  - Unzip **ChromeDriver**

3. Configure Variables in ***config.json***

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