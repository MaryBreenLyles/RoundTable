enviornment=development        # set default env to dev env
flaskTargetFile=roundtable.py  # set default served app to roundtable
port=5000                      # set default port the web server should run on

#Use get opts to take named arguments
while getopts 'e:f:p:' option
do  
  case $option in
    e) enviornment=$OPTARG ;;
    f) flaskTargetFile=$OPTARG ;;
    p) port=$OPTARG ;;
  esac
done


#Define an enviornment variable to tell the terminal what program Flask should operate with
export FLASK_APP=$flaskTargetFile  #file is an argument of f

#Put application in development mode
export FLASK_ENV=$enviornment  #environment is an argument of e

#Tell flask to start, and open it up to the local network
pipenv run flask run -h 0.0.0.0 -p $port     #running on port 5000, open to other computers (ip address 0.0.0.0)

