# stock-broker-interface

Error I encountered:
ERROR: (gcloud.run.deploy) PERMISSION_DENIED: Permission 'run.services.get' denied on resource 'namespaces/boreal-conquest-337614/services/stock-request' (or resource may not exist).

Cause:
cloud build account doesn't have permission

Solution:

Grant cloudbuild.gserviceaccount.com Cloud Build Editor permission

Reference:
https://stackoverflow.com/questions/62783869/why-am-i-seeing-this-error-error-gcloud-run-deploy-permission-denied-the-c