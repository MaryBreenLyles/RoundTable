enviornment=development        # set default env to dev env
flaskTargetFile=roundtable.py   # set default served app to roundtable

#Use get opts to take named arguments
while getopts 'e:f:' option
do  
  case $option in
    e) enviornment=$OPTARG ;;
    f) flaskTargetFile=$OPTARG ;;
  esac
done


#Define an enviornment variable to tell the terminal what program Flask should operate with
export FLASK_APP=$flaskTargetFile  #file is an argument of f

#Put application in development mode
export FLASK_ENV=$enviornment  #environment is an argument of e

#Tell flask to start, and open it up to the local network
pipenv run flask run --host=0.0.0.0

