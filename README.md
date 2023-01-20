<h1>
<img alt="prime" src="https://prime.nerdunited.com/images/prime-logo.svg" width="90">
 REWARDS
</h1>

Automation for Rewards  [prime.nerdunited.com](https://www.prime.nerdunited.com)
### DEPENDANCIES
1. **Python 3.10 >**
2. **[ChromeDriver](https://chromedriver.chromium.org/downloads)** - *Matching Version to your OS*
  - Add **ChromeDriver** to the top-level directory *where .git is*.
  - Unzip **ChromeDriver**
### INSTALL
1. Install Dependancies 
`$ pip install requirements.txt`


2. Configure Variables in ***config.json***<br/>
`credentials['team']` must be Capitalized, **ex.** `"<First> <Last>",` => `"Jace Otterson"`
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

### RUN SCRIPT
Run `$ python main.py`