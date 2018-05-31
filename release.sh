python3 manage.py migrate;
if [ $RUN_UNIT_TEST == "False" ]
then
   bandit -r portalbackend;
   coverage run --source=. --omit=*/migrations/*,*/v0/*,*/python/*  manage.py test portalbackend -v 2;
   coverage report;
fi

