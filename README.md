A django based User creation and authentication application.
<hr>
<div style="display: flex; gap: 10px;">
    <img src="https://github.com/user-attachments/assets/9c858097-872d-49ab-a02e-482fc0f3c502" alt="Image 1" style="width: 25%; max-width: 400px;" />
    <img src="https://github.com/user-attachments/assets/8736d38e-41b6-4c1c-a53b-8f5a71d15440" alt="Image 2" style="width: 25%; max-width: 400px;" />
    <img src="https://github.com/user-attachments/assets/29ccb306-1c9f-4e08-b461-727feee926c4" alt="Image 2" style="width: 25%; max-width: 400px;" />
</div>
<hr>
<b>Setup and run:</b>
<br>
1. Download the project, and open a terminal on the root folder.
<br>
2. Run the following commands:

```bash
cd authBasic
python manage.py runserver
```
<br>
<b>Note about Environment variables:</b>
<br>
In order to protect my gmail app password, EMAIL_HOST_PASSWORD <b>(in authBasic/settings.py)</b> has been secured as a system environment variable as shown below.

```
EMAIL_HOST_PASSWORD = os.environ['djangoPass']
```
