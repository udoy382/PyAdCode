# Flask 1.1.2

# step1 ==> install virtualenv ==> pip instsall virtualenv
# step2 ==> type in terminal ==> virtualenv myprojectenv

# for linux users ==> source myprojectenv/bin/activate
# for window proweshell users ==> .\myprojectenv\Scripts\activate.ps1
# deactivate virtualenv type ==> deactivate

# pip freeze ==> use this command for see all module/pkage verson
# pip freeze > requirements.txt ==> use for all verson save to .txt file
# pip install .\requirements.txt ==> this command use for install all requirements.txt, pkage in virtualenv but does not work for me

import flask
import pandas as pd
import fibo